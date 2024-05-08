#!python3

import json

#f = open('data.csv','r')
#data = f.read().strip()
#print(data)

#decoded = json.loads(data)
#print(type(decoded))
#print(decoded)

import csv

with open('data.csv', newline='') as x:
    reader = csv.reader(x)
    data = list(reader)

print(data)
print(type(data))