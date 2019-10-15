
#Lista je slozena struktura koja se sastoji od niza primitiva i/ili slozenih struktura
#   - cuva poredak kojim dodajemo elemente

dorucak = [] #sad je lista_brojeva zapravo struktura lista
dorucak.append("kruska") #kruska dodan u listu

print(dorucak) #ispis liste

print(dorucak[0]) #ispis prvog elementa liste

dorucak.append("jaja") #dodavanje jaja u listu

print(dorucak[1]) #ispis drugog elementa liste
print(dorucak)

#zamjena nekog elementa liste
dorucak[0] = "jabuka"
print(dorucak)

dorucak[0] = []
dorucak[0].append([])

dorucak.remove(dorucak[0])
del(dorucak[0])

print(dorucak)

