import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode
from textnode import TextNode
from textnode import TextType
from textnode import text_node_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode(props=None)
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"href": "https://boot.dev"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://boot.dev"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://boot.dev", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://boot.dev" target="_blank"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")
    
    def test_leaf_to_html_i(self):
        node = LeafNode("a", "Click me!", {"href": "https://boot.dev"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev">Click me!</a>')
    
    def test_leaf_to_html_none(self):
        node = LeafNode(None, "Just raw text")
        self.assertEqual(node.to_html(), "Just raw text")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )
        
def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()