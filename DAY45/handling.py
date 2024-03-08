"List methods"
"""You can think of list methods as special functions that are applied to lists. 
To call a list method, you need to use dot notation (as in the examples that follow).  """
"Method" '' # A function that belongs to an object.
    #  Use list methods to:"
    #  list.append(item)"        # add item at end of list
    #  list.insert(index,item)   "  # add item at index
    #  list.pop(index)"       # remove item at index
    #  list.remove(item)   "  # remove item
    #  list.index(item)   "  # search for index of item
    #  list.count(item)"  # get occurrences of item
    #  list.reverse()"   # reverse list
    #  list.sort()"      # sort list


"Method"  # A function that belongs to an object.
"Custom  built function"  # A function that you have created yourself and imported into other programs that you have created.
"List"  # A dynamic data structure that holds items under one name. The items can be of varying data types.


"Traverse" ''  # Move through a sequence.
"You can use a for loop to traverse a list of elements"
#              0         1         2        3          4      5       6
trainers =  ["Abdul", "Christian","Narayan","Richie","Tim", "Waqas", "Zak"]
for trainer in trainers:
    if trainer == "Tim":
        print("Python")
    else:
        print("HTML")
"To Do: Task 1: Predict, run and investigate the code above"
# HTML, HTML, HTML, HTML, PYTHON, HTML, HTML

"To Do: Task 2: "
"" '' # Your task is to traverse through the variable 'course' provided below using a for loop and you are not required to search for a specific element
course = "Python Programming"

"Objective "
"" '' # List methods: Recap

"To Do: Task 3: "
"Use any two list method from above to perform operation on the list, listOfNames"


"To Do: Task 4: Predict, run and investigate the code above"
#                  0         1         2        3         4        6       7
listOfNames = ["Nicole", "Laura", "Silvia", "Steve", "Juliet", "Laura", "Silvia"]
print(listOfNames)  # Prints the list
print(listOfNames[2])  # Prints Silvia
listOfNames.sort()
listOfNames.append("Jake")

"What is the len() used for in the code below?"
for index in range(len(listOfNames)):
    print(f"{index} : {listOfNames[index]}")

print(f"\n{listOfNames}")
# What item is returned from the list and why?
print(f"{listOfNames[3]}\n")


# Note 
"" '' # Refer to https://www.w3docs.com/learn-python/python-lists.html if you find on any of the tasks  

"Objective:"
"" '' # Use chr() and ord() to perform ASCII conversion
# Perform ASCII conversion in pyhon
# chr(97): takes in a decimal number and returns its character equivalent
# ord("a"): takes in a character and returns its character decimal equivalent

"To Do: Task 1:  Predict, then Run, and then Investigate the use of ord() function in python"
aChar = input("Enter a character: ")
# ord("a"): takes in a character: Return the Unicode code point for a one-character string.
convertChar = ord(aChar)  # ord"(a/b/c/d")
print(convertChar)

"To Do: Task2: Modify the code above to ask for an integer value then use the chr() to return its character equivalent"
"solution"



"Objective:"
"" '' # Create a function that returns a list
"" ''   # ~ Use randomisation to append items to a list
"" ''   # ~ Use the in operator and range function to generate a range of number to be added to a list.

"""To Do: Task 3: Complete the code block below to print a list of converted numbers as letter
 The question marks indicates where the code is missing """
 
"Extension: Uncomment the code to complete th task"
"""
def alphabets(): # created the function alphabets
    alphabetList = ? # create an empty list
    for ? in range(65, 123):
        alphabetList.append(chr(letters))  # converts numbers to letters then add/append them to
    return ?
print(?)
"""
"objective"
"Create multidimentional list" '' # 2D lists
"" '' # Define a 2D list
"" '' # Use a 2D list in a program
"" '' # Access items from a 2D list

# A list is used to hold multiple elements under one name. 
# A two-dimensional list allows you to hold a list as one element. 
# Data in a 2D list can be held in rows and columns. 

bootcamp = [
    
# 0           1          2           3       4         5      6
["Abdul", "Christian", "Narayan", "Richie", "Tim", "Waqas", "Zak"], #0

["SDLC", "HTML", "CSS", "JavaScript", "Database", "Python", "Project Week"]#1

]

"To Do: Task 5: Predict, run, investigate and add comment to explain all the print statements below"
print(bootcamp)
print(bootcamp[0])
print(bootcamp[1])
print(bootcamp[0][1])
print(bootcamp[0][1:4])

