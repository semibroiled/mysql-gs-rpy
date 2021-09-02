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
        
        create_movies_table_query = """
    CREATE TABLE movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT
)
""" 
        create_reviewers_table_query = """
CREATE TABLE reviewers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
)
"""

        create_ratings_table_query = """
CREATE TABLE ratings (
    movie_id INT,
    reviewer_id INT,
    rating DECIMAL(2,1),
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
    PRIMARY KEY(movie_id, reviewer_id)
)
"""
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                print(db)
            #cursor.execute(create_movies_table_query)
            # cursor.execute(create_reviewers_table_query)
            # cursor.execute(create_ratings_table_query)
            # connection.commit()

        # create_db_query = "CREATE DATABASE online_movie_rating"
        # with connection.cursor() as cursor:
        #     cursor.execute(create_db_query)
        print(connection)
        show_table_query_1 = "DESCRIBE movies"
        show_table_query_2 = "DESCRIBE reviewers"
        show_table_query_3 = "DESCRIBE ratings"
        
        with connection.cursor() as cursor:
            cursor.execute(show_table_query_1)
            # Fetch rows from last executed query
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.execute(show_table_query_2)
            # Fetch rows from last executed query
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.execute(show_table_query_3)
            # Fetch rows from last executed query
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)