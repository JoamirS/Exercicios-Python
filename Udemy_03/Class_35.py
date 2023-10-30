"""
Metaclasse they are deeper spells than 99% of users should care about.
If you want to know if you need them, you don't.
"""


class Person(metaclass=type):
    def __new__(cls, *args, **kwargs):
        print('Meu new')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print('Meu init')
        self.name = name


person_01 = Person('Joamir')
