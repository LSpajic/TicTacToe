def potencija(baza, eksponent):
    if eksponent < 0:
        return 1/potencija(baza, eksponent * -1)
    if eksponent == 0:
        return 1
    else:
        return baza*potencija(baza,eksponent-1)



if __name__ == '__main__':
    print(potencija(2,10)) # 1024
    print(potencija(3,4)) # 81
    print(potencija(1,10)) # 1
    print(potencija(10, 3)) # 1000
    print(potencija(10,-3)) # 0.001
    print(potencija(10, 3.5)) #