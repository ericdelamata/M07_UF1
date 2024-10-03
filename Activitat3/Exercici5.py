#Posa les paraules de la frase de l'usuari en una tupla i despres crea un string amb tots els caracters sense repetir
frase = input("Posa una frase: ")
mai = tuple(frase.split())
par = ""
for x in mai:
    for y in x:
        if y not in par:
            par=par+y
print(mai)
print(par)