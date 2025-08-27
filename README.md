# Advanced Markdown to HTML Converter

A sophisticated Python-based markdown to HTML conversion system with advanced styling, theme support, and intelligent table formatting.

## Features

### Core Functionality
- **Markdown to HTML Conversion**: Convert markdown files to beautiful, styled HTML documents
- **Syntax Highlighting**: Powered by Prism.js with support for multiple programming languages
- **Math Rendering**: Full LaTeX math support with MathJax integration
- **Table of Contents**: Automatic TOC generation with `[TOC]` placeholder
- **Collapsible Sections**: Interactive section folding with customizable defaults

### Advanced Table Features
- **Natural Width Tables**: Tables size to their content instead of forced 100% width
- **Responsive Padding**: JavaScript-based intelligent padding adjustment
  - Tables exceeding 70% of content width (490px) get reduced padding (12px)
  - Smaller tables maintain full padding (24px)
- **Modern Styling**: Rounded corners, hover effects, and gradient backgrounds
- **Light Green Hover**: Beautiful light green row highlighting on hover

### Theme Support
- **Light Theme**: Clean, professional appearance with optimal readability
- **Dark Theme**: Applied selectively to code blocks only, preserving document readability
- **Inline Code**: Always uses light theme for consistency

### Code Block Features
- **Line Numbers**: Optional line numbering for code blocks
- **Language Detection**: Automatic syntax highlighting based on language tags
- **Collapsible Code**: Long code blocks can be made collapsible
- **Horizontal Scrolling**: Automatic scrollbars for wide code content

## Installation

### Prerequisites
```bash
pip install markdown pygments
```

### Setup
1. Clone or download the converter files
2. Ensure the `.prism/` directory contains:
   - `style.css` (main stylesheet)
   - `prism.js` (syntax highlighting library)

## Usage

### Basic Conversion
```bash
python md2html.py input.md output.html
```

### Advanced Options
```bash
# With custom CSS
python md2html.py input.md output.html --css custom.css

# Dark theme for code blocks
python md2html.py input.md output.html --theme dark

# Line numbers in code blocks
python md2html.py input.md output.html --line-numbers

# Collapsible sections (fold sections containing specific keywords)
python md2html.py input.md output.html --fold-sections "solution" "answer"

# Collapsible long code blocks (>N lines)
python md2html.py input.md output.html --collapse 50

# Disable table of contents
python md2html.py input.md output.html --no-toc
```

### Full Command Reference
```bash
python md2html.py [-h] [--css CSS] [--theme THEME] [--line-numbers]
                  [--collapse N] [--download-themes]
                  [--inline-lang INLINE_LANG]
                  [--fold-sections [FOLD_SECTIONS ...]] [--no-toc]
                  [input_file] [output_file]
```

## File Structure

```
render/
├── md2html.py              # Main conversion script
├── sample.md               # Example markdown file
├── .prism/
│   ├── style.css          # Main stylesheet with advanced table features
│   └── prism.js           # Syntax highlighting library
├── test_*.html            # Generated test files
└── README.md              # This documentation
```

## Key Technical Features

### Critical Fix: Browser Window Width vs Content Width Detection

**The Problem We Solved:**
The most challenging aspect was implementing responsive table padding that triggers based on **table width relative to content width**, NOT browser window width.

#### Initial Approach (WRONG ❌)
```css
/* This was the wrong approach - compares browser window width */
@media (max-width: 800px) {
    .markdown-body table th {
        padding: 12px 8px;
    }
}
```

**Why This Failed:**
- `@media (max-width: 800px)` detects when the **browser window** is narrow
- But we needed to detect when a **specific table** exceeds 70% of the **content area** (700px)
- A wide 6-column physics table should get reduced padding even on a large monitor
- A narrow 2-column table should keep full padding even on a small screen

#### The Breakthrough Solution (CORRECT ✅)
**JavaScript-based Real Table Width Detection:**

```javascript
// Get the actual content width (markdown-body is 700px)
const contentWidth = 700;
const threshold = contentWidth * 0.7; // 70% = 490px

const tables = document.querySelectorAll('.markdown-body table');
tables.forEach(function(table) {
    // Force natural width calculation
    table.style.width = 'auto';
    
    // Get ACTUAL rendered table width
    const tableWidth = table.getBoundingClientRect().width;
    
    if (tableWidth > threshold) {
        // THIS specific table is too wide - reduce its padding
        const ths = table.querySelectorAll('th');
        const tds = table.querySelectorAll('td');
        
        ths.forEach(function(th) {
            th.style.padding = '12px 12px'; // Reduced from 24px
        });
        
        tds.forEach(function(td) {
            td.style.padding = '11px 12px'; // Reduced from 24px
        });
    }
});
```

