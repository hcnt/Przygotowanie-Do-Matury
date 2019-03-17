def main():
    plik = open('NAPIS.TXT')
    wyniki = open('ZADANIE5.TXT', 'w')
    zad5a(plik, wyniki)
    zad5b(plik, wyniki)
    zad5c(plik, wyniki)


def czyPierwsza(liczba):
    if liczba == 2:
        return True
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


def zad5a(plik, wynik):
    ilosc = 0
    for linia in plik:
        linia = linia.rstrip()
        linia = map(ord, linia)
        suma = sum(linia)
        if czyPierwsza(suma):
            ilosc += 1
    print('a)', ilosc, file=wynik)
    plik.seek(0)


def czyRosnaca(tab):
    for i in range(1, len(tab)):
        if tab[i] <= tab[i - 1]:
            return False
    return True

def zad5b(plik, wynik):
    print("b)", file=wynik)
    for linia in plik:
        linia = linia.rstrip()
        liniaNumery = map(ord, linia)
        if czyRosnaca(list(liniaNumery)):
            print(linia, file=wynik)
    plik.seek(0)

def zad5c(plik, wynik):
    linie = []
    print("c)", file=wynik)
    for linia in plik:
        linia = linia.rstrip()
        if linia in linie:
            print(linia, file=wynik)
        linie.append(linia)


main()
