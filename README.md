## Overview
This project is a custom-built static site generator that converts Markdown content into HTML pages. It's perfect for creating simple blogs or documentation sites with minimal setup.

### Features:
- Converts Markdown files to HTML
- Supports common Markdown elements (headings, paragraphs, lists, code blocks, etc.)
- Handles inline formatting (bold, italic, code, links, images)
- Applies a consistent HTML template to all pages
- Preserves directory structure from content to output

## Project Structure
```
├── build.sh              # Build script with custom output path
├── content/              # Markdown content files
│   ├── blog/             # Blog posts in Markdown
│   ├── index.md          # Home page content
│   └── ...               # Other content pages
├── docs/                 # Generated HTML output
├── main.sh               # Run the generator and start local server
├── src/                  # Source code
│   ├── copystatic.py     # Utility to copy static files
│   ├── gencontent.py     # Main content generation logic
│   ├── htmlnode.py       # HTML node classes
│   ├── inline_markdown.py # Inline markdown processing
│   ├── main.py           # Main entry point
│   ├── markdown_blocks.py # Block-level markdown processing
│   └── textnode.py       # Text node classes
├── static/               # Static assets (CSS, images, etc.)
├── template.html         # HTML template for all pages
└── test.sh               # Run tests
```

## How It Works
### Data Flow
The generator processes data through several steps:
1. Markdown files in the `content` directory are parsed into blocks.
2. Each block is converted to HTML nodes based on its type (heading, paragraph, list, etc.).
3. Inline Markdown elements within blocks are processed (bold, italic, links, etc.).
4. The HTML nodes are rendered to HTML strings.
5. The template from `template.html` is applied to each page.
6. The resulting HTML files are written to the `docs` directory.
7. Static assets are copied from `static` to `docs`.

## Customizing for Your Content
### Content Structure
Place your Markdown files in the `content` directory:
```
content/index.md → docs/index.html
content/about.md → docs/about.html
content/blog/post1.md → docs/blog/post1.html
```

### Markdown Format
The generator supports standard Markdown syntax:
```md
# Heading 1
## Heading 2

This is a paragraph with **bold** and _italic_ text.

- List item 1
- List item 2

1. Ordered item 1
2. Ordered item 2

> This is a blockquote

![Image alt text](/images/image.png)

[Link text](https://example.com)
```

### HTML Template
Edit `template.html` to customize the page structure:
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ Title }}</title>
    <link href="/index.css" rel="stylesheet">
</head>
<body>
    <header>
        <h1>My Website</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/blog">Blog</a>
        </nav>
    </header>
    <main>
        {{ Content }}
    </main>
    <footer>
        &copy; 2023 My Website
    </footer>
</body>
</html>
```

### Static Assets
Place your CSS, images, and other static files in the `static` directory:
```
static/index.css → docs/index.css
static/images/logo.png → docs/images/logo.png
```

To reference images in your Markdown:
```md
![Alt text](/images/image.png)
```
For CSS, link to it in the template:
```html
<link href="/index.css" rel="stylesheet">
```

## Building Your Site
Run the generator:
```sh
./main.sh
```
This will:
- Generate your site in the `docs` directory.
- Start a local web server at [http://localhost:8888](http://localhost:8888).

For custom output paths:
```sh
./build.sh "my-website"
```

## Common Modifications
### Changing the Page Title Format
To modify how page titles are extracted, edit `extract_title` in `gencontent.py`:
```python
def extract_title(md):
    # Extract title from metadata block instead of h1
    if md.startswith("---"):
        end = md.find("---", 3)
        if end != -1:
            metadata = md[3:end]
            for line in metadata.split("\n"):
                if line.startswith("title:"):
                    return line[6:].strip()
    
    # Fallback to h1
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    
    raise ValueError("no title found")
```

### Adding Navigation Links
To add navigation based on the content structure, modify `generate_page` in `gencontent.py`:
```python
def generate_page(from_path, template_path, dest_path):
    # Existing code...
    
    # Generate navigation links
    nav_links = ""
    for page in ["Home", "About", "Blog"]:
        url = page.lower()
        if url == "home":
            url = ""
        nav_links += f'<a href="/{url}">{page}</a> '
    
    template = template.replace("{{ Navigation }}", nav_links)
    
    # Continue with existing code...
```
Then add `{{ Navigation }}` to your template:
```html
<nav>
    {{ Navigation }}
</nav>
```

### Adding Custom CSS
To modify the styling, edit `static/index.css`:
```css
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    max-width: 800px;
    margin: 0 auto;
    padding: 1rem;
}

h1, h2, h3 {
    color: #333;
}

a {
    color: #0066cc;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
```

## Testing
Run the tests to ensure everything works correctly:
```sh
./test.sh
```

## Troubleshooting
### Images Not Showing Up
- Make sure images are in the `static/images` directory.
- Verify image paths in Markdown (`/images/filename.png`).
- Check that static files are being copied correctly.

### Links Not Working
- Ensure links use the correct paths (relative to the site root).
- For internal links, use paths like `/about` or `/blog/post1`.

### Template Issues
- Check that your template has the `{{ Title }}` and `{{ Content }}` placeholders.
- Verify that CSS paths in the template are correct.

### Python Errors
- Run the tests to identify issues.
- Check that you have Python 3 installed.
- Verify that all required modules are imported.

This static site generator is intentionally simple but can be extended to support more features as your needs grow.

