usu = input("Fiqueu 10 numeros separats per espais: ")
usu = usu.split()
nums = []
sumt = 0
for x in usu:
    nums.append(int(x))
    sumt+=float(x)
mitj= sumt/len(nums)
print("Numeros de l'usuari: ",nums)
print("Suma total: ",sumt)
print("Mitjana: ",mitj)
nums.append(sumt)
nums.append(mitj)
print(nums)
