#README.md

##TEMPLATE ENGINE SYNTAX
###TAGS:

- `{{ expr }}` This tag is used to output the result of any valid Python expression into the HTML document in place of the tag. The output should be properly escaped so invalid HTML is not produced. Ensure there is a space between `{{` and the Python expression and `}}`.
  - e.g. `<h1>{{ person.name }}'s Profile</h1>`
  - e.g. `<li>{{ person.name }} is a doctor.</li>`

- `{% include path %}` This tag is used to include another template file in place of the tag. The `path` argument should be the path to the template HTML file. Does not require single quotes.
  - e.g. `{% include header.html %}`

- `{% for dest in src %}X{% end for %}` This tag is used to repeatedly execute the template code `X` for every element in the variable `src`. Every time `X` is executed, the current value of the variable `dest` is added to the context of `X`. Requires `{% end for %}` to close the `for` statement.
  - e.g. `{% for friend in person.friends %}<li class='friend'>{% include friend.html %}</li>{% end for %}`

- `{% if predicate %}X{% end if %}` This tag is used to conditionally output values. The template code `X` will only be executed if `predicate` evaluates to `True`.
  - e.g. `{% if person.friends %}{{ person.name }} has {{ len(person.friends) }} friends!{% end if %}`




## `render_file` FUNCTION

1. First you must import the engine.py file and the function `render_file` and `ParseError`.
  - e.g. `from engine import render_file, ParseError`

2. To use `render_file` you need the path to the template and the context (a dictionary). The context must define any variables that have been used in the template along with their corresponding values.
  - e.g. `print(render_file('templates/example.html', {"name": 'Henry'}))`
