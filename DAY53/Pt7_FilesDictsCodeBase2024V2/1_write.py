"" '' # Objectives

"" '' # Write to text files


"" '' # Notes:
"" '' # In order to read the data stored in a text file, you must open it first. 
"" '' # Just like a book. You cant read what is inside if you dont open it first.
"" '' # There are four modes for opening a file:
"" '' # r for only reading files
"" '' # w for only writing to file and creating the file if it does not exists but overwrites existing file contents
"" '' # a for adding to an existing file
"" '' # r+ for reading and writing files


"" '' # Key file-handling techniques are:Open, Read ,Close, Write
"" '' # The text file must be saved in the same location as your Python file for the program to work. 


"1_FileHandling_ReadWrite/myfile.txt","w"
"Syntax :  varName = openMethod('pathtofolder/parthtofile/fileName.txt', 'w')"
filePath1 = open('Day53/Pt7_FilesDictsCodeBase2024V2/file1.txt', 'w') # folder/folder/filename

# write to file
filePath1.write("Python Programming")

# close the filepath and file/ releasing the resource
filePath1.close()

"" '' #Task
"" '' # To Do: Refer to the example code above to create a file called yourName.txt and Write your name to the file" 
"" '' # If stuck refer to the example above
"" '' # Further reading"
"" '' # https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html



