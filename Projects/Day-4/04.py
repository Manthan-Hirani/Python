import datetime
# from datetime import timedelta
from dateutil.relativedelta import relativedelta

a = datetime.date.today()
# a = datetime.date(2023, 11, 25)
# print(f"Current date: {a}")

# d = a.day
# m = int(a.month) + 4
# y = a.year

# print(f"Updated date: {datetime.date(y, m, d)}")

    


z = a + relativedelta(months=4)

print(f"New Date after 4 months: {z}")
