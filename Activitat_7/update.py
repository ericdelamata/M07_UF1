import psycopg2
from connections import connections


def update(movie_id, name=None, release_year=None, director=None, rating=None, synopsis=None):
    conn = connections()
    try:
        cursor = conn.cursor()
        if name is not None:
                cursor.execute('UPDATE users SET name = %s WHERE id = %s', (name, movie_id))
        if release_year is not None:
                cursor.execute('UPDATE users SET release_year = %s WHERE id = %s', (release_year, movie_id))
        if director is not None:
                cursor.execute('UPDATE users SET director = %s WHERE id = %s', (director, movie_id))
        if rating is not None:
                cursor.execute('UPDATE users SET rating = %s WHERE id = %s', (rating, movie_id))
        if synopsis is not None:
                cursor.execute('UPDATE users SET synopsis = %s WHERE id = %s', (synopsis, movie_id))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        
        print("Error",error)
        
    conn.close()