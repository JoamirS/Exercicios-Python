"""
Generator expression, Iterables, iterators in Python
Generator pause the task and then resume running
"""
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()  # tem __iter__e__next__

# print(next(iterator))
# print(next(iterator))

list_comprehension = [number for number in range(1000000)]
generator = (number for number in range(1000000))

print(sys.getsizeof(list_comprehension))
print(sys.getsizeof(generator))

for number in generator:
    print(number)
