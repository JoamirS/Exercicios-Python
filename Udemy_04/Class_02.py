from datetime import datetime
from pytz import timezone


date = datetime.now(timezone('America/Sao_Paulo'))
date_two = datetime.now(timezone('Asia/Tokyo'))
print(date)
print(date_two)
