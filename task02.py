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
#print(tester2)

class cool:
    def option1(self):
        global naming
        naming = input("Enter the assignment name: ")
        for x in tester2:
            #print(tester2[x]['name'])
            if naming == tester2[x]['name']:
                self.overlap1()
                return
            else:
                continue
        self.makenew()

    def overlap1(self):
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
            self.main()
        else:
            print("\ninvalid answer, please type yes or no")
            self.overlap1()
        #print(testnumber)
        self.makenew()

    def makenew(self):
        newlist = []
        global naming
        global testnumber
        global tester2
        makevalue = input("Enter in Assignment Value:")
        try:
            makevalue = int(makevalue)
        except:
            print("invalid input, try again:")
            self.makenew()
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
        self.main()

    def option2(self):
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
        self.main()

    def option3(self):
        global tester2
        for x in tester2:
            x = str(x)
        #print(tester2)
        finallist = []
        for x in tester2:
            tester2[x]['value'] = str(tester2[x]['value'])
            final = ""
            print(tester2[x])
            final = final + tester2[x]['value']
            final = final + ',' + tester2[x]['name']
            for y in tester2[x]['scores']:
                final = final + ',' + y
            #print(final)
            finallist.append(final)
        #print(finallist)
        with open('data.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for x in finallist:
                csv_file.write(x)
                csv_file.write('\n')
                #print(x)

    def option4(self):
        asking = input("Enter in the assignment ID:")
        for x in tester2:
            letssee = x
            if asking == letssee:
                print(tester2)
                ok = x
        del tester2[ok]
        self.main()

    def option5(self):
        check = input("Enter in id or press 'all' to see scores. or type 'id' to see list of ids: ")
        for x in tester2:
            if check == x:
                testnumber = 1
                print(f"[id:{x}] {tester2[x]['name']}: ")
                for y in tester2[x]['scores']:
                    print(f"{testnumber}. {y}")
                    testnumber = testnumber + 1
                extra = input("press enter to go back to menu")
                self.main()
            elif check == "all":
                    testnumber = 1
                    print(f"[id:{x}] {tester2[x]['name']}: ")
                    for y in tester2[x]['scores']:
                        print(f"{testnumber}. {y}")
                        testnumber = testnumber + 1
            elif check == "id":
                print(f"[id:{x}] {tester2[x]['name']}: ")
        print("id does not exist or invalid input")
        extra = input("press enter to go back to menu")
        self.main()
        
    def main(self):
        print("\n1. Show Assignments + Data\n2. Create an Assignment \n3. Enter/Edit Assignment Scores\n4. Delete An Assignment \n5. Write your data to file\n")
        choice = input("Enter in Your Choice: ")
        if choice == "1":
            self.option5()
        elif choice == "2":
            self.option1()
        elif choice == "3":
            self.option2()
        elif choice == "4":
            self.option4()
        elif choice == "5":
            self.option3()
        else:
            print("\ninvalid choice, try again:")
            self.main()

    def __init__(self):
        self.main()

if __name__ == "__main__":
    tester3 = cool()