"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""



# import the datetime library/class/module
import datetime
import time

"To Do: Predict, then Run, and then Investigate"



print("None while Loop output")
dateTime = datetime.datetime.now()
print(dateTime.strftime("%H:%M:%S"))


"To Do: Task 1" 
" study the output of the code above and the output in in the while loop below, and use the links provide to answer"

" What is the while loop doing?"
# the while loop is constantly variable called dateTime, the dateTime is being used as a variable for the current time 
" add comment to explain what you understand the 'datetime.datetime.now().strftime('%H:%M:%S')'"
# it will output the time in Hours:Minute:Seconds string formate from the time
" add comment to explain what you understand the 'end='"
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
# end is used to concatenate and put a statement at the end of the function

" add comment to explain what you understand the '\r' "
# https://www.w3schools.com/python/gloss_python_escape_characters.asp
# returns carriage - back to the start

" add comment to explain what you understand the 'end=' is used for"
" add comment to explain what you understand the '\r' is used for "
# end is used here to put/add a function to the end of the statement in this case it would be R to replace the print from the start

" What will output if you remove  , end='\r'  from the while loop"
# it will constantly update every tick in a new line.

print("while Loop output")
count = 0
while True:
    print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
    time.sleep(1) 
    count += 1
    if count == 3:
        break

"Further reading on python while statements"
# https://www.w3schools.com/python/ref_keyword_while.asp
# https://www.w3schools.com/python/python_ref_keywords.asp
# https://www.w3schools.com/python/python_reference.asp

"""
Break in Python Python break is generally used to terminate a loop. 
This means whenever the interpreter encounters the break keyword, 
it simply exits out of the loop. Once it breaks out of the loop, 
the control shifts to the immediate next statement.
"""


"To Do: Predict, then Run, and then Investigate"

#Combining iteration and Selection"

numList = [1, 3, 4, 6, 1, 3, 5, 7]

found = False
for number in numList:
    if number == 3:
        print("Found", number)
        found = True
        break
    else:
        print(f"Number {number} not found")

if not found:
    print("Number 3 not found in the list") 

#  uses a boolean variable found to keep track of whether the number 
# 3 has been found in the list. If the number 3 is found, the found 
# variable is set to True and the loop is exited with the break statement.
#  If the loop completes without finding the number 3, the code checks 
#  the value of found and prints a message indicating that the number was not found.

"Modify/Make"
"To Do: Task 1: Write a for loop similar to the one above to break out of the loop when 'Python' is found"
#Refer to the code above to guide you in completing this task

codeList = ['Java', 'Lua', 'HTML', 'Javascript', 'CSS', 'Python', 'PHP', 'C++']
check = False

for number in codeList:
    if check == False:
        print(f"Checking {number}")
        if number == 'Python':
            check = True
    elif check == True:
        print('Python Found')
        break

# attempted to use check as the if statement as it seems more practical
    
"To Do: Predict, then Run, and then Investigate "

countries = ["Scotland", "Spain", "England", "Wales", "Brazil", "Argentina", "Italy","France"]


print("Printed all countries in the terminal")
for country in range(len(countries)):
     print(f"{countries[country]}")


print("\nNot all countries are printed in terminal")
for country in range(5):
    print(f"{countries[country]}")

"To Do: Task 1: Explain why the first loop printed all the countries and the second for loop did not"
# first one finds the length of the list and runs it in for loop, while second one finds the first 5
"Modify"
"To Do: Task 2: Modify the number in the second for loop range function from '5' to any other number and explain the output"