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


def option1():
    naming = input("Enter the assignment name: ")
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        print(data)
        test = []
        for x in data:
            if naming == x[1]:
                overlap1()
            else:
                print("yo")

def overlap1():
    check = input("this assignment already exists, would you like to erase it? ")
    if check == "yes":
        print("hi")
    elif check == "no":
        main()
    else:
        print("\ninvalid answer, please type yes or no")
        overlap1()
                

def option2():
    print("hey")

def option3():
    print("hello")

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
    overlap1()