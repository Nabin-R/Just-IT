
"Objective"
"" '' # Describe the function of string operations
"""You can perform operations with string in a similar way to the operations 
that you can perform with numbers. """

"To Do: Predict, then Run, and then Investigate"

"Objective"
"" '' # String handling techniques
stringVal1 = "a" > "b" # check if the letter a is greater than b
print(stringVal1)


stringVal2 = "b" > "a"  # check if the letter b is greater than a
print(stringVal2)

"Task 1 Working with comparison operators" # != , == , <= , >=, <,>
#  use any comparison operator to compare the letter "a" and "A"
#  use any comparison operator to compare the letters "ax" and "ZZ"
#  use any comparison operator to compare your firstname with any another first name

stringVal1 = "a" > "A" 
print("1. ", stringVal1)
stringVal1 = "B" > "a" 
print("2. ", stringVal1)
stringVal1 = "ax" > "az" 
print("3. ", stringVal1)
stringVal1 = "ax" > "ZZ" 
print("4. ", stringVal1)

"You can multiply a string, it will concatenate the same value for the number of times stated."
mutiplyWord = "Python\n" * 2  # mulitply the word n times
print(mutiplyWord)

"""The + sign concatenates (joins) the two string together.
There is no space because it hasn't been given that instruction"""
joinWords = "Python" + "Java"  # join the two words
print(joinWords)

"Task 2"
# Create two variables fName and lName and join and print them using a variable called fullName

"Objective"
"" '' # Finding the length of a string len()

"Knowledge Check: What is the len() used for in a string?"
# finding the length of a string

course = "Python"
wordLength = len(course)
print(wordLength)

"Objective"
"" '' # Finding a character using indexing e.g. course[0]

"Task 3: How can we print a specific character using the index value or position in a string or list?"
findChar = course[2]
print(findChar)

"Objective"
"" '' # Make/modify a program that uses string-handling techniques

"Task 4: Write the code to print the letter  h"
findChar = course[-3]
print(findChar)

"Hints"
course = "Python Programming"
wordLength = len(course)
print(f"The length of the string {course} is {wordLength}")

"Objective"

"" '' #Extension activity: Research and independent learning activity
"Task 1: Return all the characters from the string held in the course variable using negative values"
"Task 2: Research and independent learning activity"
# Open the Python documentation using the provided link to discover uses of :
str.capitalize()
str.title()
str.swapcase()
# https://docs.python.org/3.3/library/stdtypes.html?highlight=substring#string-methods

"The for loop can be used to iterate through a string and any sequence of elements(eg numbers etc)"

"Objective"
"" '' # Using a for loop to iterate over a string
"To Do: Predict, then Run, and then Investigate"
name = "Abdul is Software Technical Trainer"
for letter in name:
    print(letter)

"Objectives"
"" '' # Use a substring in a program
"" '' # Use the in operator to check for a substring

searchStr = "Python is a great programming language"
findChar = input("Enter character to search for: ")
# print(searchStr[3])
"""The membership operator can be used to check if a value/substring is present
or not in object and returns true if it does"""
if findChar in searchStr:  # opposite of the in operator is the 'not in'
    print(f"Found {findChar}")
else:
    print(f"Not Found {findChar}")

"Task 5: Replace the in operator above with the 'not in' operator, run the code then explore the output in the terminal "


# Further reading on operators not covered in the bootcamp see links below
"https://www.w3schools.com/python/gloss_python_identity_operators.asp"
"https://www.w3schools.com/python/gloss_python_bitwise_operators.asp"


"To Do: Task 6: use if and 'in' operator to find a character in your name"

name = "Add your full name here"  # Add your name in between the speech marks 


"Extension and research of using for loop and if statement "

# You have been provided with the vowels in a list data structure and a variable
# name that is assigned with an empty string.


"Your task is to assign your name to the variable called name and use a for loop and if statement to:"
"Iterate through the list of vowels to find the vowels in your name"
"          0,   1  ,   2,  3,  4"
vowels = ["a", "e", "i", "o", "u", "j"]  # vowels
name = "Add your full name here"  # Add your name in between the speech marks 


