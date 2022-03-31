import pymysql
from config import host, user, password, db_name



connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name
    )
print("succes")



with connection.cursor() as cursor:
    create_table_query = "SELECT * from rooms"
    cursor.execute(create_table_query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)


connection.close()
