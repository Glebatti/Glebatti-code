from  jinja2 import Environment, FileSystemLoader ,FunctionLoader

# link = """<select name="cities">
# {% for c in cities -%}
# {% if c.id > 6 -%}
#     <option value="{{c["id"]}}">{{c["city"]}}</option>
# {% endfor %}
# </select>"""

persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0},
]

def loadTpl(path):
    if path == "index":
        return '''Имя {{u.name}}, возраст {{u.old}}'''
    else:
        return '''Данные: {{u}}'''

# file_loader = FileSystemLoader('templates')
file_loader = FunctionLoader(loadTpl)
env = Environment(loader=file_loader)

#tm = env.get_template('main.html')
tm = env.get_template('index')
msg = tm.render(u = persons[0])

print(msg)