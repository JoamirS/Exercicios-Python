"""
postponing the function (closure)
"""


def sum_function(x, y):
    return x + y


def multiply(x, y):
    return x * y


def create_function(function, x):
    def inside(y):
        return function(x, y)
    return inside


sum_with_five = create_function(sum_function, 5)
multiply_for_ten = create_function(multiply, 10)

print(sum_with_five(10))
print(multiply_for_ten(10))