**Key Insight:**
- `getBoundingClientRect().width` gives us the **actual rendered width** of each individual table
- We compare each table's width against the **content container width** (700px)
- Only tables that actually exceed 70% of content width get reduced padding
- This works regardless of browser window size

#### Failed Approaches We Tried

**1. CSS Container Queries (Limited Browser Support)**
```css
@container (min-width: 490px) {
    .markdown-body table th {
        padding: 12px 8px;
    }
}
```
*Problem: Container queries have limited browser support and didn't work reliably*

**2. Column Counting with nth-child (Too Rigid)**
```css
.markdown-body table th:nth-child(5) ~ th {
    padding: 12px 8px;
}
```
*Problem: This targets columns, not actual table width. A table with 3 wide columns might need reduced padding, while a table with 6 narrow columns might not*

**3. Viewport-based Media Queries (Wrong Measurement)**
```css
@media (max-width: 750px) {
    .markdown-body table th {
        padding: 12px 8px;
    }
}
```
*Problem: This measures browser window width, not table content width*

#### The Debugging Process

**Step 1: Extreme Debug Values**
We used extreme padding (0px, 50px) and bright colors (red, yellow backgrounds) with `!important` flags to verify if CSS changes were being applied at all.

**Step 2: Testing Media Query Activation**
We tested whether `@media` queries were triggering by resizing browser windows and checking for visual changes.

**Step 3: CSS Specificity Investigation**
We discovered that media queries needed to be placed at the end of the CSS file and use `!important` to override existing table styles.

**Step 4: The JavaScript Revelation**
Finally realized that CSS cannot detect "table width vs content width" - only JavaScript can measure actual rendered dimensions using `getBoundingClientRect()`.

#### Practical Example from sample.md

**Small Table (2 columns):**
```markdown
| A | B |
|---|---|
| C | D |
```
- Actual rendered width: ~100px
- 100px < 490px threshold → **Keep full 24px padding**

**Large Physics Table (6 columns):**
```markdown
| Particle | Representation | g | B | L | Y |
|:---------|:---------------|:-:|:-:|:-:|:-:|
| Left-handed quarks | (3, 2)₁/₆ | 6 | 1/3 | 0 | 1/6 |
```
- Actual rendered width: ~580px  
- 580px > 490px threshold → **Reduce to 12px padding**

**The Beauty of This Solution:**
- The 2-column table stays spacious and readable
- The 6-column physics table becomes compact to fit properly
- No manual CSS classes or complex selectors needed
- Works automatically for any markdown table

### Intelligent Table Sizing
The system uses this JavaScript solution to measure actual table width vs content width:
- **Content Width**: 700px (markdown-body container)
- **Threshold**: 70% = 490px
- **Logic**: `if (actualTableWidth > 490px)` → reduce padding to 12px
- **Benefit**: Wide tables (like 6-column physics tables) get compact spacing while narrow tables keep full spacing

### CSS Architecture Deep Dive

#### Core Table Structure (.prism/style.css)

**1. Container Setup**
```css
.markdown-body {
    color: #24292e;
    font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif;
    font-size: 13px;
    line-height: 1.5;
    width: 700px;  /* ← Critical: This is our content width reference */
    text-align: left;
    padding: 1em 2em 2em 2em;
    margin: auto;
    background-color: white;
}
```
*The 700px width is the foundation for our 70% table width calculations*

**2. Natural Table Sizing**
```css
.markdown-body table {
    display: table;
    border-collapse: separate;  /* ← Enables rounded corners */
    border-spacing: 0;
    margin: 24px auto;
    border-radius: 8px;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    width: auto;  /* ← Key: Natural width, not forced 100% */
    overflow: hidden;  /* ← Clips content to rounded borders */
}
```

**3. Header Styling with Gradients**
```css
.markdown-body table thead {
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    border-bottom: 1px solid #d1d5db;
}

.markdown-body table th {
    padding: 12px 24px;  /* ← Default padding (reduced by JavaScript) */
    text-align: left;
    font-weight: 600;
    color: #374151;
    font-size: 0.95em;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    border: none;
}
```

