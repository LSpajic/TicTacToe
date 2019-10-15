dorucak = []
dorucak.append("kruska") #kruska dodan u listu
dorucak.append("jaja") #dodavanje jaja u listu

rucak = []
rucak.append("lazanje")
rucak.append("spageti")

vecera = ["sunka", "sir"]

print(dorucak)
print(rucak)
print(vecera)

jelovnik = [dorucak, rucak, vecera]

print()
print(jelovnik)
print(jelovnik[1][1])

#ispis broja elemenata jelovnika
len(jelovnik)

#iteriranje po elementima liste
for element in jelovnik:
    print(len(element))

