"""
Unpacking in method and function calls
"""

string = 'ABCD'
list_one = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tuple_one = 'Python', 'é', 'legal'

a, b, c, *_, penultimate, last_element = list_one
print(a, penultimate, last_element)


for name in list_one:
    print(name)

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*list_one)
print(*string)
