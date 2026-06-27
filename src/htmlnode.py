class HTMLNode():

    def __init__(self, tag: str = None, value: str = None, children: list = None, props:dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        result = ""
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props:dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError()
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag: str, children: list, props: dict = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag")
        if self.children is None:
            raise ValueError("Missing children")
        inner_html = ""
        for child in self.children:
            inner_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"