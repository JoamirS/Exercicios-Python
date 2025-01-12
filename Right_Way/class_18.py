"""
Make a program to read a number and display the correspondent day. (1 - Sunday, 2 - Monday).
If input another number, the value will be invalid.
"""
import sys

input_day_int = int(input('Qual é o dia da semana que você deseja? '))

day_of_week_list = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

if input_day_int not in list(range(1, 8)):
    print('Número inválido')
    sys.exit()

for index, day in enumerate(day_of_week_list):
    index += 1
    if index == input_day_int:
        print(day)
