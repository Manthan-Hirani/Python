import datetime
from datetime import timedelta

x = datetime.datetime.now()
print(f"Old date: {x}")

y = x + timedelta(days=7, hours=12)

print(f"New Date: {y}")