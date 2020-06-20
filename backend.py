import sqlite3
conn =sqlite3.connect('test.db')
c = conn.cursor()
import database_handling
'''
    Room_Number INT PRIMARY KEY,
    Guest_Name TEXT,
    Check_In_Date BLOB,
    Check_Out BLOB,
    Guest_ID INT,
    State INT,
    PRICE INT
'''


def reservations(roomNo, guestName, checkIn, price, GuestID, checkOut='null', state=1):
    try:

        if not database_handling.is_available(roomNo)[0]:
            return f'The Room is Occupied'
        database_handling.modifyRoom(roomNo, guestName, checkIn, checkOut, GuestID, state, price)
        return f'Room {roomNo} is reserved'
    except:
        print(f'[EXCEPTION] ROOM IS OCCUPIED')
        print(Exception.message)


def checkout(roomNo):
    try:
        acc_cost, dateIn, dateOut, numNights = database_handling.accommodationCalculation(roomNo)
        database_handling.modifyRoom(roomNo, 'null', 'null', 'null', 'null', 'null', 'null')
        return 'Check Out Process Done' + f'Accommodation Cost is  {acc_cost}'
    except:
        return 'error' + Exception.message

def availability(roomNo=None):
    try:
        if roomNo is None:
            available_rooms = []
            for i in range(1, 6):    #Looping Through all Rooms we have a !!![constant value] we must change it later
                if database_handling.is_available(i):
                    available_rooms.append(i)
            return print(available_rooms)
        elif roomNo is not None:
            return database_handling.is_available(roomNo)
    except:
        print(f'[EXCEPTION] SOMETHING WRONG IN AVAILABILITY')
        print(Exception.message)

