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
    print('Include a month to see that calendar\nInclude a month and year for years other than 2020\n')


def show_calendar(args):
    now = datetime.now()
    if len(args) > 2:
        if test_month(args[1]) and test_year(args[2]):
            month = int(args[1])
            year = int(args[2])
        else:
            return False
    elif len(args) == 2:
        if test_month(args[1]):
            month = int(args[1])
            year = now.year
        else:
            return False
    else:
        month = now.month
        year = now.year
    cal = calendar.TextCalendar(firstweekday=0)
    print(cal.formatmonth(year, month, w=0, l=0))
    return True


def test_month(month):
    if not month.isdigit() or int(month) > 12:
        return False
    return True


def test_year(year):
    if not year.isdigit():
        return False
    return True


# main program
if not show_calendar(sys.argv):
    rules()
