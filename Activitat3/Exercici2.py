#imprimeix el mes que vulgui l'usuari si posa 0 acaba el codi
meses = ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")

x = int(input("Introduce un numero entre el 0 i el 12: "))-1
while x != -1:
    print(meses[x])
    x = int(input("Vuelve a meter un numero del 0 al 12: "))-1
