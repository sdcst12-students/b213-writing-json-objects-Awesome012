#!python3
# Create a user interface to have the user enter in data for a teacher
# Use the menu options below to help navigate your program:
# User input has been encloded by _ _
"""
1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 1_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 0

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _0_
Enter in the scores for 10 students for Assignment 1:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_
Complete.

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 2_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 1

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _1_

Enter in the scores for 10 students for Assignment 2:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_

"""

import json
import csv

thisdict = {}
testnumber = 0
numberlist = []

test1 = 0
test2 = ""
test3 = []

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    #print(data)
    try:
        #print(data[0][1])
        for x in data:
            number = x[0]
            thisdict.update({testnumber:{}})
            thisdict[testnumber].update({"value":number})
            x.pop(0)
            thisdict[testnumber].update({"name":x[0]})
            x.pop(0)
            thisdict[testnumber].update({"scores":x})
            testnumber = testnumber + 1
            #print(testnumber)
        tester = json.dumps(thisdict)
        tester2 = json.loads(tester)
        #print(tester2)
    except:
        print("")
    jsonholder = json.dumps(tester2)

def option1():
    test1 = 0
    test2 = ""
    test3 = []
    global naming
    naming = input("Enter the assignment name: ")
    for x in tester2:
        #print(tester2[x]['name'])
        if naming == tester2[x]['name']:
            test1 = tester2[x]['value']
            test2 = tester2[x]['name']
            test3 = tester2[x]['scores']
            same = True
            resting = maker(test1,test2,test3)
            return
        else:
            continue
    resting = resting = maker(test1,test2,test3)

class maker:
    value = 0
    name = ""
    scores = []

    def __init__(self,a,b,c):
        self.value = a
        self.name = b
        self.scores = c
        pass
        self.throttle()

def option2():
    print("")

def option3():
    print("")

def main():
    print("\n1. Create an Assignment \n2. Enter in Assignment Scores \n3. Write your data to file")
    choice = input("Enter in Your Choice: ")
    if choice == "1":
        option1()
    elif choice == "2":
        option2()
    elif choice == "3":
        option3()
    else:
        print("\ninvalid choice, try again:")
        main()