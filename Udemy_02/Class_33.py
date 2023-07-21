# Decorator

def decorator_function(function):
    print('Decoradora 1')
    print(function.__name__)

    def inner(*args, **kwargs):
        print('Aninhada')
        print(args)
        print(kwargs)
        result = function(*args, **kwargs)

        return result

    return inner


@decorator_function
def sum_function(x, y):
    return x + y


ten_sum_five = sum_function(10, 5)
print(ten_sum_five)
