"""Nested selection/nesting is when a selection block(if/else)
is placed within another if,  else selection block"""

"Modify"
"To Do: Task 1: Using if elif and else"
# Exercise: Use the notes/comments after the variable initialisation to create a nested if statement that will:

# 1. Check 'userAge' against the 'ageLimit

# 1.1 When the 'userAge' is not greater that the 'ageLimit then display a suitable message

# 2. When the 'userAge' is greater than the 'ageLimit' then execute another code block( that asks user to provide a code, see 2.1 below)

# 2.1 create a variable called 'userCode' to ask for user input and compare the value provided(userCode) with the value held in passCode

# 3. When the 'userCode' is not the same as 'passCode' display a suitable message

# 3.1 When the 'userCode' is the same as 'passCode' display a suitable message


userAge = int(input("Enter your age: "))

ageLimit = 16

passCode = "Bootcamp"

if userAge >= ageLimit:
    print("Age Validated")
    userInput = input("Enter passcode: ")
    if userInput == passCode:
        print("User Verified")
    else:
        print("Passcode incorrect")
else:
    print("Underaged")

# compare if the value held in userAge is greater than the value held in ageLimit


# execute the code block below if the comparison returns true


# nested if will execute if the codition above is true (if userAge > ageLimit:)

 # This else will execute if nested if condition above is false (userCode is not equal to passCode:)

# This else will execute if the if condition above is false ( userAge is less than the ageLimit:)

"To Do: Q&A"
"What do you think is the equivalent of JS nested if in python?"

# if statements inside if statements

"""Nested selection/nesting is when a selection block(if/else) is placed within another if, 
 else selection block"""


"""Nested selection/nesting is when a selection block(if/else) is placed within another if, 
 else selection block"""



"To Do: Predict, then Run, and then Investigate and then comment the code to explain each line of code does"

pyCourse = float(input("Enter your Python score: "))
htmlCourse = float(input("Enter your HTML score: "))
sqlCourse = float(input("Enter your SQL score: "))

if pyCourse < 45: #checks if value is less than 45 (44 or lower)
    print(f"Try again in python {pyCourse}") #prints failuire - ends code
elif htmlCourse < 45: #checks if value is less than 45 (44 or lower)
    print(f"Try again in HTML {htmlCourse}") #prints failuire - ends code
elif sqlCourse < 45: #checks if value is less than 45 (44 or lower)
    print(f"Try again in SQL {sqlCourse}") #prints failuire - ends code
else:
    gradesAverage = (pyCourse + htmlCourse + sqlCourse)/ 3 #checks sum of values given earlier, then divided by 3 for average result.
    if gradesAverage <= 55:
         print(f" Your average score is {gradesAverage} and is Grade C ")  #55+ total = A
    if gradesAverage <= 79:
         print(f" Your average score is {gradesAverage} and is Grade B") #79+ total = B
    if gradesAverage <= 89:
         print(f" Your average score is {gradesAverage} and is Grade A ") #89+ total = A



num1 = 106
num2 = 25
num3 = 27
print(f"\nWhen num1 = {num1} num2 = {num2} num3 = {num3}")
if num1 > num2:
    if num2 > num3:
        print("num1 is greater than num2 and num2 is greater than num3")
    else:
        print("num1 is greater than num2 and num2 less than num3")
elif num1 == num2:
    print("num1 is equal to num2")
else:
    print("num1 is less than num2")


num1 = 106
num2 = 28
num3 = 27
print(f"\nWhen num1 = {num1} num2 = {num2} num3 = {num3}")
if num1 > num2:
    if num2 > num3:
        print("num1 is greater than num2 and num2 is greater than num3")
    else:
        print("num1 is greater than num2 and num2 less than num3")
elif num1 == num2:
    print("num1 is equal to num2")
else:
    print("num1 is less than num2")


num1 = 1
num2 = 1
num3 = 27
print(f"\nWhen num1 = {num1} num2 = {num2} num3 = {num3}")
if num1 > num2:
    if num2 > num3:
        print("num1 is greater than num2 and num2 is greater than num3")
    else:
        print("num1 is greater than num2 and num2 less than num3")
elif num1 == num2:
    print("num1 is equal to num2")
else:
    print("num1 is less than num2")

num1 = 1
num2 = 1
num3 = 27
print(f"\nWhen num1 = {num1} num2 = {num2} num3 = {num3}")
if num1 > num2:
    if num2 > num3:
        print("num1 is greater than num2 and num2 is greater than num3")
    else: 
        print("num1 is greater than num2 and num2 less than num3")
elif num1 == num2:
    if num2 < num3:
        print("num1 is equal to num2 and num2 is less than num3")
else:
    print("num1 is less than num2")

"Use the link provided below to investigate Tenary Operators in python"
# https://www.w3docs.com/snippets/python/how-to-write-inline-if-statement-for-print.html

"Make"
"To Do: Use any two of your existing 'if else' and or 'if,elif and else' programs"
#1. Create/modify existing program using the Tenary Operators syntax
#2. From your investigation and implementation of Tenary Operators program explain:
# -(a) any use case for using or not using Tenary Operators
# use case to make situations have different states depending on other variables 
# -(b) any limitiation(s) for using or not Tenary Operators

Health = 400
EnemyAttack = 550

isAlive = "State: Alive" if EnemyAttack < Health else "State: Dead"

print(isAlive)