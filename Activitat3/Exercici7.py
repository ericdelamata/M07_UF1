#Insereix noms amb la seva edat a un diccionari
dict = {}
nom = input("Posa el nom (si vols parar d'afegir posa 0): ")
while not nom=="0":
    edat = input("Posa l'edat: ")
    dict[nom] = int(edat)
    nom = input("Posa el nom (si vols parar d'afegir posa 0):")
print(dict)
