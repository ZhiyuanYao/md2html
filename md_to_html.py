#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import markdown
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
        details_open = len(re.findall(r'<details[^>]*>', text_before, re.IGNORECASE))
        details_close = len(re.findall(r'</details>', text_before, re.IGNORECASE))
        
        # If we're inside an unclosed <details> tag, don't add additional collapse
        if details_open > details_close:
            return full_match
        
        # Also check for existing wrap-collabsible divs
        if '<div class="wrap-collabsible">' in text_before.split('</div>')[-1]:
            return full_match
            
        # Count lines in the code block
        # Look for the content between <code> and </code>
        code_content = re.search(r'<code[^>]*>(.*?)</code>', full_match, re.DOTALL)
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
        collapsible_html = f'''<div class="wrap-collabsible">
    <input id="{collapse_id}" class="toggle" type="checkbox">
    <label for="{collapse_id}" class="lbl-toggle">{language.upper()} ({lines} lines)</label>
    <div class="collapsible-content">
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
    <!-- Prism.js for Code Highlighting - 100% offline with embedded theme -->
    <style>
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
    
    print(f"Downloaded {downloaded} new themes. All themes are now cached locally!")
    print(f"Total available themes: {len(official_themes + prism_themes)}")
    print("Popular editor themes now available: one-dark, gruvbox-dark, gruvbox-light, material-dark, nord, night-owl, dracula")

def convert_md_to_html(md_file_path, css_file_path='style.css', prism_theme='prism', line_numbers=False, collapse_lines=10, inline_lang='python', enable_toc=True):
    """
    Converts a Markdown file to a full HTML document with styling.

    Args:
        md_file_path (str): Path to the input Markdown file.
        css_file_path (str, optional): Path to a custom CSS file. Defaults to 'style.css'.
        prism_theme (str, optional): Prism.js theme name. Defaults to 'prism'.
        line_numbers (bool, optional): Enable line numbers in code blocks. Defaults to False.
        collapse_lines (int, optional): Auto-collapse code blocks longer than this many lines. Defaults to 10.
        inline_lang (str, optional): Language for highlighting inline code. Defaults to 'python'.
        enable_toc (bool, optional): Enable table of contents generation. Defaults to True.

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
    
    # Determine if this is a dark theme for body class
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
        print(f"Warning: Custom CSS file not found at '{css_file_path}'. Proceeding without it.")
    
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
        print(f"Warning: Theme '{prism_theme}' not found in cache. Run 'python converter.py --download-themes' first.")
        prism_theme_css = ""


    # --- 2. Configure Markdown extensions ---
    # 'fenced_code': For GitHub-style code blocks (```)
    # 'tables': For Markdown tables
    # 'extra': Includes tables, fenced_code, and more
    # 'toc': Table of contents generation from headings (optional)
    extensions = ['extra']
    extension_configs = {}
    
    if enable_toc:
        extensions.append('toc')
        extension_configs['toc'] = {
            'permalink': False  # Don't add permalink anchors to headings
        }
    
    # Configure line numbers and theme classes based on parameters
    classes = []
    if line_numbers:
        line_numbers_css = '<link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.css" rel="stylesheet" />'
        line_numbers_js = '<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/line-numbers/prism-line-numbers.min.js"></script>'
        classes.append("line-numbers")
    else:
        line_numbers_css = ''
        line_numbers_js = ''
    
    if is_dark_theme:
        classes.append("dark-theme")
    else:
        classes.append("light-theme")
    
    body_class = f' class="{" ".join(classes)}"' if classes else ''

    # --- 3. Convert Markdown to an HTML fragment with proper math handling ---
    # Temporarily replace math expressions with placeholders (like md_to_html.py does)
    import re
    math_expressions = []
    def replace_math(match):
        math_expressions.append(match.group(0))
        return f"MATHPLACEHOLDER{len(math_expressions)-1}MATHPLACEHOLDER"
    
    # Replace display math first ($$...$$ - can span lines), then inline math ($...$)
    temp_md_text = re.sub(r'\$\$([^$]+?)\$\$', replace_math, md_text, flags=re.DOTALL)
    temp_md_text = re.sub(r'\$([^$\n]+?)\$', replace_math, temp_md_text)
    
    # Convert markdown to HTML
    md_converter = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)
    html_body = md_converter.convert(temp_md_text)
    
    # Restore math expressions as proper MathJax script tags
    def restore_math(match):
        index = int(match.group(1))
        original_math = math_expressions[index]
        if original_math.startswith('$$'):
            # Display math
            content = original_math[2:-2]
            return f'<script type="math/tex; mode=display">{content}</script>'
        else:
            # Inline math
            content = original_math[1:-1]
            return f'<script type="math/tex">{content}</script>'
    
    html_body = re.sub(r'MATHPLACEHOLDER(\d+)MATHPLACEHOLDER', restore_math, html_body)
    
    # --- 4. Auto-collapse long code blocks if specified ---
    if collapse_lines:
        html_body = wrap_long_code_blocks(html_body, collapse_lines)
    
    # --- 4.4. Convert JSON code blocks to use JavaScript highlighting ---
    # Replace language-json with language-javascript for Prism compatibility
    html_body = html_body.replace('class="language-json"', 'class="language-javascript"')
    
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
        html_body = re.sub(r'(?<!<pre>)<code>([^<]+)</code>', add_inline_lang, html_body)
    
    # --- 4.5. Prism.js will automatically add toolbar to code blocks ---
    # No manual wrapping needed

    # --- 5. Prism.js handles code highlighting via CDN ---
    # No need to generate CSS for code highlighting
    
    # Extract title from the first H1 tag, or use filename
    title = md_file_path.split('/')[-1].split('.')[0].replace('_', ' ').title()
    if '<h1>' in html_body:
        title = html_body.split('<h1>')[1].split('</h1>')[0]


    # --- 6. Assemble the final HTML document ---
    final_html = HTML_TEMPLATE.format(
        title=title,
        custom_css=custom_css,
        html_body=html_body,
        prism_theme=prism_theme,
        prism_theme_css=prism_theme_css,
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
    parser.add_argument("input_file", nargs='?', help="Path to the input Markdown file (.md).")
    parser.add_argument("output_file", nargs='?', help="Path for the output HTML file (.html). If not provided, uses input filename with .html extension.")
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
        default=10,
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
        "--no-toc",
        action="store_true",
        help="Disable automatic table of contents generation from headings."
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
    enable_toc = not args.no_toc
    full_html = convert_md_to_html(args.input_file, args.css, args.theme, args.line_numbers, collapse_lines, inline_lang, enable_toc)

    # Write to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        print(f"✅ Successfully converted '{args.input_file}' to '{output_file}'")
    except IOError as e:
        print(f"Error: Could not write to output file '{output_file}'.\n{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

