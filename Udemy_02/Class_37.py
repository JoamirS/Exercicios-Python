# grouping values | groupby - (itertools)
from itertools import groupby

students = [
    {'Name': 'Luiz', 'Grade': 'A'},
    {'Name': 'Letícia', 'Grade': 'B'},
    {'Name': 'Fabrício', 'Grade': 'A'},
    {'Name': 'Rosemary', 'Grade': 'C'},
    {'Name': 'Joana', 'Grade': 'D'},
    {'Name': 'Eduardo', 'Grade': 'A'},
    {'Name': 'João', 'Grade': 'B'},
    {'Name': 'André', 'Grade': 'A'},
    {'Name': 'Anderson', 'Grade': 'C'},
]


def order(student_input):
    return student_input['Grade']


group_students = sorted(students, key=order)
groups = groupby(group_students, key=order)


for key, group in groups:
    print(key)
    for student in group:
        print(student)
