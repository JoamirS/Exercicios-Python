"""
__new__ and __init__ in Python Classes
__new__ is a method responsible for create and return the new object. By that receive cls.
__new__ must be return the new object
__init__ is a responsible method for initiate an instance. By that init receive self.
__init__ must be return nothing (None)
object is a super class of a class
"""


class A:
    def __new__(cls):
        print('Antes de criar a instância')
        instance = super().__new__(cls)
        print('Depois')
        instance.x = 200
        return instance

    def __init__(self):
        print('Eu sou o init')

    def __repr__(self):
        return 'A()'


a = A()
print(a)
print(a.x)
