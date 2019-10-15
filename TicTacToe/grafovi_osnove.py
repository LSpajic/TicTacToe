
def mozemo_li_doci(pocetak, kraj, povezanost):
    trenutna_razina = [pocetak]
    # sljedeca_razina = [povezanost[pocetak]]
    if pocetak == kraj:
        return True
    posjeceni=[pocetak]
    while True:
        sljedeca_razina = []
        for trenutni_cvor in trenutna_razina:
            for sljedeci_cvor in povezanost[trenutni_cvor]:
                if sljedeci_cvor not in posjeceni:
                    sljedeca_razina.append(sljedeci_cvor)

        if len(sljedeca_razina) == 0:
            return False

        if kraj in sljedeca_razina:
            return True
        posjeceni.extend(sljedeca_razina)
        trenutna_razina = sljedeca_razina

# 1. -> start
# 2. -> 1.
# 3. -> 2.
#vrati: start, 1., 2., 3.
def backtrack( pocetak, zadnji, nadredjeniii):
    rezultat = [zadnji]
    trenutni = zadnji
    while trenutni != pocetak:
        rezultat.append(nadredjeniii[trenutni])
        trenutni = nadredjeniii[trenutni]

    rezultat.reverse()

    return rezultat

def daj_put(pocetak, kraj, povezanost):
    trenutna_razina = [pocetak]
    # sljedeca_razina = [povezanost[pocetak]]
    nadredjeniii = {}
    if pocetak == kraj:
        return [pocetak]
    posjeceni=[pocetak]
    while True:
        sljedeca_razina = []
        for trenutni_cvor in trenutna_razina:
            for sljedeci_cvor in povezanost[trenutni_cvor]:
                if sljedeci_cvor not in posjeceni:
                    sljedeca_razina.append(sljedeci_cvor)
                    if sljedeci_cvor not in nadredjeniii:
                        nadredjeniii[sljedeci_cvor] = trenutni_cvor
        if len(sljedeca_razina) == 0:
            return None

        if kraj in sljedeca_razina:
            return backtrack(pocetak, kraj, nadredjeniii)
        posjeceni.extend(sljedeca_razina)
        trenutna_razina = sljedeca_razina


def daj_imena_cvorova(indeksi, imena_cvorova):
    if indeksi is None:
        return None

    izlaz = []
    for i in indeksi:
        izlaz.append(imena_cvorova[i])
    return izlaz

def daj_imena_cvorova_2(indeksi, imena_cvorova):
    if indeksi is None:
        return None
    return [imena_cvorova[x] for x in indeksi]

if __name__ == '__main__':
    cvorovi = ["Zagreb", "Berlin", "Moskva", "London", "Djakovo", "Piskorevci", "Nasice","NY","CHI","ATL"]
    povezanost = {}

    povezanost[0] = [1, 4, 6]
    povezanost[1] = [0, 2, 3]
    povezanost[2] = [1]
    povezanost[3] = [1]
    povezanost[4] = [0, 5]
    povezanost[5] = [4, 6]
    povezanost[6] = [0, 5]
    povezanost[7] = [8, 9]
    povezanost[8] = [7]
    povezanost[9] = [7]


    """print(mozemo_li_doci(5, 2, povezanost)) #T
    print(mozemo_li_doci(8, 2, povezanost)) #F
    print(mozemo_li_doci(9, 8, povezanost)) #T
    print(mozemo_li_doci(2, 8, povezanost)) #F

    print(mozemo_li_doci(2, 2, povezanost)) #T"""

    print(daj_imena_cvorova(daj_put(8, 2, povezanost), cvorovi))  # F
    print(daj_imena_cvorova(daj_put(5, 2, povezanost), cvorovi))  # T
    print(daj_imena_cvorova(daj_put(9, 8, povezanost), cvorovi))  # T
    print(daj_imena_cvorova(daj_put(2, 8, povezanost), cvorovi))  # F
    print(daj_imena_cvorova(daj_put(2, 2, povezanost), cvorovi))  # T

    print(daj_imena_cvorova_2(daj_put(5, 2, povezanost), cvorovi))  # T

