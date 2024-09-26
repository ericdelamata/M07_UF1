x=input("Escriu entre 1 i 3 paraules: ")
par = x.split()
print("Hi han",len(par),"paraules")
for y in par:
    print("Hi han",len(y),"caracters a la paraula",y)
    print("El primer caracter es",y[0],", i l'ultim es",y[-1])