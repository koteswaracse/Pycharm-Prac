#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Alice']: ", dict['Alice'])

dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict1['Age'] = 8; # update existing entry
dict1['School'] = "DPS School"; # Add new entry

print ("dict['Age']: ", dict1['Age'])
print ("dict['School']: ", dict1['School'])

dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict2['Name']; # remove entry with key 'Name'
dict2.clear();     # remove all entries in dict
del dict2 ;        # delete entire dictionary

print ("dict['Age']: ", dict2['Age'])
print ("dict['School']: ", dict2['School'])

dict2 = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("dict['Name']: ", dict2['Name'])

dict2 = {['Name']: 'Zara', 'Age': 7}
print ("dict['Name']: ", dict2['Name'])
