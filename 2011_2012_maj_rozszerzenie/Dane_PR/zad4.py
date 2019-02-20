def main():
    tj = open('tj.txt')
    klucze1 = open('klucze1.txt')
    klucze2 = open('klucze2.txt')
    sz = open('sz.txt')
    wynik4a = open('wynik4a.txt', 'w')
    wynik4b = open('wynik4b.txt', 'w')
    zad4a(tj,klucze1,wynik4a)
    zad4b(sz,klucze2,wynik4b)


def szyfruj(slowo, klucz):
    slowo = list(slowo)
    klucz = list(klucz)
    lenKlucz = len(klucz)
    wielokrotnosci = 0
    zaszyfrowaneSlowo = []
    for i, litera in enumerate(slowo):
        if i - wielokrotnosci * lenKlucz >= lenKlucz:
            wielokrotnosci += 1
        kluczIndex = i - wielokrotnosci * lenKlucz
        if kluczIndex >= lenKlucz:
            print(slowo,klucz)
        suma = ord(litera) + ord(klucz[kluczIndex]) - 64
        if suma > 90:
            suma = suma - 26
        if suma > 90 or suma < 65:
            print(suma,litera,slowo,klucz)
        zaszyfrowaneSlowo.append(chr(suma))
    return ''.join(zaszyfrowaneSlowo)


def deszyfruj(slowo, klucz):
    slowo = list(slowo)
    klucz = list(klucz)
    lenKlucz = len(klucz)
    wielokrotnosci = 0
    zaszyfrowaneSlowo = []
    for i, litera in enumerate(slowo):
        if i - wielokrotnosci * lenKlucz >= lenKlucz:
            wielokrotnosci += 1
        kluczIndex = i - wielokrotnosci * lenKlucz
        if kluczIndex >= lenKlucz:
            print(slowo,klucz)
        suma = ord(litera) - ord(klucz[kluczIndex]) + 64
        if suma < 65:
            suma = suma + 26
        if suma > 90 or suma < 65:
            print(suma,litera,slowo,klucz)
        zaszyfrowaneSlowo.append(chr(suma))
    return ''.join(zaszyfrowaneSlowo)




def zad4a(slowa, klucze, wynik):
    slowa = slowa.readlines()
    klucze = klucze.readlines()
    slowa = [szyfruj(a.rstrip(), b.rstrip()) for a, b in zip(slowa, klucze)]
    for slowo in slowa:
        print(slowo, file=wynik)

def zad4b(slowa, klucze, wynik):
    slowa = slowa.readlines()
    klucze = klucze.readlines()
    slowa = [deszyfruj(a.rstrip(), b.rstrip()) for a, b in zip(slowa, klucze)]
    for slowo in slowa:
        print(slowo, file=wynik)


main()
