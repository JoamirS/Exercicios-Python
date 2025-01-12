"""
Make a program to read two partial notes for a student in a subject over the course of a semester, and calculate your
average. So, display which is the concept the student are.

Between 9 and 10 > A
Between 7.5 and 9.0 > B
Between 6 and 7.5 > C
Between 4 and 6 > D
Between 4 and 0 > E
"""

input_first_grade = float(input('Qual é a primeira nota? '))
input_second_grade = float(input('Qual é a segunda nota? '))

average_two_grades_student = (input_second_grade + input_first_grade) / 2

if 9 < average_two_grades_student <= 10:
    print('Aluno nota A')
elif 8 < average_two_grades_student <= 9:
    print('Aluno nota B')
elif 6 < average_two_grades_student <= 8:
    print('Aluno nota C')
elif 4 < average_two_grades_student <= 6:
    print('Aluno nota D')
elif 0 < average_two_grades_student <= 4:
    print('Aluno nota E')