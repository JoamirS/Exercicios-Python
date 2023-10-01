"""
abstractmethod is any already decorated method.
It's possible to create @property, @setter @classmethod, @staticmethod, and normal methods like abstract, for that use
@abstractmethod like as a more internal decorator.
'Foo' and 'Bar' are words used like placeholder for words than can change in programming.
"""

from abc import ABC, abstractmethod


class AbstractFOO(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def get_name(self, name):
        self.name = name


class Foo(AbstractFOO):
    def __init__(self, name):
        super().__init__(name)
        print('Sou inútil')

    @AbstractFOO.get_name.setter
    def get_name(self, name):
        self.name = name


foo = Foo('Bar')
print(foo.get_name)
foo.get_name = 'Joamir'
print(foo.get_name)
