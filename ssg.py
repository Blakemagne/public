import os
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    """
    Extract the first h1 header from markdown content.
    
    Args:
        markdown (str): The markdown content
        
    Returns:
        str: The title (without the # and whitespace)
        
    Raises:
        ValueError: If no h1 header is found
    """
    lines = markdown.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith('#') and len(line) > 1 and line[1].isspace():
            return line[1:].strip()
    raise ValueError("No h1 header found in the markdown")


def generate_page(from_path, template_path, dest_path):
    """
    Generate an HTML page from a markdown file using a template.
    
    Args:
        from_path (str): Path to the markdown file
        template_path (str): Path to the template file
        dest_path (str): Path where the generated HTML will be written
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown file
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    # Read the template file
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Extract the title
    title = extract_title(markdown_content)
    
    # Replace placeholders in the template
    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    # Create directories if they don't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the full HTML to the destination file
    with open(dest_path, 'w') as f:
        f.write(full_html)