#!/usr/bin/python
import time;  # This is required to include time module.
import calendar;

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print ("1Local current time :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("2Local current time :", localtime)

cal = calendar.month(2018, 12)
print ("Here is the calendar:")
print (cal)
