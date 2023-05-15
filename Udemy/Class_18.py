"""
Take Care with mutable data
= - copied the value (immutable) | string
= - point to the same value in memory (mutable) | List
"""

name = 'Joamir'
another_variable = name
name = 'Paulo'
print(name)
print(another_variable)
#
# list_a = ['Luiz', 'Maria']
# list_b = list_a
#
# list_a[0] = 'Qualquer coisa'
# print(list_b)

list_a = ['Luiz', 'Maria', 1, True, 1.2]
list_b = list_a.copy()

list_a[0] = 'Qualquer coisa'
print(list_b)
