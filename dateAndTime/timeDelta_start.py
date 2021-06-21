from datetime import date, time, datetime, timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# printing todays date
print("todays date"+str(datetime.now()))

# printing todays date 1 year from now
print("one year from today will be: "+str(datetime.now()+timedelta(days=365)))

# Calculate date of 1 week ago. Formatted as string
print("1 week before date will be: "+str(datetime.now()-timedelta(days=7)))

# Date in 2 days and 3 weeks
print("Date in 2 days and 3 weeks=" +
      str(datetime.now()+timedelta(days=2, weeks=3)))
