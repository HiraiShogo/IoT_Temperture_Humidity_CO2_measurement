import datetime
now = datetime.date(2024, 8, 3)
yesterday = now - datetime.timedelta(days=1)
if now > yesterday:
    print("a")
else:
    print("b")