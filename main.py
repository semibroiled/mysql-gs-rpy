from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        #user=input("Enter username: "),
        user = 'acm',

        password=getpass("Enter password: "),
        database = 'online_movie_rating'
    ) as connection:
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
        # create_db_query = "CREATE DATABASE online_movie_rating"
        # with connection.cursor() as cursor:
        #     cursor.execute(create_db_query)
        print(connection)
except Error as e:
    print(e)