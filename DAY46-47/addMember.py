from connect import *

def insert_member():
    try:
        dbCon, dbCursor = db_access()
        # fields/columns = SongID, Title, Artist, Genre
        # SongID field is auto increment, no data required
 
        # create variables to store the input for the respective fields
        member_fname = input("Enter first name: ")
        member_lname = input("Enter last name: ")
        member_email = input("Enter email: ")
 
       
        # Create a sql insert statement to inset data from the rspective variables above
        dbCursor.execute("INSERT INTO members (firstname,lastname,email) VALUES(?,?,?)", (member_fname, member_lname, member_email))
        # Call/invoke the commit method to save the changes(record) permanently in the db table
        dbCon.commit()
 
        print(f"{member_fname}  inserted in the member table")
    except sql.OperationalError as oe:
        print(f"Failed because {oe}")
if __name__ == "__main__":
    insert_member()