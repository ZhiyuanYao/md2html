#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import mistune
import sys
import re

# --- Helper Functions ---


def wrap_long_code_blocks(html_content, max_lines):
    """
    Wrap code blocks longer than max_lines in collapsible HTML structure.

    Args:
        html_content (str): HTML content with code blocks
        max_lines (int): Maximum lines before wrapping in collapsible

    Returns:
        str: HTML content with long code blocks wrapped in collapsible sections
    """
    # Counter for unique IDs
    collapse_counter = 0

    def replace_code_block(match):
        nonlocal collapse_counter

        # Extract the full code block
        full_match = match.group(0)
        start_pos = match.start()

        # Check if this code block is inside a <details> tag or existing collapsible
        # Look backwards from the match position for unclosed <details> tags
        text_before = html_content[:start_pos]

        # Count <details> tags (opening) and </details> tags (closing) before this position
        details_open = len(re.findall(
            r'<details[^>]*>', text_before, re.IGNORECASE))
        details_close = len(re.findall(
            r'</details>', text_before, re.IGNORECASE))

        # If we're inside an unclosed <details> tag, don't add additional collapse
        if details_open > details_close:
            return full_match

        # Also check for existing wrap-collabsible divs
        if '<div class="wrap-collabsible">' in text_before.split('</div>')[-1]:
            return full_match

        # Count lines in the code block
        # Look for the content between <code> and </code>
        code_content = re.search(
            r'<code[^>]*>(.*?)</code>', full_match, re.DOTALL)
        if not code_content:
            return full_match

        lines = code_content.group(1).count('\n') + 1

        # If code block is short enough, return as-is
        if lines <= max_lines:
            return full_match

        # Generate unique ID for this collapsible
        collapse_counter += 1
        collapse_id = f"code-collapse-{collapse_counter}"

        # Extract language from class attribute if present
        lang_match = re.search(r'class="[^"]*language-([^"\s]+)', full_match)
        language = lang_match.group(1) if lang_match else "code"

        # Special handling for JSON - if it looks like JSON but uses javascript class, show as JSON
        if language == "javascript":
            # Check if the content looks like JSON (starts with { or [, has quotes around keys)
            content_text = code_content.group(1).strip()
            if re.search(r'^\s*[\{\[]', content_text) and re.search(r'"[^"]+"\s*:', content_text):
                language = "json"

        # Create collapsible wrapper (Prism.js will add toolbar automatically)
        collapsible_html = f'''<div class="wrap-content-collapsible">
    <input id="{collapse_id}" class="toggle" type="checkbox">
    <label for="{collapse_id}" class="lbl-toggle">{language.upper()} ({lines} lines)</label>
    <div class="content-collapsible-content">
        <div class="content-inner">
{full_match}
        </div>
    </div>
</div>'''

        return collapsible_html

    # Find and replace code blocks
    # Pattern matches <pre><code>...</code></pre> structures
    pattern = r'<pre[^>]*><code[^>]*>.*?</code></pre>'
    result = re.sub(pattern, replace_code_block, html_content, flags=re.DOTALL)

    return result


def create_mistune_with_toc():
    """
    Create mistune markdown parser with native TOC hook support.
    
    Returns:
        mistune.Markdown: Configured markdown parser with TOC support
    """
    from mistune.toc import add_toc_hook
    
    # Create basic mistune markdown parser
    md = mistune.create_markdown(
        escape=False,
        plugins=['strikethrough', 'table', 'footnotes', 'task_lists']
    )
    
    # Add native TOC hook for extracting headers
    add_toc_hook(md)
    
    return md


def convert_toc_ids_to_slugs(html_body, toc_items, md_text):
    """
    Convert toc_N style IDs to user-specified slug IDs found in markdown links.
    
    Args:
        html_body (str): HTML content with toc_N IDs
        toc_items (list): List of (level, anchor, title) tuples
        md_text (str): Original markdown text to extract link slugs from
        
    Returns:
        str: HTML with user-specified slug IDs
    """
    import re
    
    # Extract all markdown links and their targets
    link_pattern = r'\[([^\]]+)\]\(#([^)]+)\)'
    links = re.findall(link_pattern, md_text)
    
    # Create mapping of link text to slug
    text_to_slug = {}
    for link_text, slug in links:
        text_to_slug[link_text.strip()] = slug
    
    # Convert toc_N IDs to user-specified slugs
    for level, anchor, title in toc_items:
        # Look for user-provided slug for this title
        user_slug = text_to_slug.get(title)
        if user_slug:
            # Replace both the header ID and any TOC links with user's slug
            html_body = html_body.replace(f'id="{anchor}"', f'id="{user_slug}"')
            html_body = html_body.replace(f'href="#{anchor}"', f'href="#{user_slug}"')
    
    return html_body


