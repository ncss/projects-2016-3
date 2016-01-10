import re
import os
tokenisingExpr = re.compile(r'(?:\{(?=%|\{))(.*?)(?:%|\})\}')

class ParseError(Exception):
    def __init__(self, msg):
        return super().__init__(msg)

class Node:
    def __init__(self, content, parent):
        self.content = content
        self.parent = parent
        
    def evaluate(self, context):
        raise NotImplementedError()

class TextNode(Node):
    def evaluate(self, context):
        return self.content
        
class PythonNode(Node):
    def evaluate(self, context):
        return eval(self.content, {}, context)

class IncludeNode(Node):
    def evaluate(self, context):
        try:
            with open(self.content) as f:
                return render_template(f.read(), context)
        except FileNotFoundError:
            raise ParseError('\nIncluded file: {} is nonexistent'.format(self.content))

class IfNode(Node):
    def evaluate(self):
        pass

class GroupNode(Node):
    def evaluate(self, context):
        nodestr = []
        for node in self.content:
            nodestr.append(node.evaluate(context))
        return ''.join(str(i) for i in nodestr)
    
def _tokenise(template):
    return re.split(tokenisingExpr, template)
        
def _parse_template(template, upto, parent):
    root_node = GroupNode([], parent)
    tokenvalues = _tokenise(template)
    content = []
    for token in tokenvalues:
        if token.startswith('{ '):
            token = PythonNode(token[2:-1], root_node)
        elif token.startswith('% include'):
            token = IncludeNode(token[len('% include '):-1], root_node)
        else:
            token = TextNode(token, root_node)
        content.append(token)
    root_node.content = content
    return root_node
        
def parse_template(template):
    return _parse_template(template, 0, None)
    
def render_template(template, context):
    return parse_template(template).evaluate(context)

def render_file(filename, context):
    try:
        with open(filename) as f:
            os.chdir(os.path.dirname(os.path.abspath(filename)))
            return render_template(f.read(), context)
    except FileNotFoundError:
        raise ParseError('Tried to render nonexistent file')
if __name__ == '__main__':
    render_file('test.html', {'person': 0, 'title':1, 'age':2})
    print(render_template("""{{ a }} {% include test.html %} {{ title }}""", {'person': 0, 'title':1, 'age':2}))