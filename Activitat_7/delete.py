import psycopg2
from connections import connections


def delete(movie_id):
    conn = connections()
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM movies WHERE id = %s', (movie_id,))
    except (Exception, psycopg2.Error) as error:
        
        print("Error",error)
        
    conn.commit()
    conn.close()