def render_toc_ul_with_symbols(toc_items):
    """
    Custom TOC renderer that adds different list symbols for different levels with proper nesting.
    """
    symbols = ['', '●', '○', '▪', '▫', '▸', '▹']
    
    if not toc_items:
        return ''
    
    html = []
    current_level = 0
    open_lists = []
    
    for level, anchor, title in toc_items:
        symbol = symbols[(level - 1) % len(symbols)]
        
        # Close lists if we're at a shallower level
        while current_level > level:
            html.append('  ' * (current_level - 1) + '</ul>')
            open_lists.pop()
            current_level -= 1
        
        # Open new lists if we're at a deeper level
        while current_level < level:
            html.append('  ' * current_level + '<ul>')
            open_lists.append(level)
            current_level += 1
        
        # Add the list item
        indent = '  ' * (level - 1)
        html.append(f'{indent}  <li><span class="toc-symbol" data-level="{level}">{symbol}</span><a href="#{anchor}">{title}</a></li>')
    
    # Close all remaining lists
    while open_lists:
        current_level -= 1
        html.append('  ' * current_level + '</ul>')
        open_lists.pop()
    
    return '\n'.join(html) + '\n'


def process_toc_with_native_mistune(md_text):
    """
    Process markdown with native mistune TOC functions, 
    excluding headers before [TOC] placeholder.
    
    Args:
        md_text (str): Markdown text with [TOC] placeholders
        
    Returns:
        tuple: (html_content, toc_items_after_toc)
    """
    if '[TOC]' not in md_text:
        # No TOC requested, use regular processing
        md = mistune.create_markdown(
            escape=False,
            plugins=['strikethrough', 'table', 'footnotes', 'task_lists']
        )
        return md(md_text), []
    
    import re
    from mistune.toc import add_toc_hook, render_toc_ul
    
    # Create mistune with TOC hook - use basic mistune, not the wrapper
    md = mistune.create_markdown(
        escape=False,
        plugins=['strikethrough', 'table', 'footnotes', 'task_lists']
    )
    add_toc_hook(md, min_level=1, max_level=5)
    
    # Find position of [TOC] in the original markdown
    toc_position = md_text.find('[TOC]')
    lines_before_toc = md_text[:toc_position].count('\n')
    
    # Replace [TOC] with a placeholder that will survive markdown processing
    toc_placeholder = '<!--TOC_PLACEHOLDER-->'
    temp_md_text = md_text.replace('[TOC]', toc_placeholder)
    
    # Parse the markdown to get TOC items
    html_content, state = md.parse(temp_md_text)
    
    # Get all TOC items
    all_toc_items = state.env.get('toc_items', [])
    
    # Get header positions in original markdown
    header_lines = {}
    for line_num, line in enumerate(md_text.split('\n')):
        if re.match(r'^#+\s', line):
            header_text = re.sub(r'^#+\s*', '', line).strip()
            header_lines[header_text] = line_num
    
    # Filter toc_items to only include those after TOC position
    filtered_toc_items = []
    for level, anchor, title in all_toc_items:
        # Check if this header appears after the TOC in the original text
        if title in header_lines and header_lines[title] > lines_before_toc:
            filtered_toc_items.append((level, anchor, title))
    
    # Generate TOC HTML using native render_toc_ul with custom symbols
    if filtered_toc_items:
        toc_html = '<div class="toc">'
        toc_html += render_toc_ul_with_symbols(filtered_toc_items)
        toc_html += '</div>'
    else:
        toc_html = ''
    
    # Replace the placeholder with actual TOC HTML
    html_content = html_content.replace(toc_placeholder, toc_html)
    
    # Also handle case where placeholder got wrapped in <p> tags
    html_content = html_content.replace(f'<p>{toc_placeholder}</p>', toc_html)
    
    return html_content, filtered_toc_items


def add_toc_css():
    """
    Generate CSS for mistune's native table of contents styling.
    
    Returns:
        str: CSS styles for TOC generated by mistune
    """
    return """
/* Table of Contents Styling - simple div without title */
div.toc {
    background-color: #f8f9fa;
    border: 1px solid #e1e5e9;
    border-radius: 6px;
    padding: 12px;
    margin: 20px 0;
    max-width: 100%;
    width: 100%;
}

div.toc ul {
    list-style: none;
    padding-left: 0;
    margin: 0;
}

div.toc ul ul {
    padding-left: 20px;
    margin: 4px 0;
}

div.toc .toc-symbol {
    margin-right: 4px;
    color: #666;
    display: inline-flex;
    align-items: center;
    vertical-align: baseline;
}

div.toc .toc-symbol[data-level="2"],
div.toc .toc-symbol[data-level="3"] {
    font-size: 0.5em;
    transform: translateY(-2px);
}

div.toc .toc-symbol[data-level="4"],
div.toc .toc-symbol[data-level="5"] {
    font-size: 1.2em;
    transform: translateY(1px);
}

div.toc li {
    margin: 3px 0;
    line-height: 1.4;
}

div.toc a {
    color: #0066cc;
    text-decoration: none;
    display: inline-block;
    padding: 2px 6px;
    border-radius: 4px;
    transition: all 0.2s ease;
    font-size: 1.0em;
}

div.toc a:hover {
    background-color: #e3f2fd;
    text-decoration: none;
    color: #004494;
}

/* Smooth scrolling to anchors */
html {
    scroll-behavior: smooth;
}

/* Style for targeted headers (when clicked from TOC) */
h1:target, h2:target, h3:target, h4:target, h5:target, h6:target {
    scroll-margin-top: 20px;
    animation: highlight-flash 2s ease-out;
}

@keyframes highlight-flash {
    0% { background-color: #fff3cd; }
    100% { background-color: transparent; }
}
"""


