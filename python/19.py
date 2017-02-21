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
                  "Leap": 29,
                  "March": 31,
                  "April": 30,
                  "May": 31,
                  "June": 30,
                  "July": 31,
                  "August": 31,
                  "September": 30,
                  "October": 31,
                  "November": 30,
                  "December": 31
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

leap =          {
                  1: "January",
                  2: "Leap",
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
cycle = cycle(days)

date = [ [ [[] for d in range(32)] for m in range(13)] for y in range(2014)]

for y in range(1900, 2014):
    if y%4 == 0 and y != 2000 and y != 1900:
        for m in range(1,13):
            for d in range(1, days_in_month[leap[m]]+1):
                today = cycle.next()
                date[y][m][d] = today
        
    elif y%400 == 0 and y == 2000:
        for m in range(1,13):
            for d in range(1, days_in_month[leap[m]]+1):
                today = cycle.next()
                date[y][m][d] = today
        
    else:
        for m in range(1,13):
            for d in range(1, days_in_month[months_by_num[m]]+1):
                today = cycle.next()
                date[y][m][d] = today

print date[2013][8][22]

the_Wednesdays = 0

for y in range(1901, 2000):
    for m in range(1,13):
        if date[y][m][1] == "Wednesday":
            the_Wednesdays += 1

print the_Wednesdays

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)