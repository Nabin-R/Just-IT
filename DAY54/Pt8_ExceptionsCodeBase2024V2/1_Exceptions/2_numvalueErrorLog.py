import logging
import logging

"" ''  # objectives
" " '' # To configure and log to a file the respective error messages.
" " '' # Use different logging methods with their severity level(s)
"" ''  # Use try and except to log Errors and Exceptions in a file




" " '' # To Do: Predict, then Run, and then Investigate
" " '' # different logging methods and severity
" " '' # logging.basicConfig(filename=r"folderpath/filename", level=logging.DEBUG) 

try:  # attempt to run the indented code block
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 / num2
    #Output for user/what the user see
    print(answer)
    #Output for developer/what the developer see
    logging.info(f"Divided {num1} / {num2} = {answer}")
       
except ZeroDivisionError:  # handles exception if code in try block fails
    #Output for user/what the user see
    print("You can't divide a number by zero")
    #Output for developer/what the developer see
    logging.warning("User attempted to divide by zero")
   
finally:
    print("Closing....")


" " '' #To Do: Task 1: Modify
" " '' #1. Use any one of the logging methods to log error to the Exceptions folder in a file called myFilelog1.log 
