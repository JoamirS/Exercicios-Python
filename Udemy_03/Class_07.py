"""
Class Methods + factories
They are methods where self will be cls, in other words, instead to receive an instance in first parameter,
we will receive class itself
"""


class Person:
    year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def class_method(cls):
        print('Hey')

    @classmethod
    def create_with_50_years_old(cls, name):
        return cls(name, 50)

    @classmethod
    def create_anonymous(cls, age):
        return cls('Anônimo', age=age)


person_01 = Person('João', 34)
print(Person.year)
Person.class_method()
person_02 = Person.create_with_50_years_old('Helena')
print(person_02.age)
person_03 = Person.create_anonymous(23)
print(person_03.name)
print(person_03.age)
