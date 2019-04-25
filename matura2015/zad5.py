def main():
    plik = open("kraina.txt")
    wyniki = open('wynik5.txt', 'w')
    dane = [line.rstrip().split(';') for line in plik]
    zad5_1(dane, wyniki)
    zad5_2(dane, wyniki)
    zad5_3(dane, wyniki)


def zad5_1(dane, wyniki):
    slownik = {}
    for wiersz in dane:
        slownik[wiersz[0]] = int(wiersz[1]) + int(wiersz[2])
    print("zad5.1", file=wyniki)
    slownik2 = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for woj in slownik:
        slownik2[woj[-1]] += slownik[woj]
    print(slownik2)
    for reg in slownik2:
        print(reg, slownik2[reg], sep=',', file=wyniki)


def zad5_2(dane, wyniki):
    wojewodztwa = []
    for wiersz in dane:
        if int(wiersz[3]) > int(wiersz[1]) and int(wiersz[4]) > int(wiersz[2]):
            wojewodztwa.append(wiersz[0])
    ilosci = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    print("zad5.2", file=wyniki)
    for woj in wojewodztwa:
        ilosci[woj[-1]] += 1
    for reg in ilosci:
        print(reg, ilosci[reg], file=wyniki)


def zad5_3(dane, wyniki):
    ludnosc2013 = {}
    ludnosc2014 = {}
    tempawzrostu = {}
    for wiersz in dane:
        ludnosc2013[wiersz[0]] = int(wiersz[1]) + int(wiersz[2])
        ludnosc2014[wiersz[0]] = int(wiersz[3]) + int(wiersz[4])
        tempawzrostu[wiersz[0]] = zaokr(round(ludnosc2014[wiersz[0]] / ludnosc2013[wiersz[0]], 6))
    # print(ludnosc2013['w01D'])
    # print(ludnosc2014['w01D'])
    # print(tempawzrostu['w01D'])
    print(ludnosc(2025, ludnosc2014['w01D'], ludnosc2013['w01D'], tempawzrostu['w01D']))
    ludnosc2025 = 0
    for woj in ludnosc2014:
        x,czyCzyByloPrzeludnienie = ludnosc(2025, ludnosc2014[woj], ludnosc2013[woj], tempawzrostu[woj])
        ludnosc2025 += x
    print("liczba mieszkancow edulandii 2025:", ludnosc2025, file=wyniki)


def ludnosc(rok, ludnoscWoj2014, ludnoscWoj2013, tempo, czyByloPrzeludnienie):
    if rok == 2014:
        return ludnoscWoj2014, False
    x = ludnosc(rok - 1, ludnoscWoj2014, ludnoscWoj2013, tempo,czyByloPrzeludnienie)
    if int(x*tempo) > 2 * ludnoscWoj2013:
        czyByloPrzeludnienie = True
    return int(x*tempo)


def zaokr(n):
    return float(str(n)[:-1])


main()
