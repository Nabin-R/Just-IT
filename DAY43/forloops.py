
# for i in range(20):
#     print(i+1)

#     name = 'Nabin'

# for i in name:
#     print(i)

# num = 4
# numguess = int(input("Guess a number between 1 - 10: "))

# while numguess != num:
#     numguess = int(input("Incorrect \nGuess again: "))
# print("Correct")

# ---

# for variableName in rangeObject(numberOfIteration)
# for loops that use the range() function
# range() is the sequence that you are going to iterate through
# range() is a built-in function just like input(). 


# range(stop) -> range object range(start, stop[, step]) -> range object
# When you call the range function, you can pass it up to three values: 
# The start number
# The end number
# The step 

"To Do: Predict, then Run, and then Investigate"

"start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3"
for findNum in range(10):
    print(findNum)

"Modify/Make"
"Task 2: Create a program that uses a for loop to start count from 1 to and ends at 20 "

for i in range(1, 20):
    print(i)

"Task 3: Create a program that uses a for loop to start count  from 0, and increment(step) of 5 a and ends/stop at 30"
for i in range(0,31,5):
    print(i)

"Task 4:  Modify the code you produced in task 3 to count down in steps of 5 (from a high number(30) to a low number greater or equal to 1)"

for i in range(31,0, -5):
    print(i)


"Further reading on python for statements"
# https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#for-statements

"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""


num = 1
maxnum = 50

while num != maxnum:
    num += 1
    print(num)

"To Do: Explain what is += 1  ?"
# A = A + 1 shortened

"Modify/Make"
"To Do: Task 2: Modify the whileloop above to count down from 20 to 1 and comment your code"

num = 20 # set num to 20

while num != 1: # while num is not 1
    num -= 1 #subtract if not 1 yet
    print(num)
print("number = 1")

# --

"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""

import math
import random

"To Do: Predict, then Run, and then Investigate"

num = 1  # int(input("Enter a number: "))
userNum = random.randint(1,20)
# while 1 <= 20

while num <= 20:  # start from 1 and keep looping to 20(condition is met)
    print(f"The number is {num}")
    if num == userNum:  # check if the value in userNum is the same as the value in num
        print(f"Exited loop - Found Random number: {userNum}")
        break  # break/exit the loop
    num += 1  

"Modify/Make"
"To Do: Task1: modify the userNum variable to use a randomly generated number between 1 - 20"
"Further reading on python while statements"




# https://www.w3schools.com/python/ref_keyword_while.asp
# https://www.w3schools.com/python/python_ref_keywords.asp
# https://www.w3schools.com/python/python_reference.asp

