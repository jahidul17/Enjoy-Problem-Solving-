import calendar

month, day, year= list(map(int, input().split()))

ans= calendar.weekday(year,month,day)
day_names=calendar.day_name[ans]
print(day_names.upper())

# print (calendar.TextCalendar(firstweekday=5).formatyear(2035))
