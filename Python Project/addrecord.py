"Objectives"
"" '' # Import connect module
from connect import *

"" '' # Create a function to add record(s) to a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement


"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

# ceate a function to insert ecord in the songs table
def insert_record():
    try:
        dbCon, dbCursor = db_access()
        # fields/columns = SongID, Title, Artist, Genre
        # SongID field is auto increment, no data required

        # create variables to store the input for the respective fields
        song_title = input("Enter song title: ")
        song_artist = input("Enter song artist: ")
        song_genre = input("Enter song genre: ")

        
        # Create a sql insert statement to inset data from the rspective variables above
        dbCursor.execute("INSERT INTO songs (Title,Artist,Genre) VALUES(?,?,?)", (song_title, song_artist, song_genre))
        # Call/invoke the commit method to save the changes(record) permanently in the db table
        dbCon.commit()

        print(f"{song_title}  inserted in the songs table")
    except sql.OperationalError as oe:
        print(f"Failed because {oe}")
if __name__ == "__main__":
    insert_record()
