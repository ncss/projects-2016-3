import re

tokenisingExpr = re.compile(r'(?:\{(?=%|\{))(.*?)(?:%|\})\}')

class ParseError(Exception):
    def __init__(self, msg):
        return super(msg)

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
        return eval(self.content, {}, self.context)

class IncludeNode(Node):
    def evaluate(self, context):
        try:
            with open(self.content) as f:
                return parse_template(f.read()).eval
        except IOError():
            raise ParseError('Failed to read file')

def _tokenise(template):
    print(re.split(tokenisingExpr, template))
        
def _parse_template(template, upto, parent):
    pass
        
def parse_template(template):
    return _parse_template(template, 0, None)
    
def render_template(template, context):
    pass

if __name__ == '__main__':
    _tokenise("""{% include header.html %}
<section id='profile'>
<h1>{{ person.name }}</h1>
<ul id='friends-list'>
{% for f in person.friends %}
<li class='friend'>
{{ f.name.title() }} {{ f.age }} {% if f.gender == 'M' %}Male{% else %}Female{% end if %}
</li>
{% end for %}
</ul>
</section>
{% include footer.html %}""")