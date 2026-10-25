import calendar
month, day, year = map(int, input().split())
day_index = calendar.weekday(year, month, day)
result = calendar.day_name[day_index]
print(result.upper())
