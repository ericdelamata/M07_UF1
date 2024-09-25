preu = float(input("Preu en €: "))
iva = int(input("El IVA (4%, 10%: o 21%): "))
while not (iva==4 or iva==10 or iva==21):
    iva = int(input("Aquest IVA no es valid: "))
ivado=preu*(iva/100)
total=preu+ivado
print("El preu inicial es ",preu)
print("El valor del IVA es ",ivado)
print("El valor total es ", total)