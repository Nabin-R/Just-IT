fname    = input("Enter you full name: ")
address   = input("Enter your address: ")
interest = input("Enter your interest: ")
age      =    int(input("Enter your age: "))

"Make"
"To Do: Task 1: Use the code above to ask for user input and then save it to a file called userDetails.txt"

with open(r"Day53/Pt7_FilesDictsCodeBase2024V2/userDetails.txt", 'r') as fp:
    x = len(fp.readlines())

with open('Day53/Pt7_FilesDictsCodeBase2024V2/userDetails.txt',"a") as filePath1:
    contents =f"User {x} [First Name: {fname}, Address: {address}, Interest: {interest}, Age: {age}] \n"
    filePath1.write(contents) #write to file 


"Further reading"
# https://www.w3schools.com/python/python_file_handling.asp