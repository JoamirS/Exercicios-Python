# __dict__ and vars for instance attributes

class Person:
    current_year = 2022

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_year_birthday(self):
        return Person.current_year - self.age


data_insert = {'name': 'João', 'age': 35}
person_01 = Person(**data_insert)
person_01.name = 'Joamir'
print(person_01.name)

print(person_01.__dict__)
print(vars(person_01))