**4. Cell Styling**
```css
.markdown-body table td {
    padding: 11px 24px;  /* ← Default padding (reduced by JavaScript) */
    border-bottom: 1px solid #f3f4f6;
    color: #4b5563;
    background: #ffffff;
    border-left: none;
    border-right: none;
}
```

**5. Interactive Hover Effects**
```css
.markdown-body table tbody tr:hover {
    background: #f0fdf4;  /* Light green background */
    color: #166534;
    transform: translateY(-1px);
    transition: all 0.2s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.markdown-body table tbody tr:hover td {
    border-left: 3px solid #22c55e;  /* Green left border accent */
    background: inherit;
}
```

**6. Rounded Corner Implementation**
```css
.markdown-body table tr:last-child td {
    border-bottom: none;  /* Remove border from last row */
}
```
*Critical: `border-collapse: separate` + `border-spacing: 0` + `overflow: hidden` creates perfect rounded corners*

#### Theme System

**Light Theme (Default)**
- Headers: Gradient from `#f8fafc` to `#f1f5f9`
- Cells: White background `#ffffff`
- Hover: Light green `#f0fdf4` with green accent `#22c55e`

**Dark Theme (Code Blocks Only)**
```css
pre.dark-theme {
    background-color: #1e1e1e !important;
    color: #d4d4d4 !important;
}
```
*Applied via JavaScript only to `pre` elements, not entire document*

**Inline Code (Always Light)**
```css
.markdown-body code:not(pre code),
code:not(pre code) {
    background-color: rgba(27, 31, 35, .05) !important;
    color: #333 !important;
    border-radius: 3px !important;
    font-size: 90% !important;
    padding: 1px 3px !important;
}
```
*Uses `!important` to override any dark theme inheritance*

#### Selection Colors
```css
*::selection {
    background-color: #C0D4F3 !important;
    color: inherit !important;
}
```
*Consistent blue selection across all content*

### Python Script Architecture (md2html.py)

#### Core Structure and Flow

**1. Import and Setup**
```python
import markdown
import sys
import argparse
from pathlib import Path
import re
import os
import pygments
```

**2. Command Line Argument Parsing**
```python
def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to styled HTML')
    parser.add_argument('input_file', nargs='?', help='Input Markdown file')
    parser.add_argument('output_file', nargs='?', help='Output HTML file')
    parser.add_argument('--css', help='Custom CSS file path')
    parser.add_argument('--theme', choices=['light', 'dark'], default='light')
    parser.add_argument('--line-numbers', action='store_true')
    parser.add_argument('--collapse', type=int, metavar='N', 
                       help='Make code blocks with more than N lines collapsible')
    parser.add_argument('--fold-sections', nargs='*', 
                       help='Keywords for sections to fold by default')
    parser.add_argument('--no-toc', action='store_true', 
                       help='Disable table of contents generation')
```

#### Key Functions Breakdown

**1. Table Detection and Formatting**
```python
def fix_table_formatting(md_text):
    """
    Ensures tables are properly formatted by adding blank lines before/after
    Critical for markdown parser to recognize tables correctly
    """
    lines = md_text.split('\n')
    result = []
    in_table = False
    
    for i, line in enumerate(lines):
        is_table_line = '|' in line and line.strip()
        
        if is_table_line and not in_table:
            # Starting a table - ensure blank line before
            if i > 0 and result and result[-1].strip():
                result.append('')
            in_table = True
        elif not is_table_line and in_table:
            # Ending a table - ensure blank line after
            result.append(line)
            if i < len(lines) - 1 and lines[i + 1].strip():
                result.append('')
            in_table = False
            continue
            
        result.append(line)
    
    return '\n'.join(result)
```

**2. Code Block Processing**
```python
def process_code_blocks(html_content, collapse_threshold=None, 
                       add_line_numbers=False, theme='light'):
    """
    Enhanced code block processing with:
    - Language detection and syntax highlighting
    - Optional line numbers
    - Collapsible long code blocks
    - Theme-aware styling
    """
    # Pattern to match code blocks with language specification
    code_block_pattern = r'<pre><code class="language-(\w+)">(.*?)</code></pre>'
    
    def replace_code_block(match):
        language = match.group(1)
        code = match.group(2)
        
        # Handle special language cases
        if language == "javascript" and is_json_like(code):
            language = "json"
        
        # Count lines for collapse decision
        lines = code.split('\n')
        line_count = len(lines)
        
        # Build CSS classes
        classes = [f"language-{language}"]
        if theme == 'dark':
            classes.append('dark-theme')
        
        # Create collapsible wrapper if needed
        if collapse_threshold and line_count > collapse_threshold:
            return create_collapsible_code_block(code, language, line_count, classes)
        else:
            return create_standard_code_block(code, language, classes, add_line_numbers)
```

