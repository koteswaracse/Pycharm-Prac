#!/usr/bin/python

var = 100
if ( var == 100 ) : print ("Value of expression is 100")
print ("Good bye!")

var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')

print ("My name is %s and weight is %d kg!" % ('Zara', 21))

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)

print ('C:\\nowhere')
print (r'C:\\nowhere')

print (u'Hello, world!')

