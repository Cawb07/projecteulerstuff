'''
Created on Aug 17, 2013

https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

@author: Cawb07
'''
import time
from itertools import cycle

days_in_month = {
                  "January": 31,
                  "February": 28,
                  "March": 31,
                  "April": 30,
                  "May": 31,
                  "June": 30,
                  "July": 31,
                  "August": 31,
                  "September": 30,
                  "October": 31,
                  "November": 30,
                  "December": 31,
                  "Leap": 29
                }

months_by_num = {
                  1: "January",
                  2: "February",
                  3: "March",
                  4: "April",
                  5: "May",
                  6: "June",
                  7: "July",
                  8: "August",
                  9: "September",
                  10: "October",
                  11: "November",
                  12: "December"
                }

start = time.time()

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

date = [ [ [[] for d in range(0,32)] for m in range(0,13)] for y in range(0,2001)]

date[1900][1][1] = "Monday"
print date


cycle = cycle(days)
today = cycle.next()
print today

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)