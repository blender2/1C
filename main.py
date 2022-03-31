from multiprocessing import connection
import pymysql
import searcher
from config import host, db_name, user, password
from datetime import date, timedelta

_login = ""
_password = ""


def twodigit(_str):
    if len(_str) < 2:
        return "0" + _str
    return _str

def datetime(_date, _time):
    _date = date.today() + timedelta(days=_date - 1)  

    res = "\'" + str(_date.year) + "-" + twodigit(str(_date.day)) + "-" + twodigit(str(_date.month)) + " " + twodigit(str((_time-1) * 2)) + ":00:00" + "\'"
    return res

#connection to db
try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name
    )      
except Exception:
    print("connection failure")


#start
print("1: sign in\n2: log in")
_acc = int(input())

if (_acc == 1):
    print("login:\n ", end="")
    _login = input()
    print("password:\n ", end="")
    _password = input()


    with connection.cursor() as cursor:
        create_table_query = "SELECT COUNT(login) from users WHERE login =\'" +str(_login) +"\'"
        cursor.execute(create_table_query)
        rows = cursor.fetchall()
    print(rows[0][0])
    if (rows[0][0] == 0):
            with connection.cursor() as cursor:
                insert_query = "INSERT INTO users (login, password) VALUES ( \'"+ str(_login) + "\', \'"+ str(_password)+"\');"
                cursor.execute(insert_query)
                connection.commit()
            print("account created")
    else:
        print("login busy, try another one")
        exit()


elif (_acc == 2):
    print("login:\n ", end="")
    _login = input()
    print("password:\n ", end="")
    _password = input()
    with connection.cursor() as cursor:
        create_table_query = "SELECT COUNT(login) from users WHERE login =\'" +str(_login) +  "\' AND password = \'" + str(_password) + "\'"
        cursor.execute(create_table_query)
        rows = cursor.fetchall()
        if (rows[0][0] != 1):
            print("wrong login/password")
            exit()




print("Choose date:")
today = date.today()
for i in range(0, 7):
    print("{}: {}.{}.{}".format(i+1, today.day, today.month, today.year))
    today += timedelta(days=1)

_date = int(input())

print("Choose time:")

today = date.today()
for i in range(0, 12):
    print("{}: {}:00 - {}:59".format(i+1, 2*i, 2*i+1))
    today += timedelta(days=1)

_time = int(input())

print("enter number of people")
_people = int(input())




with connection.cursor() as cursor:
    create_table_query = "SELECT name, room_id from rooms WHERE capacity >=" +str(_people) +  " AND name NOT IN ( SELECT name from rooms join booking on rooms.room_id = booking.room_id" +" WHERE start_time = "+ datetime(_date,_time)+ ")"
    cursor.execute(create_table_query)
    rows = cursor.fetchall()


print("available rooms with suitable amount of space, which room to book: ")
k = 0
for i in range(0, len(rows)):
    print (i+1, end=": ")
    print(rows[i][0]) 
print(str(len(rows)+1) + ": choose other rooms")



_in = int(input())


if _in > 0 and _in < len(rows)+1:
    with connection.cursor() as cursor:
        insert_query = "INSERT INTO booking (room_id, start_time) VALUES ( "+ str(rows[_in-1][1]) + ", "+ datetime(_date,_time)+");"
        cursor.execute(insert_query)
        connection.commit()


