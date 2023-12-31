from datetime import datetime

formatted = '%d/%m/%Y'
# date = datetime(2022, 12, 13, 7, 59, 23)

date = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(date)

print(date.strftime(formatted))
print(date.strftime('%d/%m/%Y %H:%M'))
print(date.strftime('%Y'), date.year)
