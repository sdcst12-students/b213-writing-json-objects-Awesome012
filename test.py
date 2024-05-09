#!python3

import json
import csv

#f = open('data.csv','r')
#data = f.read().strip()
#print(data)

#decoded = json.loads(data)
#print(type(decoded))
#print(decoded)

'''
Test = {
        0 = { 'name' = 'A1',
              'scores' = [
                    8,
                    7,
                    7,
                    6,
                    9.5
                ],
        1 = { 'name' = 'A2',
              'scores' = [
                    8,
                    7,
                    7,
                    6,
                    9.5
                ],
        2 = { 'name' = 'A3',
              'scores' = [
                    8,
                    7,
                    7,
                    6,
                    9.5
                ],

}
'''
thisdict = {}

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    print(data[0][1])
    test = []
    for x in data:
        number = x[0]
        del x[0]
        thisdict.update({number:x})
    print(thisdict)