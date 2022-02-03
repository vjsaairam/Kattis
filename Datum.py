import datetime

days = ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday', 'Saturday', 'Sunday']
day,month = map(int,input().split())
d = datetime.datetime(2009, month, day).weekday()
print(days[d])
