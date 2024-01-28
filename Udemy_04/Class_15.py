"""
Using calendar to calendars and dates
calendar used for generic things of calendar and dates.
With calendar, do you know thinks like:
    - Which the last name of month
    - What is the name and number of certain day
    - Create a calendar
    - Work with specific things of calendar
"""
import calendar
# print(calendar.calendar(2024))
# print(calendar.month(2024, 1))
''' The first day said on day of the week and the number od last day at the month'''
print(calendar.monthrange(2024, 1))
print(list(enumerate(calendar.day_name)))

day_week_first_day_month, number_last_day_month = calendar.monthrange(2024, 1)
print(calendar.day_name[day_week_first_day_month])
print(calendar.day_name[calendar.weekday(2024, 1, number_last_day_month)])
