from collections import Counter


def main():
    plik = open("liczby.txt")
    wyniki = open('wynik4.txt', 'w')
    zad4_1(plik, wyniki)
    zad4_2(plik, wyniki)
    zad4_3(plik, wyniki)


def zad4_1(plik, wyniki):
    liczba = 0
    for line in plik:
        line = line.rstrip()
        slownik = dict(Counter(line))
        try:
            slownik['0']
        except:
            continue
        if slownik['1'] < slownik['0']:
            liczba += 1
    print("zad 4.1", file=wyniki)
    print(liczba, file=wyniki)
    plik.seek(0)


def zad4_2(plik, wyniki):
    liczba2 = 0
    liczba8 = 0
    for line in plik:
        line = line.rstrip()
        if int(line, 2) % 2 == 0:
            liczba2 += 1
        if int(line, 2) % 8 == 0:
            liczba8 += 1
    print("zad4.2", file=wyniki)
    print("podzielne przez 2:", liczba2, file=wyniki)
    print("podzielne przez 8:", liczba8, file=wyniki)
    plik.seek(0)


def zad4_3(plik, wyniki):
    tab = plik.readlines()
    tab = [int(line.rstrip(), 2) for line in tab]
    maxLiczba = max(tab)
    minLiczba = min(tab)
    maxIndex = tab.index(maxLiczba) + 1
    minIndex = tab.index(minLiczba) + 1
    print("zad 4.3", file=wyniki)
    print("wiersz maksymalnej liczby",maxIndex, file=wyniki)
    print("wiersz minimalnej liczby",minIndex, file=wyniki)
    plik.seek(0)


main()
