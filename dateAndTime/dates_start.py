# Working with datetime lib

from datetime import date
from datetime import time
from datetime import datetime


def main():
    # printing todays date
    today = date.today()
    print("today date is ", today)
    # printing individual content of todays date
    day = date.today().day
    print("day ", day)
    year = date.today().year
    print("year ", year)
    month = date.today().month
    print("month ", month)
    days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
    weekday = days[date.today().weekday()]
    print("Today's weekday ", weekday)

# Datetime Objects

    today = datetime.now()
    print(today)  # getting current date time

    t = datetime.time(datetime.now())
    print(t)


main()
