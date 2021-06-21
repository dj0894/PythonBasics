import calendar

# Create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2020, 1, 0, 0)
print(st)

# Create a HTML formatted calendar
htmlcalendar = calendar.HTMLCalendar(calendar.SUNDAY)
st1 = c.formatmonth(2021, 1)
print(st1)

# Loop over days of month, zeroes means that the day of week is in overlapping month
for i in c.itermonthdays(2020, 6):
    print(i)

# Scenarios based calculations
# Calculate days based on a rule: For example, consider a team meeting on the first friday of every month.
# Calculate the dates of the meetings
print("Team meeting will be on")
for m in range(1, 13):
    cal = calendar.monthcalendar(2020, m)
    weekOne = cal[0]
    weekTwo = cal[1]
    if weekOne[calendar.FRIDAY] != 0:
        meetday = weekOne[calendar.FRIDAY]
    else:
        meetday = weekTwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))
