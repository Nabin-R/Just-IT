
pStudy = input("Enter your program of study: ").title()
curProgram = "Bootcamp"
 
# "Predict, then Run, and then Investigate"
 
# check the condition that pStudy value is same as the value held in curProgram

# do something/execute the line of code if the condition is checked above true/met - welcome
 
# The block(else) of code will be executed if the codition in the if block is not true/not met
 
if pStudy == curProgram:
    print("Predict, then Run, and then Investigate")
else:
    print(":(")

"Task 1: Using if and else"
#1. Create a program that finds the minimum value between two numbers using if else##
 
minV = 20
maxV = 230

userIn = input(f"Select a Value between {minV} and {maxV}: ")

if int(userIn) >= minV and  userIn <= userIn:
    print("User input accepted")
    if int(userIn) == minV:
        print("Input is minimum value")
    elif int(userIn) == maxV:
        print("Input is maximum value")
    else:
        print("Input is between the values")
else:
    print("Number is out of bounds")

"Task 2"
# 2.Create a python program to check user's password and print "Logged In" if successful
# else "Not Logged In“ when unsuccessful.

password = "python"
userIn = input("Type Password: ")

if userIn == password:
    print("Login successful")
else:
    print("Login unsuccessful")

#ToDo: Task 1: Using if elif and else
# Create a Menu program that allows users to select between three subject choices
# User must be presented with the value assoiciated with each choice
# for example 1. Music, 2. Maths ....
# A choice must also be available for the user to exit the program
# A message using the print function must be display as per the user choice
    
subjectChoice = ["Maths", "English", "Computer Science", "Exit"]
userInput = input(f"Select a subject of interest from the list \n 1. {subjectChoice[0]} \n 2. {subjectChoice[1]} \n 3. {subjectChoice[2]} \n 4. Exit \n Type number associated with option \n Type Number: ")

if int(userInput) >= 1 and int(userInput) <= 4:
    print("Option Selected")
    if int(userInput) == 1:
        print(f"User has selected: {subjectChoice[0]}")
    elif int(userInput) == 2:
        print(f"User has selected: {subjectChoice[1]}")
    elif int(userInput) == 3:
        print(f"User has selected: {subjectChoice[2]}")
    elif int(userInput) == 4:
        print(f"User has Terminated the program")
else:
    print("No option was selected")


    
#ToDo: Task 2
# Use if else to find item(a specific number) from a list
numList = [56, 78, 100, 45, 88, 71]

userInput = input(f"")
