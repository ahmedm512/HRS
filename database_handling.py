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
        return print(c.fetchall())
    except:
        print(f'[EXCEPTION] FAILED TO SELECT {tableName}')


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
        if output[0][0] is None or c.fetchall()[0][0] == 0:
            return (True, roomNo)
        elif output[0][0] == 1:
            return (False, roomNo)
        elif output[0][0] == 2:
            print(f'Room {roomNo} is Under Maintenance')
            return (False, roomNo)
    except:
        return False


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
        date_objIn = datetime.datetime.strptime(dateIn, '%d/%m/%Y')
        date_objOut = datetime.datetime.strptime(dateOut, '%d/%m/%Y')
        num_nights = abs((date_objIn.date() - date_objOut.date()).days)
        acc_cost = num_nights * price
        return acc_cost, date_objIn.date(), date_objOut.date(), num_nights
    except:
        return 'Error in dateHandling' + Exception.message



