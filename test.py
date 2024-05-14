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
Test = {
        0 : { 'name' : 'A1',
              'scores' : [
                    8,
                    7,
                    7,
                    6,
                    9.5
                ]
        },
        1 : { 'name' : 'A2',
              'scores' : [
                    8,
                    7,
                    7,
                    6,
                    9.5
                ]
        },
        2 : { 'name' : 'A3',
              'scores' : [
                    8,
                    7,
                    7,
                    6,
                    9.5
                ]
        }

}
for x in Test:
    print(x)



thisdict = {}
testNumber = 0
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    test = []
    for x in data:
        number = x[0]
        del x[0]
        thisdict.update({testNumber:{}})
        thisdict[testNumber].update({"name":number})
        thisdict[testNumber].update({"scores":x})
        testNumber = testNumber + 1
    print(thisdict)

with open('data.csv', 'r') as file:
    file = map(str, file)
    line = "".join(file)
    cool = str(line)
    tester = json.dumps(cool)
    awesome = json.loads(tester)
    print(tester)
    filename = "dbase.txt"
    try:
        file = open(filename,'w')
        file.write(awesome)
        print("Write complete")
    except Exception as e:
        print(f"An error occurred {e}")


print(awesome)