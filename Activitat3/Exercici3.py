#Imprimeix la taula de multiplicar que hagi indicat el usuari
tabla = []

x = int(input("Introdueix un numero de l'1 al 10: "))

for y in range(1,11):
    tabla.append(x*y)
print(tabla)