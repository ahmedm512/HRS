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
                if database_handling.is_available(i)[0]:
                    available_rooms.append(i)
            return print(available_rooms)
        elif roomNo is not None:
            return database_handling.is_available(roomNo)
    except:
        print(f'[EXCEPTION] SOMETHING WRONG IN AVAILABILITY')
        print(Exception.message)

def show_room(roomNo):
    try:
        database_handling.showRoom(roomNo)
    except:
        print('yes')

def maintenance(roomNo, main=0):   # 0: set maintenance, 1: set maintenance free
    if main==0:
        if availability(roomNo)[0] is False:
            return print('[Exception] YOU CANT SET RESERVED ROOM TO MAINTENANCE')
        else:
            if main == 0: # Set maintenance
                database_handling.maintenanceModifier(roomNo, state=2)
                print('ROOM IS SET TO UNDER MAINTENANCE')
    if main==1:
        database_handling.maintenanceModifier(roomNo, state='null')
        print(f'ROOM{roomNo} IS SET TO FREE')