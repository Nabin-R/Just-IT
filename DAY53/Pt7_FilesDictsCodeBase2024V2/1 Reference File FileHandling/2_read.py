"" '' # Objectives
"" '' # Use the r to read from a file

"" '' # Notes
"" '' # There are four modes for opening a file
"" '' # w for only writing to file and creating the file if it does not exists but overwrites existing file contents
"" '' # a for adding to an existing file
"" '' # r for reading and writing files



"To Do: Task 2:Modify the code below to:"
"" '' # Read the contents of your file (yourName.txt) by replacing the:
"" '' # 1. "w" mode after the file path with the "r"
"" '' # 2. the write() method with the read method()
"" '' # 3. Unlike the write mode, no argument is required within the parenthesis of the read mode.

"Syntax :  varName = openMethod('pathtofolder/parthtofile//fileName.txt', 'w')"
filePath1 = open('Day53/Pt7_FilesDictsCodeBase2024V2/file2.txt', 'r') # folder/folder/filename
fr = filePath1.read()

print(fr)
filePath1.close()


"Further reading"
# https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html