**3. JavaScript Integration for Table Width Detection**
```python
# Embedded JavaScript (lines 260-300 in md2html.py)
javascript_code = f"""
document.addEventListener('DOMContentLoaded', function() {{
    const isDarkTheme = {str(is_dark_theme).lower()};
    
    // Dark theme application (only to pre elements)
    if (isDarkTheme) {{
        const codeBlocks = document.querySelectorAll('pre');
        codeBlocks.forEach(function(pre) {{
            pre.classList.add('dark-theme');
        }});
    }}
    
    // ★ CRITICAL TABLE WIDTH DETECTION ★
    const contentWidth = 700; // markdown-body width
    const threshold = contentWidth * 0.7; // 70% = 490px
    
    const tables = document.querySelectorAll('.markdown-body table');
    tables.forEach(function(table) {{
        table.style.width = 'auto'; // Force natural width
        
        // Get actual rendered table width
        const tableWidth = table.getBoundingClientRect().width;
        
        if (tableWidth > threshold) {{
            // Reduce padding for wide tables
            const ths = table.querySelectorAll('th');
            const tds = table.querySelectorAll('td');
            
            ths.forEach(function(th) {{
                th.style.padding = '12px 12px'; // Reduced from 24px
            }});
            
            tds.forEach(function(td) {{
                td.style.padding = '11px 12px'; // Reduced from 24px
            }});
        }}
    }});
}});
"""
```

**4. Section Collapsing System**
```python
def create_collapsible_sections(headers, collapsed_sections):
    """
    Creates interactive collapsible sections based on header keywords
    """
    for header in headers:
        text = header.textContent
        section_id = f'section-{index}'
        
        # Check if section should be collapsed by default
        is_collapsed = any(keyword.lower() in text.lower() 
                          for keyword in collapsed_sections)
        
        # Create header wrapper with click handler
        header_div = create_header_wrapper(is_collapsed, section_id)
        
        # Wrap content in collapsible container
        content_wrapper = create_content_wrapper(is_collapsed, section_id)
```

**5. HTML Template Generation**
```python
def generate_html_template(title, custom_css, javascript_code, prism_js_content):
    """
    Generates complete HTML document with:
    - MathJax integration for math rendering
    - Prism.js for syntax highlighting  
    - Custom CSS and JavaScript injection
    - Responsive meta tags
    """
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        
        <!-- MathJax for LaTeX math rendering -->
        <script type="text/javascript" async
            src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.0/es5/tex-mml-chtml.js">
        </script>
        
        <!-- Custom CSS with table intelligence -->
        <style>{custom_css}</style>
    </head>
    <body>
        <div class="markdown-body">
            {{content}}
        </div>
        
        <!-- Prism.js for syntax highlighting -->
        <script>{prism_js_content}</script>
        
        <!-- Table width detection and section collapsing -->
        <script>{javascript_code}</script>
    </body>
    </html>
    """
```

#### Processing Pipeline

**Step 1: Input Processing**
1. Read markdown file
2. Apply table formatting fixes
3. Parse command line arguments

**Step 2: Markdown Conversion** 
1. Initialize markdown processor with extensions
2. Convert markdown to HTML
3. Process code blocks for syntax highlighting

**Step 3: Enhancement Layer**
1. Add table of contents if requested
2. Create collapsible sections
3. Apply theme-specific modifications

**Step 4: JavaScript Integration**
1. Embed table width detection logic
2. Add section collapsing functionality  
3. Apply dark theme to code blocks only

**Step 5: Output Generation**
1. Load custom CSS (.prism/style.css)
2. Load Prism.js for highlighting
3. Generate final HTML with all components
4. Write to output file

#### Error Handling and Robustness

```python
try:
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
except FileNotFoundError:
    print(f"Error: Input Markdown file not found at '{md_file_path}'")
    sys.exit(1)

try:
    with open(css_file_path, 'r', encoding='utf-8') as f:
        custom_css = f.read()
except FileNotFoundError:
    print(f"Warning: Custom CSS file not found. Proceeding without it.")
```

