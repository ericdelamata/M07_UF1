n1 = float(input("Introdueix un valor: "))
n2 = float(input("Introdueix un altre valor: "))
operacio = input("Que vols operar: ")

if operacio=="suma":
    print(n1+n2)
elif operacio=="resta":
    print(n1-n2)
elif operacio=="divisio":
    print(n1/n2)
elif operacio=="multiplicacio":
    print(n1*n2)
else:
    print("No es una operacio vàlida")