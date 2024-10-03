#Elimina les lletres que estan en una posicio multiple de 3 ho converteix en una tupla i ensenya la llista i la tupla
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for x in range(len(abc)-3,0,-3):
    abc.pop(x)
abctuple = tuple(abc)
print(abc)
print(abctuple)