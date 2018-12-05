import datetime
import pytz
dt_now = datetime.datetime.now(tz=pytz.timezone('Hongkong'))
print(dt_now)

print(dt_now.strftime("%d %B, %Y"))
print(dt_now.isoformat()
