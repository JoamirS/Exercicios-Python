# Decorator functions and decorators with classes


def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = my_repr
    return cls


class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr


class SuperTime:
    ...


def my_planet(method):
    def internal(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        print(result, 'Teste')
        if 'Terra' in result:
            return 'Você está em casa'

        return result
    return internal


@add_repr
class Team(SuperTime, MyReprMixin):
    def __init__(self, name):
        self.name = name


@add_repr
class Planet(MyReprMixin):
    def __init__(self, name):
        self.name = name

    @my_planet
    def talk_name(self):
        return f'O planeta é {self.name}'


brasil = Team('Brasil')
portugal = Team('Portugal')
earth = Planet('Terra')
marte = Planet('Marte')

# print(brasil)
# print(portugal)
# print(earth)
# print(marte)
print(earth.talk_name())
# print(marte.talk_name())
