import sqlite3
from database_handling import insertDB
conn = sqlite3.connect('test.db')
c = conn.cursor()

try:
    c.execute('''CREATE TABLE rooms(
     Room_Number INT PRIMARY KEY,
     Guest_Name TEXT,
     Check_In_Date BLOB,
     Check_Out BLOB,
     Guest_ID INT,
     State INT,
     PRICE INT
     )''')
    print('TABLE ROOMS CREATED')
except:
    print('TABLE ALREADY EXIST')




try:
    c.execute('''CREATE TABLE reservation(
         Reservation_Number INT PRIMARY KEY,
         Room_Number INT,
         Guest_Name BLOB,
         Check_In_Date BLOB,
         Check_Out BLOB,
         Guest_ID INT,
         PRICE INT
         )''')
    print('TABLE reservation CREATED')
except:
    print('TABLE ALREADY EXIST')



## CREATION OF 30 ROOMS
def create5():
    for i in range(1,6):
        insertDB('rooms', "({}, null, null, null, null, null, null)".format(i))
    print('Done Creating 5 rows')
