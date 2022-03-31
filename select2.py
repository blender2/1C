import pymysql
from config import host, user, password, db_name

from datetime import date, timedelta

def twodigit(_str):
    if len(_str) < 2:
        return "0" + _str
    return _str

def datetime(_date, _time):
    _date = date.today() + timedelta(days=_date - 1)  

    res = "\'" + str(_date.year) + "-" + twodigit(str(_date.day)) + "-" + twodigit(str(_date.month)) + " " + twodigit(str((_time-1) * 2)) + ":00:00" + "\'"
    return res #"YEAR(start_time) = "+str(_date.year) + " AND DAY(start_time) = " + str(_date.month) + " AND MONTH(start_time) = " + str(_date.day)# + "AND HOUR(TIME(start_time)) = "+ str(_time * 2)

connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name
    )


with connection.cursor() as cursor:
    create_table_query = "SELECT * from users"
    cursor.execute(create_table_query)
    rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
