# -- Arithmetics
"Arithmetic expression evaluates to a number"

num1 = 10  # static object/value
num2 = 5  # static object/value
num3 = 11  # static object/value
num4 = 2  # static object/value

# + operator is use for adddition and also concatenation(join things)

print("Addition: " + str(num1) + " + " + str(num2) + " =", num1 + num2)

# Using f-strings to format print statement (f followed by quotes)
# strings cater for all data types

# plus operator +
print(f"Using f-strings\nAddition: {num1} + {num2} = { num1 + num2} ")

"To Do: Task 1: What is the equivalent of f-strings in JavaScript?"
# f string are equivelent to using `` quotations

"Review the code below to answer the following questions"
"Task 1: Explain in your own words the operators listed below "
# Division (/) # Divides the first value by the second value
# Floor Division (//) 10 / 3 = 3 # divide and then round down to the nearset whole value(integer)
# Modulus (%) Getting remainder from divided value

"To Do: Explain in your own words when you would use the operators listed above"

# You would use operators to get values from stored variables or any math-related code.

# division /
print(f"Division (/): {num3} / {num4}  = {num3 / num4}")

# Floor division
print(f"Floor division (//): {num3} / {num4}  = {num3 // num4}")

# Modulus %
print(f"Modulus (%): {num3} / {num4}  = {num3 % num4}")

# -- Comparison
"Read through the Comparison operators examples and reference or use it as a guide during lesson"
"To DO: For further reading and independent learning refer to the link below"
#https://www.w3schools.com/python/gloss_python_comparison_operators.asp



"Comparison operator compare values/object"

# ==    equal  ( 2 == 2)
# < 	less than
# > 	more than
# <= 	less than or equal to
# >= 	greater than or equal to
# !=    Not equal to

# -- Logical

"Read through the Logical operators examples and reference or use it as a guide during lesson"
"To DO: For further reading and independent learning refer to the link below"
#https://www.w3schools.com/python/gloss_python_comparison_operators.asp

"Logical expression evaluates to True or False"
# Logical operators: and , or, not

# ==    equal  ( 2 == 2)
# < 	less than
# > 	more than
# <= 	less than or equal to
# >= 	greater than or equal to
# !=    Not equal to

num1 = 10  # static object/value
num2 = 5  # static object/value
num3 = 11  # static object/value
num4 = 2  # static object/value
# comparison operator
print(num1 == num2)
print(num1 == 10)
print(num2 == 5)


"Task 1: Predict, then Run, then Investigate, and then add comments"

# Logical operator: and
print("Logical operator: and")

print(num1 == 10 and num2 == 5)
print(num1 == 10 and num2 == 50)
print(num1 == 15 and num2 == 5)

# Logical operator: or
print("Logical operator: or")
print(num1 == 10 or num2 == 5)
print(num1 == 10 or num2 == 50)
print(num1 == 15 or num2 == 5)


# Logical operator:not
print("Logical operator: not")
print(not (num1 == 10))

# Logical operator:not
print("Logical operator: not with or")
print(not (num1 == 10 or num2 == 5))
print(not (num1 == 10 or num2 == 50))
print(not (num1 == 15 or num2 == 5))


# Logical operator:not
print("Logical operator: not with and")
print(not (num1 == 10 and num2 == 5))
print(not (num1 == 10 and num2 == 50))
print(not (num1 == 15 and num2 == 5))


# -- Assignment

"Read through the assignment operations examples and reference or use it as a guide during lesson"
"To DO: For further reading and independent learning refer to the link below"
#https://www.w3schools.com/python/gloss_python_assignment_operators.asp


""" assigned same value to multiple variables"""
num1=num2=num3=10
print(num1,num2,num3)

"""use of  compound assignment a+=b """
num4,num5=10,5
#print(num4 -5," + ",num5 , "=", num4)
num4+=num5# #compound assignment
print("Addition",num4)

num4,num5=10,5
num4-=num5# #compound assignment
print("Subtraction",num4)

num4,num5=10,5
num4*=num5# #compound assignment
print("Multiplication",num4)

num4,num5=10,5
num4/=num5# #compound assignment
print("Division",num4)

num4,num5=10,5
num4%=num5# #compound assignment
print("Modulus",num4)

num4,num5=10,5
num4**=num5# #compound assignment
print("Power",num4)


num4,num5=10,5
num4//=num5# #compound assignment
print("Floor Division",num4)