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
    global naming
    naming = input("Enter the assignment name: ")
    for x in tester2:
        #print(tester2[x]['name'])
        if naming == tester2[x]['name']:
            overlap1()
            return
        else:
            continue
    makenew()

def overlap1():
    global naming
    global testnumber
    check = input("this assignment already exists, would you like to erase it? ")
    if check == "yes":
        for x in tester2:
            if naming == tester2[x]['name']:
                #print(tester2)
                ok = x
                continue
            else:
                #print("hi")
                continue
        testnumber = ok
        #print(testnumber)
        del tester2[ok]
        #print(tester2)
    elif check == "no":
        main()
    else:
        print("\ninvalid answer, please type yes or no")
        overlap1()
    #print(testnumber)
    makenew()

def makenew():
    newlist = []
    global naming
    global testnumber
    global tester2
    makevalue = input("Enter in Assignment Value:")
    try:
        makevalue = int(makevalue)
    except:
        print("invalid input, try again:")
        makenew()
    makevalue = int(makevalue)
    tester2.update({testnumber:{}})
    #print(tester2)
    tester2[testnumber].update({"value":makevalue})
    tester2[testnumber].update({"name":naming})
    print(f'Enter in the scores for {makevalue} students for {naming}:')
    for x in range(makevalue):
        cool = x + 1
        newvalue = input(f"{cool}: ")
        newlist.append(newvalue)
    #print(newlist)
    tester2[testnumber].update({"scores":newlist})
    print(tester2)
    jsonholder = json.dumps(tester2)
    main()

def option2():
    extra = False
    global tester2
    newlist = []
    asking = input("Enter in the assignment ID:")
    for x in tester2:
        letssee = x
        if asking == letssee:
            extra = True
            makevalue = tester2[x]['value']
            makevalue = int(makevalue)
            tester2[x].pop('scores')
            for y in range(makevalue):
                cool = y + 1
                newvalue = input(f"{cool}: ")
                newlist.append(newvalue)
            tester2[x].update({"scores":newlist})
        else:
            continue
    if extra == False:
        print("that id does not exist")
    main()

def option3():
    global tester2
    for x in tester2:
        x = str(x)
    tester2 = dict(sorted(tester2.items()))
    print(tester2)
    finallist = []
    for x in tester2:
        final = ""
        print(tester2[x])
        final = final + tester2[x]['value']
        final = final + ',' + tester2[x]['name']
        for y in tester2[x]['scores']:
            final = final + ',' + y
        print(final)
        finallist.append(final)
    print(finallist)
    with open('data.csv', 'w') as csv_file:  
        writer = csv.writer(csv_file)
        for x in finallist:
            csv_file.write(x)
            csv_file.write('\n')
            print(x)

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

if __name__ == "__main__":
    main()