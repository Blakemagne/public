from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    # Test TextNode
    text_node = TextNode("This is text", TextType.BOLD, "https://www.boot.dev")
    
    # Test HTMLNode props
    html_node = HTMLNode(
        tag="div",
        value="Hello World",
        props={"class": "container"}
    )
    
    # Test LeafNode
    leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    
    # Test ParentNode with nested structure
    parent_node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            ParentNode(
                "div",
                [
                    LeafNode("i", "italic text"),
                    LeafNode(None, "More text")
                ],
                {"class": "nested"}
            ),
            LeafNode(None, "Final text"),
        ]
    )

    # Print results
    print("TextNode:", text_node)
    print("HTMLNode props:", html_node.props_to_html())
    print("LeafNode HTML:", leaf_node.to_html())
    print("ParentNode HTML:", parent_node.to_html())

if __name__ == "__main__":
    main()