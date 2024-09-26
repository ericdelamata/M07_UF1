par=input("Introdueix dues paraules: ")
x=par.split()
if len(x[0])<3 or len(x[1])<3:
    print("Les paraules son massa curtes")
else:
    final1 = x[1][0]+x[1][1]
    final2 = x[0][0]+x[0][1]
    for y in range(2,len(x[0])):
        final1 = final1+x[0][y]
    for y in range(2,len(x[1])):
        final2 = final2+x[1][y]
    print(final1,final2)