areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]
#Imprimeix el segon element
print(areas_pis[1])
#Imprimeix l'ultim element
print(areas_pis[len(areas_pis)-1])
#Imprimeix el area de la terrassa
print(areas_pis[areas_pis.index("Terrassa")+1])
#Imprimeix tots els tres primers elements
for x in range(3):
    print(areas_pis[x])
#Imprimeix desde el 3er element fins l'ultim
for x in range(2,len(areas_pis)):
    print(areas_pis[x])
#Imprimeix la area total de les dues habitacions
print(float(areas_pis[areas_pis.index("Habitació1")+1])+float(areas_pis[areas_pis.index("Habitació2")+1]))
#canvia l'area del lavabo i l'imprimeix
areas_pis[areas_pis.index("Lavabo")+1] = 6.89
print(areas_pis)
#Afageix el pati interior amb la seva area i l'imprimeix
areas_pis.append("Pati interior")
areas_pis.append(2.78)
print(areas_pis)
#suma totes les areas i les imprimeix
total = 0
for x in range(1,len(areas_pis),2):
    total = total+float(areas_pis[x])
print(total)