"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


def rules():
    print('Enter a month to see that calendar\nEnter a month and year for years other than 2020\n')


def show_calendar(args):
    arglist = args.split()
    now = datetime.now()
    if len(args) > 1:
        month = int(arglist[0])
        year = int(arglist[1])
    elif len(args) == 1:
        month = int(arglist[0])
        year = now.year
    else:
        month = now.month
        year = now.year
    cal = calendar.TextCalendar(firstweekday=0)
    print(cal.formatmonth(year, month, w=0, l=0))


def test_input(case):
    testing = case.split()
    if len(testing) > 1:
        if test_month(testing[0]) and test_year(testing[1]):
            return True
    elif len(testing) == 1:
        if test_month(testing[0]):
            return True
    else:
        return True
    return False


def test_month(month):
    if not month.isdigit() or type(int(month)) != int or int(month) > 12:
        print("Month False")
        return False
    print("Month True")
    return True


def test_year(year):
    if not year.isdigit() or type(year) != int:
        print("Year False")
        return False
    print("Year True")
    return True


rules()
uinput = input()
success = test_input(uinput)
if success:
    show_calendar(uinput)
else:
    rules()
