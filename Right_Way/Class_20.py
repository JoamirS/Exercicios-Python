"""
You are building a calendar to control work days at the request of HR. In this project, you will need to define which
years are leap year, and which are not to show the calendar in the correct way. Make a program to ask the corresponded
number of a certain year, right away display if this year is a leap year or not.
"""
import sys


input_year = int(input("Insira um número: "))


def is_multiple_of_400(year):
    return year % 400 == 0


def is_multiple_of_4(year):
    return year % 4 == 0


def is_multiple_of_100(year):
    return year % 100 == 0


if is_multiple_of_400(input_year):
    print(f'O ano {input_year} é bissexto.')
    sys.exit()

if is_multiple_of_4(input_year) and not is_multiple_of_100(input_year):
    print(f'O ano {input_year} é bissexto.')
else:
    print(f'O ano {input_year} não é bissexto.')
    sys.exit()

if is_multiple_of_4(input_year) and is_multiple_of_100(input_year):
    if is_multiple_of_400(input_year):
        print(f'O ano {input_year} é bissexto..')
    else:
        print(f'O ano {input_year} não é bissexto')