# --- HTML Template ---
# This template wraps the converted Markdown content and includes placeholders
# for the title, custom CSS, and the code highlighting CSS.
HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    
    <!-- MathJax Configuration and Loading - NOTE: Requires internet for LaTeX rendering -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({{
      tex2jax: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true,
        processEnvironments: true,
        processClass: "math"
      }},
      "HTML-CSS": {{ 
        linebreaks: {{ automatic: true }},
        scale: 90
      }}
    }});
    </script>
    <script type="text/javascript" async
      src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
    </script>

    <!-- Prism.js for Code Highlighting - 100% offline with embedded theme -->
    <!-- Modern CSS frameworks for cross-platform support -->
    <style>
/* Normalize.css for consistent cross-browser rendering */
{normalize_css}

/* Modern base styles with CSS variables and accessibility */
{modern_base_css}

/* Mobile-responsive styles */
{mobile_responsive_css}

/* Prism {prism_theme} theme - embedded for offline use */
{prism_theme_css}
    </style>
    {line_numbers_css}
    <!-- Copy the exact prism.js that demo.html uses -->
    <script>
{prism_js_content}
    </script>
    <script>
        // Ensure Prism highlights all code blocks when page loads
        document.addEventListener('DOMContentLoaded', function() {{
            Prism.highlightAll();
        }});
    </script>

    <style>
{custom_css}
    </style>
</head>
<body{body_class}>
    <div id="__next">
        <div id="page-ctn">
            <header id="page-header">
                <h3></h3>
            </header>
            <section class="markdown-body">
{html_body}
            </section>
        </div>
    </div>
    
    <!-- Section folding JavaScript is included by the folding function -->
