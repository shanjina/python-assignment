from datetime import date, timedelta

today = date.today()
next_week = today + timedelta(days=7)

print("Today's date:", today)
print("Date after 7 days:", next_week)