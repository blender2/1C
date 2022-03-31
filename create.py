from typing import final
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
except Exception:
    print("connection refused")

   
try:
    with connection.cursor() as cursor:
        drop_table_query = "DROP TABLE IF EXISTS rooms"
        cursor.execute(drop_table_query)

        create_table_query = "CREATE TABLE rooms(id int AUTO_INCREMENT, name varchar(32), capacity int,  PRIMARY KEY(id));"
        cursor.execute(create_table_query)
except Exception:
    print("creation refused")
finally:
    connection.close()