</body>
</html>"""


def download_all_prism_themes():
    """Download and cache all available Prism themes for offline use."""
    # Official Prism themes from CDNJS
    official_themes = [
        'prism', 'prism-dark', 'prism-funky', 'prism-okaidia',
        'prism-twilight', 'prism-coy', 'prism-solarizedlight',
        'prism-tomorrow'
    ]

    # Popular editor themes from prism-themes repository
    prism_themes = [
        'prism-one-dark', 'prism-gruvbox-dark', 'prism-gruvbox-light',
        'prism-material-dark', 'prism-material-light', 'prism-material-oceanic',
        'prism-nord', 'prism-night-owl', 'prism-shades-of-purple',
        'prism-dracula', 'prism-atom-dark', 'prism-base16-ateliersulphurpool.light',
        'prism-cb', 'prism-duotone-dark', 'prism-duotone-earth', 'prism-duotone-forest',
        'prism-duotone-light', 'prism-duotone-sea', 'prism-duotone-space',
        'prism-ghcolors', 'prism-hopscotch', 'prism-pojoaque', 'prism-vs',
        'prism-xonokai', 'prism-z-touch'
    ]

    import urllib.request
    import os

    os.makedirs('.prism', exist_ok=True)
    downloaded = 0

    # Download official themes
    for theme in official_themes:
        cache_file = f".prism/theme-{theme}.css"
        if not os.path.exists(cache_file):
            try:
                theme_url = f"https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/{theme}.min.css"
                print(f"Downloading official theme: {theme}")
                with urllib.request.urlopen(theme_url) as response:
                    theme_css = response.read().decode('utf-8')

                with open(cache_file, 'w', encoding='utf-8') as f:
                    f.write(theme_css)
                downloaded += 1
            except Exception as e:
                print(f"Failed to download {theme}: {e}")

    # Download prism-themes repository themes
    for theme in prism_themes:
        cache_file = f".prism/theme-{theme}.css"
        if not os.path.exists(cache_file):
            try:
                # prism-themes uses different URL structure
                theme_name = theme.replace('prism-', '')
                theme_url = f"https://cdn.jsdelivr.net/npm/prism-themes@1.9.0/themes/{theme}.css"
                print(f"Downloading prism-themes: {theme}")
                with urllib.request.urlopen(theme_url) as response:
                    theme_css = response.read().decode('utf-8')

                with open(cache_file, 'w', encoding='utf-8') as f:
                    f.write(theme_css)
                downloaded += 1
            except Exception as e:
                print(f"Failed to download {theme}: {e}")

    print(
        f"Downloaded {downloaded} new themes. All themes are now cached locally!")
    print(f"Total available themes: {len(official_themes + prism_themes)}")
    print("Popular editor themes now available: one-dark, gruvbox-dark, gruvbox-light, material-dark, nord, night-owl, dracula")


def add_universal_section_folding(html_content, default_collapsed_sections=None, is_dark_theme=False):
    """
    Simple section folding using JavaScript DOM manipulation instead of complex HTML parsing.
    This avoids breaking existing HTML structure and code blocks.

    Args:
        html_content (str): HTML content with headers  
        default_collapsed_sections (list): Section titles that start collapsed (default: ["Solution"])
        is_dark_theme (bool): Whether to apply dark theme to code blocks (default: False)

    Returns:
        str: HTML content with collapsible sections added via JavaScript
    """
    if default_collapsed_sections is None:
        default_collapsed_sections = ["Solution", "Answer"]

    # Convert collapsed sections list to JavaScript array
    collapsed_sections_js = str(default_collapsed_sections).replace("'", '"')

    # Add JavaScript that will process the DOM after page load
    folding_script = f'''
    
    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        const collapsedSections = {collapsed_sections_js};
        const isDarkTheme = {str(is_dark_theme).lower()};
        
        // Apply dark theme only to pre code blocks if needed
        if (isDarkTheme) {{
            const codeBlocks = document.querySelectorAll('pre');
            codeBlocks.forEach(function(pre) {{
                pre.classList.add('dark-theme');
            }});
        }}
        
        // Check table widths and apply reduced padding if they exceed 70% of content width
        const markdownBody = document.querySelector('.markdown-body');
        const contentWidth = 700; // markdown-body width is 700px
        const threshold = contentWidth * 0.7; // 70% = 490px
        
        const tables = document.querySelectorAll('.markdown-body table');
        tables.forEach(function(table) {{
            // Force table layout to calculate natural width
            table.style.width = 'auto';
            
            // Get the actual rendered width of the table
            const tableWidth = table.getBoundingClientRect().width;
            
            if (tableWidth > threshold) {{
                // Table exceeds 70% of content width, reduce padding
                const ths = table.querySelectorAll('th');
                const tds = table.querySelectorAll('td');
                
                ths.forEach(function(th) {{
                    th.style.padding = '12px 20px';
                }});
                
                tds.forEach(function(td) {{
                    td.style.padding = '11px 20px';
                }});
            }}
        }});
        
        // Find all headers h2-h6
        const headers = document.querySelectorAll('.markdown-body h2, .markdown-body h3, .markdown-body h4, .markdown-body h5, .markdown-body h6');
        
        headers.forEach(function(header, index) {{
            // Skip headers inside code blocks
            if (header.closest('pre, code')) {{
                return;
            }}
            
            const level = parseInt(header.tagName.substring(1));
            const text = header.textContent;
            const sectionId = 'section-' + index;
            
            // Check if this section should be collapsed by default (exact match only)
            const isCollapsed = collapsedSections.some(section => 
                text.toLowerCase().trim() === section.toLowerCase().trim()
            );
            
            // Create wrapper div for the header
            const headerDiv = document.createElement('div');
            headerDiv.className = 'section-collapsible-header ' + (isCollapsed ? 'collapsed' : 'expanded');
            headerDiv.onclick = function() {{ toggleSection(sectionId); }};
            
            // Create collapse icon
            const icon = document.createElement('span');
            icon.className = 'collapse-icon';
            icon.innerHTML = '⌄';
            
            // Replace header with wrapped version
            header.parentNode.insertBefore(headerDiv, header);
            headerDiv.appendChild(header);
            headerDiv.appendChild(icon);
            
            // Create content div and collect content until next same-level header
            const contentDiv = document.createElement('div');
            contentDiv.className = 'section-collapsible-content ' + (isCollapsed ? 'collapsed' : 'expanded');
            contentDiv.id = sectionId;
            
            let nextElement = headerDiv.nextElementSibling;
            while (nextElement) {{
                // Stop at next header of same or higher level
                if (nextElement.tagName && nextElement.tagName.match(/^H[1-6]$/)) {{
                    const nextLevel = parseInt(nextElement.tagName.substring(1));
                    if (nextLevel <= level) {{
                        break;
                    }}
                }}
                
                const elementToMove = nextElement;
                nextElement = nextElement.nextElementSibling;
                contentDiv.appendChild(elementToMove);
            }}
            
            // Insert content div after header
            headerDiv.parentNode.insertBefore(contentDiv, headerDiv.nextElementSibling);
        }});
    }});
    
    function toggleSection(sectionId) {{
        const content = document.getElementById(sectionId);
        const header = content.previousElementSibling;
        
        if (content.classList.contains('collapsed')) {{
            content.classList.remove('collapsed');
            content.classList.add('expanded');
            header.classList.remove('collapsed');
            header.classList.add('expanded');
        }} else {{
            content.classList.remove('expanded');
            content.classList.add('collapsed');
            header.classList.remove('expanded');
            header.classList.add('collapsed');
        }}
    }}
    </script>'''

    return html_content + folding_script


def convert_md_to_html(md_file_path, css_file_path='style.css', prism_theme='prism', line_numbers=False, collapse_lines=10, inline_lang='python', foldable_sections=None, toc=False):
    """
    Converts a Markdown file to a full HTML document with styling.

    Args:
        md_file_path (str): Path to the input Markdown file.
        css_file_path (str, optional): Path to a custom CSS file. Defaults to 'style.css'.
        prism_theme (str, optional): Prism.js theme name. Defaults to 'prism'.
        line_numbers (bool, optional): Enable line numbers in code blocks. Defaults to False.
        collapse_lines (int, optional): Auto-collapse code blocks longer than this many lines. Defaults to 10.
        inline_lang (str, optional): Language for highlighting inline code. Defaults to 'python'.
        toc (bool, optional): Auto-generate a TOC section if --toc is used. Defaults to False.

    Returns:
        str: A complete HTML document as a string.
    """
    # --- 0. Handle theme aliases ---
    theme_aliases = {
        'one-dark': 'prism-one-dark',
        'gruvbox-dark': 'prism-gruvbox-dark',
        'gruvbox-light': 'prism-gruvbox-light',
        'material-dark': 'prism-material-dark',
        'material-light': 'prism-material-light',
        'material-oceanic': 'prism-material-oceanic',
        'nord': 'prism-nord',
        'night-owl': 'prism-night-owl',
        'dracula': 'prism-dracula',
        'atom-dark': 'prism-atom-dark',
        'dark': 'prism-dark',
        'okaidia': 'prism-okaidia',
        'tomorrow': 'prism-tomorrow',
        'twilight': 'prism-twilight',
        'coy': 'prism-coy',
        'solarizedlight': 'prism-solarizedlight',
        'funky': 'prism-funky'
    }

    # Convert short names to full prism theme names
    if prism_theme in theme_aliases:
        prism_theme = theme_aliases[prism_theme]

    # Determine if this is a dark theme - but don't apply to body
    dark_themes = [
        'prism-one-dark', 'prism-gruvbox-dark', 'prism-material-dark', 'prism-nord',
        'prism-night-owl', 'prism-dracula', 'prism-atom-dark', 'prism-dark',
        'prism-okaidia', 'prism-twilight', 'prism-material-oceanic', 'prism-tomorrow'
    ]
    is_dark_theme = prism_theme in dark_themes

    # --- 1. Read input files ---
    try:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
    except FileNotFoundError:
        print(f"Error: Input Markdown file not found at '{md_file_path}'")
        sys.exit(1)

    custom_css = ""
    try:
        with open(css_file_path, 'r', encoding='utf-8') as f:
            custom_css = f.read()
    except FileNotFoundError:
        print(
            f"Warning: Custom CSS file not found at '{css_file_path}'. Proceeding without it.")

    # Read the exact prism.js that demo.html uses
    prism_js_content = ""
    try:
        with open('.prism/prism.js', 'r', encoding='utf-8') as f:
            prism_js_content = f.read()
    except FileNotFoundError:
        print(f"Warning: Local prism.js not found. Using fallback CDN approach.")
        prism_js_content = ""

    # Load cached Prism theme CSS for 100% offline support
    prism_theme_css = ""
    cache_file = f".prism/theme-{prism_theme}.css"
    try:
        with open(cache_file, 'r', encoding='utf-8') as f:
            prism_theme_css = f.read()
    except FileNotFoundError:
        print(
            f"Warning: Theme '{prism_theme}' not found in cache. Run 'python converter.py --download-themes' first.")
        prism_theme_css = ""

    # Load modern CSS frameworks for cross-platform support
    normalize_css = ""
    modern_base_css = ""
    mobile_responsive_css = ""

    try:
        with open('.prism/normalize.css', 'r', encoding='utf-8') as f:
            normalize_css = f.read()
    except FileNotFoundError:
        print(
            "Warning: normalize.css not found. Cross-browser consistency may be affected.")

    try:
        with open('.prism/modern-base.css', 'r', encoding='utf-8') as f:
            modern_base_css = f.read()
    except FileNotFoundError:
        print("Warning: modern-base.css not found. Modern styling may be affected.")

    try:
        with open('.prism/mobile-responsive.css', 'r', encoding='utf-8') as f:
            mobile_responsive_css = f.read()
    except FileNotFoundError:
        print("Warning: mobile-responsive.css not found. Mobile support may be limited.")

    # --- 2. Mistune handles extensions via plugins ---
    # No complex extension configuration needed - mistune is simpler
    # TOC functionality will be handled separately if needed

    # Configure line numbers but don't add theme classes to body
    if line_numbers:
        line_numbers_css = '<link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.css" rel="stylesheet" />'
        line_numbers_js = '<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.js"></script>'
        body_class = ' class="line-numbers"'
    else:
        line_numbers_css = ''
        line_numbers_js = ''
        body_class = ''

    # --- 3. Convert Markdown to an HTML fragment with proper math handling ---
    # Temporarily replace math expressions with placeholders (like md_to_html.py does)
    import re
    math_expressions = []

    def replace_math(match):
        math_expressions.append(match.group(0))
        return f"MATHPLACEHOLDER{len(math_expressions)-1}MATHPLACEHOLDER"

    # Function to check if a match is inside backticks
    def is_inside_backticks(text, match_start, match_end):
        # Count backticks before the match on the same line
        line_start = text.rfind('\n', 0, match_start) + 1
        line_text = text[line_start:match_start]
        backtick_count = line_text.count('`')
        # If odd number of backticks before match, we're inside code
        return backtick_count % 2 == 1
    
    def safe_replace_math(pattern, text, flags=0):
        result = []
        last_end = 0
        for match in re.finditer(pattern, text, flags):
            if not is_inside_backticks(text, match.start(), match.end()):
                # Not inside backticks, safe to replace
                result.append(text[last_end:match.start()])
                math_expressions.append(match.group(0))
                result.append(f"MATHPLACEHOLDER{len(math_expressions)-1}MATHPLACEHOLDER")
            else:
                # Inside backticks, keep original
                result.append(text[last_end:match.end()])
            last_end = match.end()
        result.append(text[last_end:])
        return ''.join(result)

    # Replace display math first ($$...$$ and \[...\] - can span lines), then inline math ($...$ and \(...\)), then standalone \boxed{}
    temp_md_text = safe_replace_math(r'\$\$([^$]+?)\$\$', md_text, re.DOTALL)
    temp_md_text = safe_replace_math(r'\\\[(.+?)\\\]', temp_md_text, re.DOTALL)
    temp_md_text = safe_replace_math(r'\\\((.+?)\\\)', temp_md_text)
    temp_md_text = safe_replace_math(r'\$([^$\n]+?)\$', temp_md_text)
    # Capture standalone \boxed{...} expressions (not already inside math delimiters)
    # Use a function to match nested braces properly with backtick protection
    def match_boxed(text):
        result = text
        # Find \boxed{ and match the corresponding closing brace
        start = 0
        while True:
            match_start = result.find('\\boxed{', start)
            if match_start == -1:
                break
            
            # Find the matching closing brace
            brace_count = 0
            pos = match_start + 7  # Start after '\boxed{'
            while pos < len(result):
                if result[pos] == '{':
                    brace_count += 1
                elif result[pos] == '}':
                    if brace_count == 0:
                        # Found the matching closing brace
                        match_end = pos + 1
                        # Check if this match is inside backticks
                        if not is_inside_backticks(result, match_start, match_end):
                            full_expression = result[match_start:match_end]
                            math_expressions.append(full_expression)
                            placeholder = f"MATHPLACEHOLDER{len(math_expressions)-1}MATHPLACEHOLDER"
                            result = result[:match_start] + placeholder + result[match_end:]
                            start = match_start + len(placeholder)
                        else:
                            start = match_end
                        break
                    else:
                        brace_count -= 1
                pos += 1
            else:
                # No matching closing brace found, skip this one
                start = match_start + 7
        
        return result
    
    temp_md_text = match_boxed(temp_md_text)

    # Preprocess markdown to fix table formatting issues
    # Add blank lines before tables that don't have them
    def fix_table_formatting(text):
        lines = text.split('\n')
        fixed_lines = []

        def is_table_header(line):
            """Check if line looks like a table header row."""
            stripped = line.strip()
            if not stripped or not stripped.startswith('|') or not stripped.endswith('|'):
                return False
            # Count pipe symbols - should have at least 3 (start + separators + end)
            pipe_count = stripped.count('|')
            return pipe_count >= 3

        def is_table_separator(line):
            """Check if line looks like a table separator row."""
            stripped = line.strip()
            if not stripped or not stripped.startswith('|') or not stripped.endswith('|'):
                return False
            # Should contain dashes and optionally colons for alignment
            content_between_pipes = stripped[1:-1]  # Remove outer pipes
            cells = [cell.strip() for cell in content_between_pipes.split('|')]

            # Each cell should be a combination of dashes, colons, and spaces
            for cell in cells:
                if not cell:  # Empty cell
                    continue
                # Valid separator cell contains only dashes, colons, and spaces
                if not all(c in '-: ' for c in cell):
                    return False
                # Must contain at least one dash
                if '-' not in cell:
                    return False
            return len(cells) >= 2  # At least 2 columns

        for i, line in enumerate(lines):
            # Check if this line looks like a table header
            if is_table_header(line):
                # Verify next line is separator row
                if (i + 1 < len(lines) and is_table_separator(lines[i + 1])):
                    # This is definitely a table start
                    # Check if previous line exists and is not blank
                    if i > 0 and lines[i - 1].strip() != '':
                        # Add blank line before table
                        fixed_lines.append('')

            # Also check for table separator rows (handle cases where header detection missed)
            elif is_table_separator(line):
                # Look back to see if previous line could be a table header
                if (i > 0 and is_table_header(lines[i - 1])):
                    # Previous line is a header, check if we need spacing before it
                    if i > 1 and lines[i - 2].strip() != '':
                        # Need to insert blank line before the header (which is already in fixed_lines)
                        # Remove the header from fixed_lines and re-add with spacing
                        if fixed_lines and len(fixed_lines) >= 2:
                            # Check if the line before the header (in fixed_lines) is not blank
                            if len(fixed_lines) >= 2 and fixed_lines[-2].strip() != '':
                                header_line = fixed_lines.pop()  # Remove header
                                fixed_lines.append('')  # Add blank line
                                fixed_lines.append(
                                    header_line)  # Re-add header

            fixed_lines.append(line)

        return '\n'.join(fixed_lines)

    temp_md_text = fix_table_formatting(temp_md_text)

    # Auto-generate TOC section if --toc argument is provided
    if toc and '[TOC]' not in temp_md_text:
        lines = temp_md_text.split('\n')
        toc_inserted = False
        
        # Strategy: Insert TOC before the first content section (level 2+ header)
        # This preserves the document title and intro paragraphs
        for i, line in enumerate(lines):
            if line.startswith('##') and not toc_inserted:  # Level 2+ header (main content)
                # Insert TOC before this section
                lines.insert(i, '')
                lines.insert(i + 1, '## Table of Contents')
                lines.insert(i + 2, '[TOC]')
                lines.insert(i + 3, '')
                toc_inserted = True
                break
        
        if not toc_inserted:
            # No level 2+ headers found, look for any header
            for i, line in enumerate(lines):
                if line.startswith('#') and not toc_inserted:
                    # Insert TOC after the first header
                    lines.insert(i + 1, '')
                    lines.insert(i + 2, '## Table of Contents')
                    lines.insert(i + 3, '[TOC]')
                    lines.insert(i + 4, '')
                    toc_inserted = True
                    break
        
        if not toc_inserted:
            # No headers found, insert after any intro content
            # Find the end of the intro (empty line followed by content)
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.strip() == '' and i + 1 < len(lines) and lines[i + 1].strip() != '':
                    insert_pos = i + 1
                    break
            
            lines.insert(insert_pos, '## Table of Contents')
            lines.insert(insert_pos + 1, '[TOC]')
            lines.insert(insert_pos + 2, '')
        
        temp_md_text = '\n'.join(lines)

    # === ALL COMPLEX LIST PROCESSING REMOVED ===
    # Let mistune handle all list rendering naturally - much simpler and more reliable

    # Simple preprocessing - only handle math expressions protection
    # No complex list processing - let mistune handle lists naturally

    # Convert markdown to HTML - always use mistune with TOC hooks for header IDs
    if '[TOC]' in temp_md_text:
        html_body, toc_items = process_toc_with_native_mistune(temp_md_text)
        # Apply user-specified slug IDs for TOC path as well
        if toc_items:
            html_body = convert_toc_ids_to_slugs(html_body, toc_items, temp_md_text)
    else:
        # Process without visible TOC but still need IDs on headers for internal links
        from mistune.toc import add_toc_hook
        mistune_md = mistune.create_markdown(
            escape=False,
            plugins=['strikethrough', 'table', 'footnotes', 'task_lists']
        )
        add_toc_hook(mistune_md, min_level=1, max_level=6)
        html_body, state = mistune_md.parse(temp_md_text)
        
        # Post-process to convert toc_N IDs to user-specified slug IDs
        toc_items = state.env.get('toc_items', [])
        if toc_items:
            html_body = convert_toc_ids_to_slugs(html_body, toc_items, temp_md_text)

    # Restore math expressions as proper MathJax script tags
    def restore_math(match):
        index = int(match.group(1))
        original_math = math_expressions[index]
        if original_math.startswith('$$'):
            # Display math with $$ delimiters
            content = original_math[2:-2]
            return f'<script type="math/tex; mode=display">{content}</script>'
        elif original_math.startswith('\\['):
            # Display math with \[ \] delimiters
            content = original_math[2:-2]
            return f'<script type="math/tex; mode=display">{content}</script>'
        elif original_math.startswith('\\boxed'):
            # Standalone \boxed{...} as display math
            return f'<script type="math/tex; mode=display">{original_math}</script>'
        elif original_math.startswith('\\('):
            # Inline math with \( \) delimiters
            content = original_math[2:-2]
            return f'<script type="math/tex">{content}</script>'
        else:
            # Inline math with $ delimiters
            content = original_math[1:-1]
            return f'<script type="math/tex">{content}</script>'

    html_body = re.sub(r'MATHPLACEHOLDER(\d+)MATHPLACEHOLDER',
                       restore_math, html_body)

    # Add Topic and Thumbnail admonition styling for Problem sections
    def add_topic_thumbnail_admonitions(html_content):
        """
        Convert Topic and Thumbnail pairs under Problem sections to a single orange admonition.

        Example:
        **Topic**: Multicritical points (123)
        **Thumbnail**: Description text

        Becomes:
        <div class="admonition orange">
            <p class="admonition-orange">Multicritical points (123)</p>
            Description text
        </div>
        """
        import re

        # Pattern to match Topic followed by Thumbnail
        pattern = r'<p><strong>Topic</strong>:\s*(.*?)</p>\s*<p><strong>Thumbnail</strong>:\s*(.*?)</p>'

        def replace_with_combined_admonition(match):
            # Content of Topic (becomes title)
            topic_content = match.group(1)
            # Content of Thumbnail (becomes body)
            thumbnail_content = match.group(2)

            return f'''<div class="admonition-wrapper">
        <div class="admonition orange">
            <p class="admonition-orange">{topic_content}</p>
            {thumbnail_content}
        </div>
    </div>'''

        # Also handle cases where there's only Topic (no Thumbnail)
        pattern_topic_only = r'<p><strong>Topic</strong>:\s*(.*?)</p>(?!\s*<p><strong>Thumbnail</strong>)'

        def replace_topic_only(match):
            topic_content = match.group(1)
            return f'''<div class="admonition-wrapper">
        <div class="admonition orange">
            <p class="admonition-orange">{topic_content}</p>
        </div>
    </div>'''

        # First handle Topic+Thumbnail pairs, then handle standalone Topics
        html_content = re.sub(
            pattern, replace_with_combined_admonition, html_content, flags=re.DOTALL)
        html_content = re.sub(
            pattern_topic_only, replace_topic_only, html_content, flags=re.DOTALL)

        return html_content

    html_body = add_topic_thumbnail_admonitions(html_body)

    # --- 4. Auto-collapse long code blocks if specified ---
    if collapse_lines:
        html_body = wrap_long_code_blocks(html_body, collapse_lines)

    # --- 4.5. Add universal section folding functionality ---
    if foldable_sections is not None:
        html_body = add_universal_section_folding(
            html_body, foldable_sections, is_dark_theme)

    # --- 4.6. Convert JSON code blocks to use JavaScript highlighting ---
    # Replace language-json with language-javascript for Prism compatibility
    html_body = html_body.replace(
        'class="language-json"', 'class="language-javascript"')

    # --- 4.5. Add language class to inline code for highlighting ---
    if inline_lang:
        # Replace inline code with language-specific classes for Prism.js highlighting
        # Matches <code>...</code> that are NOT inside <pre> tags
        def add_inline_lang(match):
            code_content = match.group(1)
            # Convert JSON to javascript for Prism highlighting (since JSON isn't in our bundle)
            highlight_lang = "javascript" if inline_lang == "json" else inline_lang
            return f'<code class="language-{highlight_lang}">{code_content}</code>'

        # Only replace code tags that are not preceded by <pre> (inline code)
        # This regex finds <code>content</code> not preceded by <pre> on the same line
        html_body = re.sub(
            r'(?<!<pre>)<code>([^<]+)</code>', add_inline_lang, html_body)

    # --- 4.5. Prism.js will automatically add toolbar to code blocks ---
    # No manual wrapping needed

    # --- 5. Prism.js handles code highlighting via CDN ---
    # No need to generate CSS for code highlighting

    # Extract title from the first H1 tag, or use filename
    title = md_file_path.split('/')[-1].split('.')[0].replace('_', ' ').title()
    if '<h1>' in html_body:
        title = html_body.split('<h1>')[1].split('</h1>')[0]

    # --- 6. Assemble the final HTML document ---
    # Add TOC CSS if TOC is present in the content
    if '[TOC]' in temp_md_text:
        custom_css += add_toc_css()
    
    final_html = HTML_TEMPLATE.format(
        title=title,
        custom_css=custom_css,
        html_body=html_body,
        prism_theme=prism_theme,
        prism_theme_css=prism_theme_css,
        normalize_css=normalize_css,
        modern_base_css=modern_base_css,
        mobile_responsive_css=mobile_responsive_css,
        line_numbers_css=line_numbers_css,
        line_numbers_js=line_numbers_js,
        body_class=body_class,
        prism_js_content=prism_js_content
    )

    return final_html


def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert a Markdown file to a styled HTML document.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("input_file", nargs='?',
                        help="Path to the input Markdown file (.md).")
    parser.add_argument("output_file", nargs='?',
                        help="Path for the output HTML file (.html). If not provided, uses input filename with .html extension.")
    parser.add_argument(
        "--css",
        default=".prism/style.css",
        help="Path to a custom CSS file to include (default: style.css)."
    )
    parser.add_argument(
        "--theme",
        default="prism",
        help="Prism.js theme for code highlighting.\nShort names: gruvbox-dark, one-dark, nord, dracula, material-dark, atom-dark, etc.\nFull names: prism-gruvbox-dark, prism-one-dark, prism-nord, prism, prism-solarizedlight, etc.\nDefault: prism."
    )
    parser.add_argument(
        "--line-numbers",
        action="store_true",
        help="Enable line numbers in code blocks."
    )
    parser.add_argument(
        "--collapse",
        type=int,
        default=15,
        metavar="N",
        help="Auto-collapse code blocks longer than N lines into collapsible sections (default: 10). Use 0 to disable."
    )
    parser.add_argument(
        "--download-themes",
        action="store_true",
        help="Download and cache all Prism themes for offline use, then exit."
    )
    parser.add_argument(
        "--inline-lang",
        default="python",
        help="Language for highlighting inline code (default: python). Use 'none' to disable inline code highlighting."
    )
    parser.add_argument(
        "--fold-sections",
        nargs='*',
        default=None,  # Use None as default to distinguish from empty list
        help="Section titles to make foldable (default: ['Solution']). Use --fold-sections without arguments for default sections, or provide specific section names."
    )
    parser.add_argument(
        "--toc",
        action="store_true",
        help="Enable automatic table of contents generation from headings."
    )
    args = parser.parse_args()

    # Handle download themes command
    if args.download_themes:
        download_all_prism_themes()
        return

    # Ensure input file is provided for conversion
    if not args.input_file:
        parser.error("input_file is required unless using --download-themes")

    # Determine output filename
    if args.output_file:
        output_file = args.output_file
    else:
        from pathlib import Path
        input_path = Path(args.input_file)
        output_file = input_path.stem + '.html'

    # Perform conversion
    inline_lang = None if args.inline_lang.lower() == 'none' else args.inline_lang
    collapse_lines = None if args.collapse == 0 else args.collapse
    toc = args.toc if hasattr(args, 'toc') else False
    # Handle fold-sections argument properly
    if args.fold_sections == []:  # Empty list when --fold-sections used without args - use default
        foldable_sections = ["Solution"]  # Use the default value
    elif args.fold_sections is None:  # Not provided at all - use default sections
        foldable_sections = ["Problem", "Solution"]  # Enable by default
    else:  # Non-empty list - use as provided
        foldable_sections = args.fold_sections
    full_html = convert_md_to_html(args.input_file, args.css, args.theme,
                                   args.line_numbers, collapse_lines, inline_lang, foldable_sections, toc)

    # Write to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        print(
            f"✅ Successfully converted '{args.input_file}' to '{output_file}'")
    except IOError as e:
        print(f"Error: Could not write to output file '{output_file}'.\n{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
