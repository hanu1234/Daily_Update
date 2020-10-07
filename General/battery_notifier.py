import psutil
from plyer import notification
import time

battery = psutil.sensors_battery()
while True:
    percent = battery.percent
    print(percent)
    notification.notify(title="Battery Percentage", message=str(percent) + "Battery remaining", app_icon='C:\\Users\\hshivanagi\\Downloads\\battery_discharging_100.ico', timeout=100)
    time.sleep(30)
