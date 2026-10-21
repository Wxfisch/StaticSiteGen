from textnode import TextNode, TextType

def main():
    text_node = TextNode("Placeholder Value", TextType.PLAIN, "https://www.kagi.com")
    print(f"TextNode({text_node.text}, {text_node.text_type}, {text_node.url})")

if __name__ == "__main__":
    main()