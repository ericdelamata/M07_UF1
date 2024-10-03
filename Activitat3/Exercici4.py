#ordena els numeros que hagi posat l'usuari de menor a major els posa en una tupla i l'imprimeix
nums = input("Fiqueu 10 numeros separats per espais: ")

si = nums.split()
sa = []
for x in si:
    sa.append(int(x))
sa.sort()
print(tuple(sa))