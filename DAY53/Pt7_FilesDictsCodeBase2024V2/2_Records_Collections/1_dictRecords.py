"" '' # Objectives
"" '' # Understand the difference between keys and value
"" '' # Understand what is a record(database)
"" '' # Use keys and values to create a dictionary data structure

"" '' # Notes:

"" '' # Read data structures and record for 2 minutes
"" '' # Data structures are used to store data in an organised and accessible way. 
"" '' # A list is a data structure.  Another example of a data structure is a record.  
"" '' # You might have heard of the word record if you have ever created a database before. 

"" '' # A record allows you to store a collection of attributes for a single entity.
"" '' # Data structure: record: An entity can be any object, place, person, or thing. 
"" '' # Attributes are properties or characteristics of that entity.  
"" '' # Attributes are sometimes referred to as fields. 




"To Do: Predict, then Run, and then Investigate"
# create a dictionary 

dict1 = {"FName": "Nabin", "Address": "London", "Age": 23, "Interest": "Coding"}
print(dict1)

"Using dictionary methods"

# D.items() -> a set-like object providing a view on D's items
print(dict1.items())
 
# D.keys() -> a set-like object providing a view on D's keys
dKeys = dict1.keys()
print(dKeys)
 
# D.values() -> an object providing a view on D's values
dVals = dict1.keys()
print(dVals)

# create a second dictinary
dict2 = {2:"Python", 3:"HTML", 4:"CSS"}

# update dictionary 1 with the key values in dictionary 2
dict1.update(dict2)

for aKey, aValue in dict1.items():
    print(f"Key: {aKey} | Value: {aValue}")

# remove specified key and return the corresponding value
dict1.pop("fName")
dict1.pop(3)

print(dict2)
print(dict1)

# removes the last key value pair from the dictionary
dict2.popitem()
print(dict2)