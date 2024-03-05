import random 
import math # import (module) math

"Modify "
"You have been provided with an incomplete diceRoll.py program with bugs "
"To Do: Task 1: Review, debug and fix the code below, by repacing the '?s' with the code syntax "

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print(f"Dice: {dice1} | Dice: {dice2}")

dice = dice1 + dice2  # What i the values of both dice

if dice == 12:  # check if both dice equals 12
    dice = dice * 2  # double the total from both dice
    print(f"You threw {dice}")
else:
    if dice1 == dice2:
        dice = dice * 2 # 10 = 20
        print(f"You threw {dice}")
    else:
        print(f"You threw {dice}")
print(f"You threw a total {dice}")



"To Do: Task 2: Add notes below to explain the application in your own words"

"""
dice 1 & 2 will find a random integer between 1 and 6
dice will be the sum of dice 1 and dice 2
if dice sum of both dices is equal to 12 it will double the dices and give 24
else the check will continue to see if u get same values for both dice 1 and 2 and times them by 2
if nothing matches then itll not mutliply by 2

"""

# This module provides access to the mathematical functions defined by the C standard

radius = float(input("Enter radius: "))
area = math.pi * radius ** 2

"Predict, then Run, and then Investigate"

print(f"The area is {area}")

# Method 1
# Round (round) a number to a given precision in decimal digits.
print(f"The area displayed is rounded to 2 decimal places {round(area, 2)}")

# Method 2
print(f"The area displayed is rounded to 2 decimal places {area:.2f}")
   

""" Debug the code by replacing the questions marks with the correct variables and/or methods Where applicable. """

"Modify"
"To Do: Task 1: Use the floor method to round down to the nearest whole number"
# Method 3
roundDown = math.floor(area)
print(f"The area displayed is rounded down to whole number {roundDown}")


# Method 4
"To Do: Task 2: Use the ceil method to round up to the nearest whole number"
roundUp  = math.ceil(area)
print(f"The area displayed is rounded up to a whole number {roundUp}")



"To Do: Knowledge Check: Why use the 'dir(math)' in the print below?"
print(f"\n{dir(math)}")

# Prints out all the properties and method on the module.