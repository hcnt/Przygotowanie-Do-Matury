import math
from decimal import Decimal,getcontext

getcontext().prec = 3


def main():
    wyniki = open("wykres.txt", 'w')
    sumulacja(wyniki)


def sumulacja(wynik):
    kury = 200
    czyNiedziela = False
    cenaPaszy = 1.9
    cenaJajka = 0.9
    cenaKury = 18
    realnyZysk = 0
    sumaPaszy = 0
    paszaNaKureNaDzien = 0.2
    for i in range(1, 181):
        # rano
        # if kury == 200:
        # print("kury rano = 200",i)
        if i % 30 == 0:
            kupioneKury = 0.2 * kury
            kupioneKury = math.floor(kupioneKury)
            zaplataZaKury = kupioneKury * cenaKury
            kury += kupioneKury
        else:
            zaplataZaKury = 0
        # posilek
        zaplataZaPasze = kury * paszaNaKureNaDzien * cenaPaszy
        sumaPaszy += zaplataZaPasze
        # sprzedaż
        if not i % 7 == 0:
            zarobekTegoDnia = kury * cenaJajka
        else:
            zarobekTegoDnia = 0
        # noc
        if i % 2 != 0:
            kury -= 2
        # if kury == 200:
        # print("kury w nocy = 200",i)
        dziennyZysk = zarobekTegoDnia - zaplataZaPasze - zaplataZaKury
        realnyZysk += dziennyZysk
        print(i,round(zarobekTegoDnia,2),round(zaplataZaKury+zaplataZaPasze,2),file=wynik)

    # print(sumaPaszy)


main()
