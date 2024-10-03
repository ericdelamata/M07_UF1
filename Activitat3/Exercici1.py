#fa una tupla del 1 al numero especificat per l'usuari
num = int(input("Posa un numero del 10 al 100: "))

nums = list()

for x in range(1,num+1):
    nums.append(x)
mytuple = tuple(nums)
print(mytuple)