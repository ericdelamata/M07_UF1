import psycopg2
from connections import connections


def read():
    conn = connections()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM movies')
        movies = cursor.fetchall()
        for movie in movies:
            print(movie)
    except (Exception, psycopg2.Error) as error:
        print("Error",error)
    conn.close()