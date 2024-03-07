"To Do: Predict, then Run, and then Investigate"
def math():
    # name is a global variable 
    # answer, num1 and num2 are local variables 
    userinp = int(input("Select one: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \nPlease type a number: ")) #Select a choice to do
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    if userinp == 1: #if elif statement for prints and result
        answer = num1 + num2
        print(f"The answer to {num1} + {num2} = {answer}")
    elif userinp == 2:
        answer = num1 - num2
        print(f"The answer to {num1} - {num2} = {answer}")
    elif userinp == 3:
        answer = num1 * num2
        print(f"The answer to {num1} * {num2} = {answer}")
    elif userinp == 4:
        answer = num1 / num2
        print(f"The answer to {num1} / {num2} = {answer}")

"Make"
"To Do:Task1: Modify the code above to use either subtraction or multiplication or division and change the subroutine name respectively"
"To Do:Task2: Add comments to the explain your lines of code"

# prevents the automatic running of the subroutine when it is imported
# in to another python file/application
"If this file is run directly it will automatically call and run the respective subroutines"
#if __name__ == "__main__":
    #math()



"Further reading on python functions"
# 

"To Do: Predict, then Run, and then Investigate"



"Modify"
"To Do: Task3: Modify the code below to use a parameter"


def user(para):
    print(f"Hello, {para}")



def userName():  # define the subroutine userName
    # function body(code to execute when the subroutine/function is called)
    name = input("What is your name? ")
    return name



# prevents the automatic running of the subroutine when it is imported
# in to another python file/application
"If this file is run directly it will automatically call and run the respective subroutines"
"To Do: Task4: Modify the code below to use an argument when you call/invoke it"
if __name__ == "__main__":
    returnValue = userName()
    print(f"Your name is {returnValue}")
    user(returnValue)

    # Import functions 
#from sub1 import user

print("Welcome to our Subroutine program")

# call/invoke subroutines from another file

"To Do: Predict, then Run, and then Investigate"

"To Do: Task1: Call and invoke the:"
returnValue = userName()
"Further reading on python functions"
# 