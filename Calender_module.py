# import calendar
# calendar.setfirstweekday(5)
# print(calendar.calendar(2100, 2, 1, 6, 2))
# calendar.prmonth(2021, 5, 0, 0)
# print(calendar.weekday(2021, 5, 19))
# print(calendar.isleap(1700))
# calendar.prmonth(400, 2, 0, 0)
# print(calendar.leapdays(2000, 2050))
import time
print("Time after epoch is {}".format(time.time()))
date = time.gmtime(10)
start_time = time.time()
print(time.asctime(date))
local_date = time.localtime(time.time())
print(local_date)
print(time.asctime(local_date))
# print(time.process_time())
print(time.mktime(local_date))
end_time = time.time()
print(end_time-start_time)