This architecture creates a robust, extensible system that handles the complex interaction between markdown parsing, CSS styling, and JavaScript enhancement to create intelligent, responsive table formatting.

## Code Highlighting Challenges We Solved

### Background Color Theme Issues

**The Problem:**
We spent significant time debugging why code block backgrounds weren't applying correctly in dark theme mode, and why inline code was inheriting dark theme styles when it shouldn't.

#### Initial Issue: Whole Document Dark Theme (WRONG ❌)
```javascript
// This was applying dark theme to EVERYTHING
if (isDarkTheme) {
    document.body.classList.add('dark-theme');
}
```
**Problems this caused:**
- Tables became dark themed
- Inline code became unreadable  
- Entire document appearance changed
- Lost the clean document aesthetic

#### The Correct Solution: Selective Dark Theme (CORRECT ✅)
```javascript
// Apply dark theme ONLY to pre code blocks
if (isDarkTheme) {
    const codeBlocks = document.querySelectorAll('pre');
    codeBlocks.forEach(function(pre) {
        pre.classList.add('dark-theme');
    });
}
```

**CSS Implementation:**
```css
/* Dark theme styles - ONLY for pre elements */
pre.dark-theme {
    background-color: #1e1e1e !important;
    color: #d4d4d4 !important;
}

/* Force inline code to ALWAYS use light theme */
.markdown-body code:not(pre code),
code:not(pre code) {
    background-color: rgba(27, 31, 35, .05) !important;
    color: #333 !important;
    border-radius: 3px !important;
    font-size: 90% !important;
    margin: 0 !important;
    padding: 1px 3px !important;
    text-shadow: none !important; /* Override any dark theme text shadow */
    border: none !important; /* Override any dark theme borders */
}
```

### Scrollbar Issues in Collapsible Content

**The Problem:**
Horizontal scrollbars were missing in collapsible content areas, making wide code blocks unreadable.

#### What We Discovered:
Initially thought this was a bug, but after debugging realized it was correct behavior:
- **Short code blocks**: No horizontal scroll needed → No scrollbar (correct)
- **Long code blocks**: Content overflows → Scrollbar appears (correct)

#### The Investigation Process:

**Step 1: CSS Debugging**
```css
/* Tried forcing scrollbars everywhere */
.content-collapsible {
    overflow-x: auto !important; /* This was unnecessary */
}

.content-collapsible pre {
    overflow-x: scroll !important; /* This was wrong - should be 'auto' */
}
```

**Step 2: HTML Structure Analysis**
We checked multiple code blocks:
- PYTHON (159 lines): Has scrollbar when needed ✅
- PYTHON (118 lines): No scrollbar because content fits ✅
- Short code snippets: No scrollbar because not needed ✅

**Step 3: The Realization**
The user feedback: *"my bad, no issue actually. some pre code contains short code lines that do not need h scroll bar. The behavior is actually correct."*

#### Final CSS for Proper Scrollbar Behavior:
```css
.content-collapsible {
    max-height: 400px;
    overflow-y: auto;
    padding: 0; /* Critical: No padding to avoid spacing issues */
    margin: 0;  /* Critical: No margin for seamless borders */
}

.content-collapsible pre {
    overflow-x: auto; /* Only show scrollbar when needed */
    margin: 0 !important; /* Remove default pre margins */
    border-radius: 0; /* Square corners inside collapsible */
}
```

### Zero Margin Between Code and Collapsible Border

**The Problem:**
There was unwanted spacing between code snippets and the collapsible container border, creating visual gaps.

#### CSS Issues We Fixed:

**1. Pre Element Default Margins**
```css
/* Problem: Browser default margins on pre elements */
pre {
    margin: 1em 0; /* Browser default - caused gaps */
}

/* Solution: Force zero margins in collapsible context */
.content-collapsible pre {
    margin: 0 !important;
    border-radius: 0; /* Remove rounded corners for seamless fit */
}
```

**2. Container Padding Issues**
```css
/* Problem: Padding on collapsible container */
.content-collapsible {
    padding: 10px; /* This created unwanted spacing */
}

/* Solution: Zero padding for seamless borders */
.content-collapsible {
    padding: 0; /* Seamless edge-to-edge fit */
    margin: 0;  /* No external spacing */
    border: 1px solid #e1e5e9;
    border-top: none; /* Seamless connection to header */
}
```

