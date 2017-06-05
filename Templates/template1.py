from string import Template

my_list = [
    dict(name="Ann", food="eggs", qty=2, meal="breakfast"),
    dict(name="Michael", food="bacon", qty=10, meal="dinner"),
]


template0 = Template("$name had $qty $food for $meal")
for person in my_list:
    print(template0.substitute(person))
