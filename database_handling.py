import sqlite3
import datetime
conn = sqlite3.connect('test.db')
c = conn.cursor()


def insertDB(tableName, VALUES):
    '''
    :param: tableName, Values :: Table Name , Values wanted to insert
    :return: String Validation || EXCEPTION
    '''

    try:
        c.execute(f'INSERT INTO {tableName} VALUES {VALUES}')
        conn.commit()
        return f'VALUES {VALUES} HAS BEEN INSERTED INTO {tableName}'
    except:
        print(f'[EXCEPTION] FAILED TO INSERT INTO {tableName}, VALUES {VALUES}')
        print(Exception.message)


def showTable(tableName):
    '''
    :param: tableName :: Table Name
    :return: String Validation || EXCEPTION
    '''
    try:
        c.execute(f'SELECT * FROM {tableName}')
        return c.fetchall()
    except:
        print(f'[EXCEPTION] FAILED TO SELECT {tableName}')


def showRoom(roomNo):
    '''
    :param roomNo: Number of the room
    :return: RoomNo  row in rooms TABLE >>contents
    '''
    try:
        c.execute(f'SELECT * FROM rooms WHERE Room_Number = {roomNo}')
        return print(c.fetchall())
    except:
        print(f'[EXCEPTION] FAILED TO SELECT {roomNo} FROM ROOMS TABLE')


def dropTable(tableName):
    '''
    :param: tableName
    :return: String Validation || EXCEPTION
    '''
    try:
        c.execute(f'DROP TABLE {tableName}')
        conn.commit()
        return f'TABLE {tableName} DROPPED'
    except:
        print(f'[EXCEPTION] FAILED TO DROP {tableName}')


def searchByID(tableName, rowid):
    '''
    :param: tableName, rowid :: Table Name , PRIMARY KEY
    :return: String Validation || EXCEPTION
    '''
    try:
        c.execute(f'SELECT * FROM {tableName} WHERE rowid = {rowid}')
        return print(c.fetchall())
    except:
        print(f'[EXCEPTION] FAILED TO SELECT FROM {tableName} ROWID {rowid}')



def is_available(roomNo):
    '''
    :param: roomNo :: Stands for the Room Number
    :return: Tuple (Bool Value representing the state, Room Number)
    '''
    try:
        c.execute(f'SELECT state FROM rooms WHERE Room_Number = {roomNo}')
        output = c.fetchall()
        if output[0][0] is None or output[0][0] == 0:
            return (True, roomNo, 'Free')
        elif output[0][0] == 1:
            return (False, roomNo, 'NotFree')
        elif output[0][0] == 2:
            print(f'Room {roomNo} is Under Maintenance')
            return (False, roomNo, 'Under Maintenance')
    except:
        return (False,roomNo)


def modifyRoom(roomNo, guestName, checkIn, checkOut, GuestID, state, price):
    try:
        c.execute(f'''UPDATE rooms
        SET Guest_Name = '{guestName}',
        Check_In_Date = '{checkIn}',
        Check_Out = '{checkOut}',
        Guest_ID = {GuestID},
        State = {state},
        PRICE = {price} 
        WHERE
        Room_Number = {roomNo}''')
        conn.commit()
        return f'Room {roomNo} Reserved to {guestName}'
    except:
        print(f'[EXCEPTION] SOMETHING WENT WRONG')
        print(Exception.message)


def maintenanceModifier(roomNo, state):
    try:
        c.execute(f'''UPDATE rooms
        SET State = {state}
        WHERE
        Room_Number = {roomNo}''')
        conn.commit()
    except:
        print(f'[EXCEPTION] SOMETHING WENT WRONG MAINTENANCE MODIFIER')
        print(Exception.message)

def accommodationCalculation(roomNo, checkOutDate=None):
    try:
        c.execute(f'''SELECT Check_In_Date, Check_Out, PRICE FROM rooms WHERE Room_Number = {roomNo}''')
        date_price = c.fetchall()
        dateIn = date_price[0][0]
        if checkOutDate is None:
            dateOut = date_price[0][1]
        else:
            pass
        price = date_price[0][2]
        date_objIn = datetime.datetime.strptime(dateIn, '%Y-%m-%d')
        date_objOut = datetime.datetime.strptime(dateOut, '%Y-%m-%d')
        num_nights = abs((date_objIn.date() - date_objOut.date()).days)
        acc_cost = num_nights * price
        return acc_cost, date_objIn.date(), date_objOut.date(), num_nights
    except:
        return 'Error in dateHandling' + Exception.message


def is_reserved(roomNo, checkIn, checkOut):
    try:
        c.execute(f'''SELECT Check_In_Date, Check_Out FROM reservation
                     WHERE
                     Room_Number = {roomNo}''')
        out = c.fetchall()
        if not out:
            return (True, roomNo)
        else:
            cIn = datetime.datetime.strptime(checkIn, '%Y-%m-%d')
            cOut = datetime.datetime.strptime(checkOut, '%Y-%m-%d')
            for i in out:
                l = datetime.datetime.strptime(i[0], '%Y-%m-%d') # checkin
                h = datetime.datetime.strptime(i[1], '%Y-%m-%d') # checkout
                if cIn < h and cOut > l:
                    return (False, roomNo)
            return(True, roomNo)
    except:
        print('error')
        return(False, roomNo)


def rem_reserved(Reservation_Number):
    try:
        c.execute(f'''DELETE FROM reservation
                     WHERE
                     Reservation_Number = {Reservation_Number}''')
        conn.commit()
        return 'Done'
    except:
        return 'Error'


def search_by(table, arg1, arg2):
    try:
        c.execute(f'''SELECT * FROM {table}
                      WHERE
                      {arg1} = {arg2}''')
        return c.fetchall()
    except:
        return f'Error'