**3. Border Radius Conflicts**
```css
/* Problem: Rounded corners on code blocks created gaps */
.content-collapsible pre code {
    border-radius: 6px; /* This left gaps at corners */
}

/* Solution: Square corners for seamless fit */
.content-collapsible pre {
    border-radius: 0 !important;
}
.content-collapsible pre code {
    border-radius: 0 !important;
}
```

#### Complete Collapsible Code Block CSS Solution:
```css
/* Collapsible container - seamless borders */
.content-collapsible {
    max-height: 400px;
    overflow-y: auto;
    overflow-x: hidden;
    padding: 0; /* Zero padding for seamless fit */
    margin: 0;  /* Zero margin for seamless fit */
    border: 1px solid #e1e5e9;
    border-top: none;
    border-radius: 0 0 8px 8px;
    background: white;
}

/* Code blocks inside collapsible - no gaps */
.content-collapsible pre {
    margin: 0 !important; /* Remove all margins */
    border-radius: 0 !important; /* Square corners */
    border: none !important; /* No double borders */
    overflow-x: auto; /* Horizontal scroll when needed */
}

/* Header styling for seamless connection */
.section-collapsible-header {
    padding: 8px 16px;
    background: linear-gradient(135deg, #f8fafc, #f1f5f9);
    border: 1px solid #e1e5e9;
    border-radius: 8px 8px 0 0; /* Rounded top, square bottom */
    cursor: pointer;
}

/* Collapsed state - full rounding */
.section-collapsible-header.collapsed {
    border-radius: 8px; /* Full rounding when collapsed */
    border-bottom: 1px solid #e1e5e9;
}
```

### The Debugging Timeline

1. **Initial Problem**: Dark theme applied to entire document
   - **Fix**: JavaScript selector targeting only `pre` elements

2. **Inline Code Issue**: Inheriting dark theme styles  
   - **Fix**: CSS `!important` overrides for inline code

3. **Missing Scrollbars**: Thought horizontal scrollbars were broken
   - **Discovery**: Actually correct behavior - scrollbars only when needed

4. **Margin Gaps**: Unwanted spacing between code and borders
   - **Fix**: Zero margins and padding with seamless border system

5. **Border Radius Conflicts**: Rounded corners creating visual gaps
   - **Fix**: Square corners inside collapsible, rounded on container

### Key Insights Learned

1. **Theme Inheritance**: CSS cascade can cause unintended theme application
2. **Default Browser Styles**: `pre` elements have default margins that must be overridden  
3. **Scrollbar Behavior**: `overflow: auto` is better than `overflow: scroll` for conditional scrollbars
4. **Seamless Borders**: Zero padding/margin + careful border-radius creates professional appearance
5. **Visual Debugging**: Colored backgrounds and extreme values help identify CSS application issues

These fixes ensure that code blocks have proper theming, appropriate scrollbars, and seamless integration with collapsible containers.

### Section Collapsing
- **Auto-detection**: Sections with keywords like "solution", "answer" can auto-collapse
- **Interactive**: Click headers to expand/collapse sections
- **Smooth Animation**: CSS transitions for professional feel

## Markdown Extensions

### Table of Contents
```markdown
# My Document

## Table of Contents
[TOC]

## Section 1
Content here...
```

### Math Support
```markdown
Inline math: $E = mc^2$

Display math:
$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$
```

### Code Blocks with Languages
```markdown
​```python
def hello_world():
    print("Hello, World!")
​```

​```json
{
    "name": "example",
    "version": "1.0.0"
}
​```
```

