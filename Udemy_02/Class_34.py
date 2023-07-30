# Decorators with functions

def function_factory(function):
    print('Decorators 1')

    def inner(*args, **kwargs):
        print('Aninhada')
        result = function(*args, **kwargs)
        return result
    return inner


def factory_decorators(a, b, c):
    return function_factory


@factory_decorators(1, 2, 3)
def function_sum(x, y):
    return x + y


multiply = function_factory(lambda x, y: x * y)
ten_sum_five = function_sum(10, 5)
