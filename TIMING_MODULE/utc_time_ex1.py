import datetime
from time import sleep

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

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
utc_time_now1 = datetime.datetime.utcnow()
utc_time_after_10min = utc_time_now1 + datetime.timedelta(minutes=10)
sleep(60)
utc_time_now2 = datetime.datetime.utcnow()

print(utc_time_now2)
print(utc_time_after_10min)

time_delta = utc_time_after_10min - utc_time_now2
total_seconds = time_delta.total_seconds()
minutes = total_seconds/60
print(minutes)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
