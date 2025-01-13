"""
You are building a calendar to control work days at the request of HR. In this project, you will need to define which
years are leap year, and which are not to show the calendar in the correct way. Make a program to ask the corresponded
number of a certain year, right away display if this year is a leap year or not.
"""

input_year = int(input("Insira um número: "))


def is_multiple_of_400(year):
    return year % 400 == 0


def is_multiple_of_4(year):
    return year % 4 == 0


def is_multiple_of_100(year):
    return not year % 100 == 0


# def all_conditions_true() -> bool:
#     """check if all conditions are true"""
#     check_all_conditions_leap_year_list = [
#         is_multiple_of_4(input_year),
#         is_multiple_of_400(input_year)
#     ]
#     return all(check_all_conditions_leap_year_list)
#
#
# def check_if_are_leap():
#     if all_conditions_met():
#         print('O ano é bissexto')
#     else:
#         print('O ano não é bissexto')


if __name__ == "__main__":
    check_if_are_leap()