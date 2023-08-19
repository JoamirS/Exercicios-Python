"""
group by -  grouping values (itertools)
"""
from itertools import groupby

student = [
    {'Name': 'Luiz', 'Grade': 'A'},
    {'Name': 'Letícia', 'Grade': 'B'},
    {'Name': 'Fabrício', 'Grade': 'A'},
    {'Name': 'Rosemary', 'Grade': 'C'},
    {'Name': 'Joana', 'Grade': 'D'},
    {'Name': 'João', 'Grade': 'A'},
    {'Name': 'Eduardo', 'Grade': 'A'},
    {'Name': 'André', 'Grade': 'A'},
    {'Name': 'Anderson', 'Grade': 'C'}
]

students = ['a', 'a', 'a', 'b', 'c']
groups = groupby(sorted(students))

for key, group in groups:
    print(key)
    print(group)
