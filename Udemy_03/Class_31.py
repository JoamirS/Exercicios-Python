# Decorator classes

class Multiply:
    def __init__(self, func):
        self.func = func
        self._multiplicator = 10
        print(func.__name__)

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result * self._multiplicator


@Multiply
def sum_function(x, y):
    return x + y


two_twice = sum_function(2, 2)
print(two_twice)

