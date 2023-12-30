from datetime import datetime


date = datetime(2022, 4, 20, 20, 2, 50)

date_two = '2022-04-20 07:49:23'
date_format = '%Y-%m-%d %H:%M:%S'

date_three = datetime.strptime(date_two, date_format)
print(date_three)
