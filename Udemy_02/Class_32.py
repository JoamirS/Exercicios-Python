"""
Decorators functions.
Decorate: add, remove, restrict and change.
Decorator functions are functions that decorate other functions.
Decorators are used to make Python use decorators functions in another functions
"""


def create_function(function):
    def inside(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        result = function(*args, **kwargs)
        print('Ok, agora você foi decorada')
        return result
    return inside


@create_function
def string_inverse(string):
    print(f'{string_inverse.__name__}')
    return string[::-1]


def is_string(parameter):
    if not isinstance(parameter, str):
        raise TypeError('Parameter deve ser uma string')


inverted = string_inverse('Luiz')

print(inverted)
