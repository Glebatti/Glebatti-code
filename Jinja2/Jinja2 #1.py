from jinja2 import Template

name = "Федор"
age = 28

tm = Template("Привет {{ name }}")
msg = tm.render(name = name)
print(msg)

class Person:
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

per = Person("Федор", 33)

tm = Template("Мне {{ p.getAge() }} лет и зовут {{ p.getName() }}.")
msg = tm.render(p = per)
print(msg)

# msg2 = f"Привет {name}"
# print(msg, msg2, sep="\n")

per = { "name": "Федор", "age": 34}
tm = Template("Мне {{ p.age }} лет и зовут {{ p.name }}.")
tm = Template("Мне {{ p['age'] }} лет и зовут {{ p['name'] }}.")
msg = tm.render(p = per)
print(msg)

