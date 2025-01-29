from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    # Create a TextNode object
    node = TextNode("This is text", TextType.BOLD, "https://www.boot.dev")
    
    # Create a PROPER HTMLNode with all required parameters
    test_html = HTMLNode(
        tag="div",
        value="Hello World",
        props={"class": "container"}
    )
    
    # Create a LeafNode object
    test_leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    
    # Print PROPERLY using .to_html() and .__repr__()
    print("TextNode:", node)
    print("HTMLNode props:", test_html.props_to_html())
    print("LeafNode HTML:", test_leaf.to_html())
if __name__ == "__main__":
    main()
