from create_table import create_table
from create import create
from read import read
from update import update
from delete import delete


def main_menu():
    
    print("\nMenu:")
    print("1. Crear")
    print("2. Llegir")
    print("3. Actualitzar")
    print("4. Eliminar")
    print("5. Crear taula")
    print("6. Sortir")


    choice = input("Tria una opció: ")
    
    while not choice == '6':

        if choice == '1':
            movie_id = input("Id: ")
            name = input("Nom: ")
            release_year = int(input("Any de llançament: "))
            director = input("Director: ")
            rating = input("Valoració: ")
            synopsis = input("Sinopsis: ")
            create(movie_id, name, release_year, director, rating, synopsis)

        elif choice == '2':
            read()

        elif choice == '3':
            print("Els camps que no vulguis cambiar deixals buits")
            movie_id = int(input("ID de la pelicula a actualitzar: "))
            name = input("Nou nom: ")
            release_year = input("Nou any de llançament: ")
            director = input("Nou director: ")
            rating = input("Nova valoració: ")
            synopsis = input("Nova sinopsis: ")
            update(movie_id, name or None, int(release_year) if release_year else None, director or None, rating or None, synopsis or None)

        elif choice == '4':
            movie_id = int(input("ID de l'usuari a eliminar: "))
            delete(movie_id)

        elif choice =='5':
            create_table()

        else:
            print("Opcio no valida")
            
        print("\nMenu:")
        print("1. Crear")
        print("2. Llegir")
        print("3. Actualitzar")
        print("4. Eliminar")
        print("5. Crear taula")
        print("6. Sortir")


        choice = input("Escull: ")


main_menu()