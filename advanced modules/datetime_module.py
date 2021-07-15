import datetime
mydate = datetime.date.today()
print('year is',mydate.year)
print('month is',mydate.month)
print('day is',mydate.day)
print(mydate.ctime())

mytime = datetime.time(20,44,55)
print(mytime)

#now to print both date and time

from datetime import datetime
mydatetime = datetime(2021,7,9,22,31,00)
print(mydatetime)