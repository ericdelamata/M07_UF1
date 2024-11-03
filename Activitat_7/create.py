import psycopg2
from connections import connections


def create(movie_id, name, release_year, director, rating, synopsis):
    conn = connections()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO movies (id, name, release_year, director, rating, synopsis)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (movie_id, name, release_year, director, rating, synopsis))
        conn.commit()
        print("Movie created successfully.")
    except psycopg2.Error as e:
        
        print(f"Error inserting movie: {e}")
        
    conn.commit()
    conn.close()