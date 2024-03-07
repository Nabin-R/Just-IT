"A subroutine(function) may or may not have a return statement"
"A subroutine(function) may or may not have parameters"

# create function use return statement without parameters and arguments
"To Do: Predict, then Run, and then Investigate"
def user():  # define the subroutine/function user
    name = "Emjay"
    return name
    

def userName():  # define the subroutine userName
    name = input("What is your name? ")
    return name
   


# create function use return statement with parameters and arguments
def addition(num1, num2):  # defines the addition function
    # variables inside a  surbroutine/function have local scope
    answer = num1 + num2
    return answer
    

# prevents the automatic running of the subroutine when it is imported
# in to another python file/application

"If this file is run directly it will automatically call and run the respective subroutines"
if __name__ == "__main__":
    # call/invoke the subroutine
    
    # call/invoke the subroutine

    username = userName()
    print(f"Method 2\nYour username is {username}")

    # call/invoke the functioneName
    "Method 1"
    result = addition(90,102)
    
    print(f"Method 2\nThe answer is {result}")

    "Method 2"
    num1 = 10#int(input("Enter your first number: "))
    num2 = 20#int(input("Enter your second number: "))

    # Assigned the function to the variable myAddition
    myAddition = addition(num1, num2)
    print(f"Method 2\nThe answer is {myAddition}")


    print(f"Your answer to {num1} + {num2} is {myAddition}")

    "To Do: Task1: Modify the code in userName function below to use parameter and arguments"

def userName(f, a, i):  # define a subrouitine called userName
    print(f"my name is {f}, my address is {a} and my interest is {i}")


fullName = input("Enter your name: ")
address = input("Enter your address: ")
interest = input("Any interest? ")

userName(fullName, address, interest)

"""
To Do Task 2: Modify the code in subroutine to convert it to a function thats uses parameters and arguments with a return statement
"""
def sub(n1,n2):  # define the subtraction function
    # variables inside a  surbroutine/function have local scope
    answer = n1 - n2
    return answer


num1 = int(input(("Enter your first number: ")))
num2 = int(input(("Enter your second number: "))) 

ans = sub(num1,num2)

print(f"he answer to {num1} - {num2} is {ans}")   

"Variable Scope "

# The scope of a variable is the section of the program where the variable can be accessed and modified.
# A variable declared in the main part of the program can be accessed globally by all subroutines. 
# It cannot be modified unless you explicitly state that the program should modify the global variable. 

"Global scope and Local scope"
# Variables can either have global scope or local scope. 

"Global scope"
# Global scope refers to a variable that can be accessed and modified from anywhere in the program, even from inside subroutines. 


"Local scope"
# Local scope refers to variables that can only be accessed and modified within the code block that they were declared.  


"Handling Variable Scope"
# Not all programming languages handle scope in the same way Python has been designed to discourage the modification 
# of global variables, you’ll find out why during this lesson.
# Variables are local unless otherwise declared. 


"To Do: Predict, then Run, and then Investigate"

"Global variable"
# This variable has a global scope
globalNum = 5

# The subroutine localSubRoutine () is accessing the globalNum variable and displaying it as output. 
def localSubRoutine():
    # Access the globalNum variable declared outside of this subroutine
    print(f"Printed globalNum variable {globalNum}from outside of local subroutine\n")
    localNum = 10  # local variable that is declared inside localSubroutine
    print(f"Printed localNum variable {localNum} from local subroutine\n")


localSubRoutine()  # call subroutine
print(f"Printed globalNum variable {globalNum}from global\n")

# Use the link below for required further reading
# https://www.programiz.com/python-programming/global-keyword

"To Do: Task 1: "
"Uncomment the line of code with the print function below and then run the file only after you run and understand the code block above"
"The code below will attempt to access locaNum from loacalsubroutine"
#print(f"attempt to access locaNum from loacalsubroutine {localNum} \n")

"Can you explain the output from the terminal when you run the print statement above?"
#it will pass an error since u cannot get localnum till it has become a variable, it can only be accessed locally by the function not globally.
# to fix this u will have to either use a return value to fix it into a global variable

