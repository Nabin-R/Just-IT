"Objectives"
"" '' # Import connect module
"" '' # Create a function to delete record(s) in a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement

"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

from connect import *
 
def delete_member():
    try:
        dbCon, dbCursor = db_access()
 
        # check if SongID exists
        member_id = int(input("Enter the MemberID to delete a record: "))
        dbCursor.execute("SELECT * FROM members WHERE MemberID = ?", (member_id,))
 
        # invoke the fetchone method and assign it to a variable called row
        row = dbCursor.fetchone()
 
        if row == None:# None is a singleton object that check if a value exist
            print(f"No record with {member_id} exists! ")
       
        else: # if there is a match with the song_id provide
            dbCursor.execute("DELETE FROM members WHERE MemberID = ?", (member_id,))
            dbCon.commit()
 
            print(f"The record with the MemberID {member_id}  deleted!! ")
    except sql.OperationalError as oe:
        print(f"Failed to delete because: {oe}")
if __name__ == "__main__":
    delete_member()