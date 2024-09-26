import math
import random
intents = 20
nums = math.ceil(random.random() * 100)
print("Tens",intents,"intents per endevinar el numero secret endevant")
x = int(input("Posa el teu secret: "))
encertat = False
while (not encertat) and intents>0:
    if x>nums:
        print("El numero secret es mes petit")
    else:
        print("El numero secret es mes gran")
    intents-=1
    print("Et queden",intents,"intents")
    x = int(input("No has encertat, torna a probar: "))
    if x==nums:
        encertat = True
if encertat:
    print("Has guanyat!")
else:
    print("Has perdut...")