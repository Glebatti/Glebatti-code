from jinja2 import Template

data = """{% raw %}Модуль Jinja вместо определения {{ name }} подставляет соответствующее значение{% endraw %}"""
link = """В HTML-документе ссылки определяются так:<a href="#">Ссылка</a>"""

tm = Template("{{link|e}}") # экранирование символов
msg = tm.render(link=link)

print(msg)

cities = [{"id": 1, "city":"Москва"},
          {"id": 5, "city":"Тверь"},
          {"id": 7, "city":"Минск"},
          {"id": 8, "city":"Смоленск"},
          {"id": 11, "city":"Калуга"}]

link = """<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c["id"]}}">{{c["city"]}}</option>
{%elif c.city == "Москва" -%}
    <option>{{c["city"]}}</option>
{%else -%}
    {{c["city"]}}
{% endif -%}
{% endfor -%}
</select>"""

tm = Template(link)
msg = tm.render(cities = cities)

print(msg)