import pymysql
from config import host, user, password, db_name



try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name
    )
    print("succes")

    with connection.cursor() as cursor:
        drop_table_query = "DROP TABLE rooms"
        cursor.execute(drop_table_query)

    with connection.cursor() as cursor:
        create_table_query = "CREATE TABLE rooms(id int AUTO_INCREMENT, name varchar(32), PRIMARY KEY(id));"
        cursor.execute(create_table_query)



except Exception as ex:
    print("connection refused")

finally:
    connection.close()
