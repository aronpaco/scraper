from datetime import datetime, timedelta

kell = datetime.now()
print("Current time:", kell)

current_time = kell.strftime('%H:%M')
print("Formatted current time:", current_time)

one_hour_one_minute_ago = kell - timedelta(hours=1, minutes=1)
formatted_one_hour_one_minute_ago = one_hour_one_minute_ago.strftime('%H:%M')
print("One hour and one minute ago:", formatted_one_hour_one_minute_ago)
