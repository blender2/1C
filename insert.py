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
        insert_query = "INSERT INTO rooms (name, capacity) VALUES ('A', 10), ('B', 15), ('C', 50);"
        cursor.execute(insert_query)
        connection.commit()


        insert_query = "INSERT INTO booking (room_id, start_time, login) VALUES (1, '2022-01-04 02:00:00', 'bob'), (2, '2022-01-04 06:00:00', 'bob'), (3, '2022-01-04 02:00:00', 'bob');"
        cursor.execute(insert_query)
        connection.commit()

        insert_query = "INSERT INTO users (login, password) VALUES ('bob', '111');"
        cursor.execute(insert_query)
        connection.commit()
except Exception:
    print("inserting failure")
finally:
    connection.close()