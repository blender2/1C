def recommendation(_date, _time, _people, connection):
    with connection.cursor() as cursor:
        create_table_query = "SELECT name from rooms join booking on rooms.room_id = booking.room_id WHERE rooms.capacity >= " + str(_people)
        cursor.execute(create_table_query)
        rows = cursor.fetchall()

    return rows
