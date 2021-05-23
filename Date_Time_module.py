from datetime import datetime
import pytz

# country1 = 'Europe/Oslo'
# country2 = 'Asia/Kolkata'
# timezone = pytz.timezone(country1)
# x = datetime.now(tz=timezone)
# timezone = pytz.timezone(country2)
# y = datetime.now(tz=timezone)
# print(x.astimezone())
# print(y)
# print(datetime.utcnow())
# print(datetime.timestamp(x))

# print(type(x))

# for x in pytz.all_timezones:
#     print(x)
#
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])

# for x in sorted(pytz.country_names):
#     print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))

local = datetime.now()
utcTime = datetime.utcnow()

print("The local time is {}".format(local))
print("the utctime is {}".format(utcTime))

tz_local = pytz.utc.localize(local).astimezone()
tz_utc = pytz.utc.localize(utcTime)

print("Time is {} and time zone is {}".format(local,tz_local.tzinfo))
print("Time is {} and time zone is {}".format(utcTime,tz_utc.tzinfo))
print(datetime(2020, 10, 5, 12, 25, 25))