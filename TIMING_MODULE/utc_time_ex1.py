import datetime
utc_time = datetime.datetime.utcnow()
print(utc_time)
# Get UTC TIME After 15 Minutes
utc_time = utc_time + datetime.timedelta(minutes=10)
print(utc_time)
hours = utc_time.strftime("%H")
minutes = utc_time.strftime("%M")
print(hours, minutes)

utc_time = utc_time + datetime.timedelta(hours=24)
print(utc_time)
