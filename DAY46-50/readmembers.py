from connect import *
def read_all_members():
    try:
       dbCon, dbCursor = db_access()
 
       # all_songs = dbCursor.execute("SELECT * FROM songs").fetchall()
       # run the the dbCursor.execute() to select all records in the songs table
       dbCursor.execute("SELECT * FROM members")
 
       #fetched all selected records using the fetchall method and assigned it to the all_songs variable
       all_members = dbCursor.fetchall()
 
       if all_members:
           print("*" * 100)
           #fortmat output SongID, Title, Artist, Genre
           print(f"MemberID{'':<3}|Firstname{'':<25}|Lname{'':<24}|Email{'':10} ")
           print("*" * 100)
 
           for aSong in all_members:
               "0     1        2       3"
               #1   Test    Tester  Testing
               print(f"{aSong[0]:<9}|{aSong[1]:<30}|{aSong[2]:<30}|{aSong[3]:<10}")
               print("-" * 100)
       else:
           print("No songs found in the songs table")
    except  sql.OperationalError as oe:
        print(f"Failed to read because: {oe}")
 
if __name__ == "__main__":
    read_all_members()