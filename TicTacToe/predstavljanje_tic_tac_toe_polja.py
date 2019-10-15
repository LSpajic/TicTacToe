import os
clear = lambda: os.system('cls')

tic_tac_toe_field = [[],[],[]] #lista redaka

CROSS = "x"
NOUGHT = "o"
EMPTY = " "

for stupac in range(0,3):
    for i in range(0,3):
        tic_tac_toe_field[stupac].append(EMPTY)

def ispis_polje(polje):
    for redak in range(0,3):
        print(tic_tac_toe_field[redak][0], end="")
        print("|", end="")
        print(tic_tac_toe_field[redak][1], end="")
        print("|", end="")
        print(tic_tac_toe_field[redak][2])
        if redak != 2:
            print("-----")


# ispis_polje(tic_tac_toe_field)            
# tic_tac_toe_field[1][1] = CROSS
# ispis_polje(tic_tac_toe_field) 
# tic_tac_toe_field[0][1] = NOUGHT
# ispis_polje(tic_tac_toe_field) 

def valjani_argumenti( redak, stupac, polje):
    if redak > 2 or redak < 0 or stupac > 2 or stupac < 0:
        return False
    if tic_tac_toe_field[redak][stupac] != EMPTY:
        return False
    return True
def provjera_redaka(polje,igrac_na_potezu):
    for redak in range(0,3):
        je_li_redak_pobjeda = True
        for stupac in range(0,3):
            if polje[redak][stupac] != igrac_na_potezu:
                je_li_redak_pobjeda = False
                break
        if je_li_redak_pobjeda:
            return True

    return False


def provjera_stupaca(polje,igrac_na_potezu):
    for stupac in range(0,3):
        stupac_pobjeda = True
        for redak in range(0,3):
            if polje[redak][stupac] != igrac_na_potezu:
                stupac_pobjeda = False
                break
        if stupac_pobjeda:
            return True
    return False

def provjera_dijagonala(polje,igrac_na_potezu):
    pobjeda=True
    for i in range(0, 3):
        if polje[i][i] != igrac_na_potezu:
            pobjeda=False
    if pobjeda:
        return True

    pobjeda=True
    for i in range(0, 3):
        if polje[i ][2-i] != igrac_na_potezu:
            pobjeda=False
    if pobjeda:
        return True
    return False

def provjera_pobjede(polje,igrac_na_potezu):
    return provjera_dijagonala(polje,igrac_na_potezu) or provjera_stupaca(polje,igrac_na_potezu) or provjera_redaka(polje,igrac_na_potezu)



trenutni_igrac = CROSS
while True:
    print("Igra ", trenutni_igrac)
    redak = int(input("unesi redak:"))
    stupac = int(input("unesi stupac:"))

    if not valjani_argumenti(redak, stupac, tic_tac_toe_field):
        print("Nisu valjani argumenti.")
        continue


    #provjerit je li input dozvoljen.
    #   dozvoljen je ako na tom mjestu nema nista i veci ili jednak 0 i manji ili jednak 2
    #provjera pobjednika
    clear()
    tic_tac_toe_field[redak][stupac]=trenutni_igrac
    ispis_polje(tic_tac_toe_field)
    if provjera_pobjede(tic_tac_toe_field,trenutni_igrac):
        print(trenutni_igrac,"je pobjedio")
        break
    
    if trenutni_igrac == CROSS:
        trenutni_igrac = NOUGHT
    else: trenutni_igrac = CROSS
