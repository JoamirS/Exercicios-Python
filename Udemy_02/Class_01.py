"""
args - unnamed arguments
*-* args (packing and unpacking)
"""

# unpacking reminder
one_variable, two_variable, *rest = 1, 2, 3, 4
print(rest)


def sum_function(*args):
    print(args)


sum_function(1, 2, 3, 4, 5, 6)

numbers = 1, 2, 3, 4, 5, 67, 34
sum_numbers = sum(*numbers)
print(sum_numbers)
