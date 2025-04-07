import re
from textnode import TextNode, TextType

'''
It takes a list of "old nodes", a delimiter, and a text type. 
It should return a new list of nodes, where any "text" type nodes 
in the input list are (potentially) split into multiple nodes based on the syntax. 
For example, given the following input:

node = TextNode("This is text with a `code block` word", TextType.TEXT)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
'''
#TODO - Markdown parsers often support nested inline elements. 
# For example, you can have a bold word inside of italics:
# This is an _italic and **bold** word_.
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    results = []
    extracted_text = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    for ex in extracted_text:
        results.append((ex))
    return results

def extract_markdown_links(text):
    results = []
    extracted_text = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    for ex in extracted_text:
        results.append((ex))
    return results

# def extract_markdown_images(text):
#     pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
#     matches = re.findall(pattern, text)
#     return matches


# def extract_markdown_links(text):
#     pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
#     matches = re.findall(pattern, text)
#     return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link_alt, link_url in links:
            # extract the text from the node and store in texttype text
            section = original_text.split(f"[{link_alt}]({link_url})", 1)
            if len(section) != 2:
                raise ValueError(f"invalid markdown, link section not closed")
            if section[0] != "":
                new_nodes.append(TextNode(text=section[0], text_type=TextType.TEXT))
            new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
            original_text = section[1]
        if section[1] != "":
            new_nodes.append(TextNode(section[0], TextType.TEXT))
    return new_nodes

# convert text to textnodes
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

if __name__ == "__main__":
    node = TextNode(
    "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    print(new_nodes)
    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    print(new_nodes)
    text = f"This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(text_to_textnodes(text))
