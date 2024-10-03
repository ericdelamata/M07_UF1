#Demana les notes de 6 asignatures ho fica a un diccionari i despres ho ensenya
assNotes={"Mates":0,"Bio":0,"Religion":0,"Educacion fisica":0,"Filo":0,"Fisica":0}
for x in assNotes:
    assNotes[x] = int(input("Posa la teva nota de "+x+": "))
for x in assNotes:
    print("A "+x+" ha tret "+str(assNotes[x]))