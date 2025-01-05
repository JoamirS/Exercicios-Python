"""
You are building a calendar to control work days at the request of HR. In this project, you will need to define which
years are leap year, and which are not to show the calendar in correct way. Make a program to ask the correspond number
of a certain year, right away display if this year is leap year or not.
"""

input_year = int(input("Insira um número: "))

def check_leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

def is_centenary_year(year):
    if year % 100 == 0:
        return True
    else:
        return False

first_check_leap_year = check_leap_year(input_year)
second_check_leap_year = is_centenary_year(input_year)

if first_check_leap_year is not second_check_leap_year:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')

if first_check_leap_year and second_check_leap_year:
    if input_year % 400 == 0:
        print('O ano é centenário')
    else:
        print('O ano é centenário, mas não é bissexto.')
