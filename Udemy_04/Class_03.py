from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

formatted = '%d/%m/%Y %H:%M:%S'
initial_date = datetime.strptime('20/04/1987 09:30:30', formatted)
final_date = datetime.strptime('12/12/2022 08:20:20', formatted)
print(final_date - initial_date)

# delta = timedelta(days=10, hours=2)
delta = relativedelta(final_date, initial_date)
print(delta.days, delta.years)
# print(initial_date - delta)
# print(final_date + relativedelta(seconds=50))