### Tables
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Row 2    | Row 2    | Row 3    |
```

## Styling Customization

### Table Styling
Tables automatically adjust based on width:
- **Small tables**: Full 24px horizontal padding
- **Large tables**: Reduced 12px horizontal padding
- **All tables**: Light green hover effects, rounded corners, modern gradients

### Color Scheme
- **Headers**: Gradient background `linear-gradient(135deg, #f8fafc, #f1f5f9)`
- **Hover**: Light green `#f0fdf4` background with `#22c55e` left border
- **Borders**: Subtle `#e5e7eb` and `#f3f4f6` borders

### Responsive Design
The system adapts to different content types:
- Physics tables with many columns get compact spacing
- Simple 2-column tables retain spacious formatting
- Code blocks auto-scroll when content is wide

## Examples

### Input: sample.md
- Demonstrates table detection and formatting
- Shows math rendering capabilities  
- Includes complex multi-column tables
- Features collapsible code sections

### Output: Generated HTML
- Professional document appearance
- Interactive table hover effects
- Properly sized tables based on content
- Syntax-highlighted code blocks

## Browser Compatibility

- **Modern Browsers**: Full feature support (Chrome, Firefox, Safari, Edge)
- **JavaScript Required**: For table width detection and section collapsing
- **CSS Grid Support**: Enhanced layout capabilities
- **MathJax**: Requires internet connection for math rendering

## Development

### Key Files
- **`md2html.py`**: Main converter with table detection logic
- **`.prism/style.css`**: Advanced CSS with responsive table features
- **`.prism/prism.js`**: Syntax highlighting engine

### Recent Improvements
- JavaScript-based table width detection (vs CSS media queries)
- Intelligent padding adjustment based on actual table width
- Natural table sizing instead of forced 100% width
- Light green hover theme with modern aesthetics

## Troubleshooting

### Tables Not Formatting Correctly
- Ensure JavaScript is enabled
- Check that table has proper markdown syntax
- Verify `.prism/style.css` is loaded correctly

### Math Not Rendering
- Check internet connection (MathJax CDN required)
- Verify math syntax follows LaTeX standards
- Ensure `$$` for display math, `$` for inline math

### Code Not Highlighting
- Check language identifier after opening ​```
- Ensure `.prism/prism.js` supports the language
- Verify Prism.js is loaded correctly

## License

## Major Issues We Solved Through Multiple Iterations

### 1. Section Collapse System: HTML String Parsing vs DOM Manipulation

**The Original Problem:**
The initial section folding system used complex HTML string manipulation that was breaking code blocks with HTML entities.

#### Failed Approach: Complex HTML String Parsing (❌)
```python
# This was breaking HTML entities like &quot; in code blocks
def create_section_boundaries(html_content):
    lines = html_content.split('\n')
    # Complex regex and string manipulation
    for line in lines:
        if '<h2>' in line or '<h3>' in line:
            # String manipulation that broke HTML entities
            modified_html = insert_collapsible_wrapper(line)
```

**Problems This Caused:**
- Code blocks containing `&quot;` were split incorrectly
- HTML entities were broken: `"Hello World"` became `"Hello World" + broken_fragment`
- Sibling sections were nested incorrectly inside each other
- Complex boundary detection logic was unreliable

#### The Breakthrough: DOM-Based JavaScript Manipulation (✅)
```javascript
// Process after HTML is fully rendered - no string parsing
document.addEventListener('DOMContentLoaded', function() {
    const headers = document.querySelectorAll('.markdown-body h2, .markdown-body h3, .markdown-body h4');
    
    headers.forEach(function(header) {
        // Create wrapper elements using DOM API
        const headerDiv = document.createElement('div');
        const contentDiv = document.createElement('div');
        
        // Move actual DOM nodes, preserving all HTML entities
        while (nextElement && !isNextHeader(nextElement)) {
            contentDiv.appendChild(nextElement);
            nextElement = headerDiv.nextElementSibling;
        }
    });
});
```

**Why This Fixed Everything:**
- HTML entities remain intact (browser has already parsed them)
- Proper DOM node relationships (no manual nesting logic needed)
- Boundary detection uses actual DOM traversal
- No risk of breaking existing HTML structure

### 2. Dark Theme Scope: Global vs Selective Application

**The Problem:**
Dark theme was initially applied to the entire document, making it unreadable and affecting tables, inline code, and main text.

#### Failed Approach: Body-Level Dark Theme (❌)
```javascript
// This made everything dark-themed
if (isDarkTheme) {
    document.body.classList.add('dark-theme');
}
```

**Problems:**
- Main document text became white on dark background (unreadable)
- Tables lost their professional light theme
- Inline code became invisible against dark backgrounds
- Headers and section text were affected

#### The Solution: Content-Collapsible Pre Code Only (✅)
```javascript
// Apply dark theme ONLY to pre code blocks in content-collapsible areas
if (isDarkTheme) {
    const codeBlocks = document.querySelectorAll('.content-collapsible pre');
    codeBlocks.forEach(function(pre) {
        pre.classList.add('dark-theme');
    });
}
```

**CSS Implementation:**
```css
/* Dark theme - ONLY for specific pre elements */
body.dark-theme .content-collapsible-content pre {
    background-color: #282C34 !important;
}

/* Force inline code to ALWAYS use light theme */
.markdown-body code:not(pre code) {
    background-color: rgba(27, 31, 35, .05) !important;
    color: #333 !important;
}
```

### 3. Background Color Coverage in Wide Code Blocks

**The Problem:**
Pre code background was limited to container width, showing white background when horizontally scrolling through wide code.

#### The Issue Visualization:
```
┌─ Container (700px) ─┐
│ [Code Block]       │ ← Background covers this
│ with very long lines that extend → │ ← White background here
└────────────────────┘
```

#### The Fix: Max-Content Width (✅)
```css
.content-collapsible-content pre {
    width: max-content !important;  /* Expand to fit content */
    min-width: 100% !important;     /* At least container width */
    background-color: #f0f2f5 !important;
}
```

**Result:**
```
┌─ Container (700px) ─┬─ Extended ─┐
│ [Code Block with very long lines] │ ← Background covers all
└────────────────────┴────────────┘
```

### 4. Horizontal Scrollbar Placement: Individual vs Window Level

**The Problem:**
Individual code blocks had their own scrollbars, making navigation difficult for long code.

#### User's Request:
*"Please add at the bottom of the content-collapsible window, instead of at the bottom of code in pre code. This is because I need to scroll left right even when the code not scroll down to the bottom"*

#### The Solution: Window-Level Scrolling (✅)
```css
/* Remove scrollbars from individual pre blocks */
.content-collapsible-content pre {
    overflow: visible !important;
}

/* Add scrollbar to the collapsible container */
.content-collapsible-content {
    overflow-x: auto !important;
    overflow-y: visible !important;
}

/* Style the container scrollbar */
.content-collapsible-content::-webkit-scrollbar {
    width: 8px !important;
    height: 7px !important;
}
```

### 5. Collapsible Class Naming Conflicts

**The Problem:**
Mixed class names between different collapsible systems caused conflicts.

#### The Cleanup:
- **Section collapse**: `.section-collapsible-header`, `.section-collapsible-content`
- **Content collapse**: `.wrap-content-collapsible`, `.content-collapsible-content`

### 6. CSS Padding Issues in Content Collapsible

**The Problem:**
Double background styling and conflicting padding rules.

#### The Fix:
```css
/* Single background on .content-inner only */
.content-collapsible-content .content-inner {
    background: rgba(106, 176, 222, .15);
    border-bottom: 2px solid rgba(106, 176, 222, .8);
    border-bottom-left-radius: 7px;
    border-bottom-right-radius: 7px;
    margin-top: -0.8rem;
    padding: 10px 0px 0px 0px;  /* Zero left/right padding */
}

/* No background on container */
.content-collapsible-content {
    max-height: 100vh !important;
    overflow-x: auto !important;
    overflow-y: visible !important;
}
```

### 7. List Detection Issues (Like Tables)

**The Problem Identified:**
Similar to tables, lists need blank lines before them to be detected by Markdown parser.

**Example Failing Case:**
```markdown
Knowledge Points Tested:
- Angular displacement ($\theta$), angular velocity ($\omega$)
- Relationship between linear distance (arc length)
```

**The Fix Needed:**
A `fix_list_formatting()` function similar to `fix_table_formatting()` that adds blank lines before lists.

### Timeline of Major Fixes

1. **Session 1-5**: Table responsive padding system development
2. **Session 6-8**: Section collapsible system from HTML parsing to DOM manipulation  
3. **Session 9-12**: Dark theme scope limitation and background coverage fixes
4. **Session 13-15**: Scrollbar placement and CSS class organization
5. **Session 16**: Content collapsible padding conflicts and final polish
6. **Current**: List detection issue identification (similar to table fix)

### Key Lessons Learned

1. **DOM Manipulation > String Parsing**: JavaScript DOM manipulation is safer than HTML string parsing
2. **Selective Theming**: Apply themes only where needed, not globally
3. **CSS Specificity**: Use `!important` strategically to override complex cascading
4. **User Testing**: Real-world usage reveals edge cases not caught in initial development
5. **Iterative Development**: Complex UI features require multiple refinement cycles

### Development Approach That Worked

1. **Start Simple**: Basic functionality first
2. **User Feedback**: Test with real content early and often
3. **Debug Visually**: Use colored backgrounds and extreme values to verify CSS application
4. **Incremental Fixes**: Address one issue at a time
5. **Comprehensive Testing**: Test edge cases like long code blocks, wide tables, nested structures

This project demonstrates the importance of iterative development and responsive problem-solving in creating robust document processing systems.

## License

This project is a custom markdown converter developed for advanced document generation with emphasis on beautiful table formatting and modern web standards.