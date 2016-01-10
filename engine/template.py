import re
import os
from collections import namedtuple
ForTag = namedtuple('ForTag', ['iterator', 'iterable', 'child_group'])
tokenisingExpr = re.compile(r'(?:\{(?=%|\{))(.*?)(?:%|\})\}')
forTokenising = re.compile(r'% for (.*) in (.*)')

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

class ForNode(Node):
    def __init__(self, parent, iterator, iterable, child_group):
        self.parent = parent
        self.iterator = iterator
        self.iterable = iterable
        self.child_group = child_group

    def evaluate(self, context):
        iterable = eval(self.iterable, {}, context)
        for_list = []
        for item in iterable:
            context = dict(context)
            context[self.iterator] = item
            for_list.append(self.child_group.evaluate(context))
        return ''.join(str(i) for i in for_list)


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

def _notFinished(parent, lookingAt, template):
    if lookingAt >= len(template):
        return False
    lookingAt = template[lookingAt]
    if isinstance(parent, ForNode):
        if lookingAt == '% end for ':
            return False
    return True

def _parse_template(template, upto, parent):
    root_node = GroupNode([], parent)
    content = []
    index = upto
    while _notFinished(parent, index, template):
        token = template[index]
        offset = None
        if token.startswith('{'):
            token = PythonNode(token[1:].strip(), root_node)
        elif token.startswith('% include'):
            token = IncludeNode(token[len('% include '):-1], root_node)
        elif token.startswith('% for'):
            for_token = re.match(forTokenising, token)
            iterator, iterable = for_token.group(1).strip(), for_token.group(2).strip()
            token = ForNode(root_node, iterator, iterable, None)
            group_node, offset = _parse_template(template, index + 1, token)
            token.child_group = group_node
        else:
            token = TextNode(token, root_node)
        content.append(token)
        if offset is not None:
            index = offset
        index += 1
    root_node.content = content
    return (root_node, index)
        
def parse_template(template):
    tokenvalues = _tokenise(template)
    return _parse_template(tokenvalues, 0, None)
    
def render_template(template, context):
    return parse_template(template)[0].evaluate(context)

def render_file(filename, context):
    try:
        with open(filename) as f:
            currentDirectory = os.getcwd()
            os.chdir(os.path.dirname(os.path.abspath(filename)))
            rendered = render_template(f.read(), context)
            os.chdir(currentDirectory)
            return rendered

    except FileNotFoundError:
        raise ParseError('Tried to render nonexistent file')
if __name__ == '__main__':
    render_file('test.html', {'person': 0, 'title':1, 'age':2})
    print(render_template("""{{ a }} {% include test.html %} {{ title }}""", {'person': 0, 'title':1, 'age':2}))