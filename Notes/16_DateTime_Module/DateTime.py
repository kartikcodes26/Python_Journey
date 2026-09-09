from datetime import datetime as dt
from datetime import date, timedelta

tday = dt.now()
print(tday.year)
print(tday.month)
print(tday.day)
print(tday.hour)
print(tday.weekday())
print(tday.isoweekday())

tdelta = timedelta(days = 10)
print(tday - tdelta)

bday = date(2027, 7, 9)
till_bday = bday - tday.date()
print(till_bday)
print(till_bday.total_seconds())
