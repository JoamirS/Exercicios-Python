"""
Enumerate - enumerates iterables (indexes)
"""

list_name = ['Maria', 'Helena', 'Luiz']
list_name.append('João')

list_name_enumerate = enumerate(list_name)
print(next(list_name_enumerate))

for item in enumerate(list_name):
    index, name = item
    print(index, name)
