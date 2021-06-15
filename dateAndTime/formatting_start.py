# Example for formatting time and date output

from datetime import datetime


def main():
    # Times and date can be formatted using a set of predefined string control codes
    now = datetime.now()

    print(now.strftime("The current year is: %Y"))

    # date formatting
    print(now.strftime("%a,%d, %B,%y"))
    print(now.strftime("Locale date and time: %c"))
    print(now.strftime("Locale date : %x"))
    print(now.strftime("Locale date : %X"))

    # time formatting
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("Current time in 24 hr clock: %H:%M:%S %p"))


main()
