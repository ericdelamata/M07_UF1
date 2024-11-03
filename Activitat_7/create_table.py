import psycopg2
from connections import connections


def create_table():
    conn = connections()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id BIGINT PRIMARY KEY NOT NULL UNIQUE,
                name VARCHAR(50) NOT NULL,
                release_year INT NOT NULL,
                director VARCHAR(50) NOT NULL,
                rating FLOAT NOT NULL,
                synopsis VARCHAR(255) NOT NULL
            )
        ''')
    except (Exception, psycopg2.Error) as error:
        
        print("Error",error)
        
    conn.commit()
    conn.close()