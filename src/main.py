from textnode import TextNode
from textnode import TextType

def main():
    textnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(textnode)

if __name__ == "__main__":
    main()
