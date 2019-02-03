def zadA(auta, osoby, wypadki):
    n = 0
    for osoba in osoby:
        for auto in auta:
            if osoba[0] == auto[3]:
                for wypadek in wypadki:
                    if auto[0] == wypadek[2]:
                        n += 1
                        break
    print(n)


def zadB(auta, osoby, wypadki):
    maxOdszk = ["nr_rej", "imie", "nazwisko", 0]
    for osoba in osoby:
        for auto in auta:
            if osoba[0] == auto[3]:
                for wypadek in wypadki:
                    if wypadek[3] > maxOdszk[3]:
                        maxOdszk[0] = wypadek[2]
                        maxOdszk[1] = osoba[1]
                        maxOdszk[2] = osoba[2]
                        maxOdszk[3] = wypadek[3]
    print(maxOdszk)


def zadC(wypadki):
    sum2006 = 0
    sum2007 = 0
    for wypadek in wypadki:
        if wypadek[1][:4] == '2006':
            sum2006 += wypadek[3]
        if wypadek[1][:4] == '2007':
            sum2007 += wypadek[3]
    print(sum2006, sum2007)


def zadD(auta, wypadki):
    marki = {}
    for auto in auta:
        if not auto[1] in marki.keys():
            marki[auto[1]] = 0
        for wypadek in wypadki:
            if wypadek[2] == auto[0]:
                marki[auto[1]] += 1
    maxMarka = max(marki, key=marki.get)
    maxWartosc = marki.get(maxMarka)
    print(maxMarka,maxWartosc)

def zadE(auta,osoby,wypadki):
    liczby = {'A':0,'B':0,'C':0,'D':0}
    for osoba in osoby:
        for auto in auta:
            if osoba[0] == auto[3]:
                for wypadek in wypadki:
                    if wypadek[2] == auto[0]:
                        liczby[osoba[3]] += 1
    print(liczby)


def main():
    osoby = open('osoby.txt').readlines()
    wypadki = open('wypadki.txt').readlines()
    auta = open('auta.txt').readlines()
    for i in range(len(osoby)):
        osoby[i] = osoby[i].rstrip().split()

    for i in range(len(wypadki)):
        wypadki[i] = wypadki[i].rstrip().split()
        wypadki[i][0] = int(wypadki[i][0])
        wypadki[i][3] = int(wypadki[i][3][:-3])

    for i in range(len(auta)):
        auta[i] = auta[i].rstrip().split()

    zadA(auta, osoby, wypadki)
    zadB(auta, osoby, wypadki)
    zadC(wypadki)
    zadD(auta, wypadki)
    zadE(auta, osoby, wypadki)


main()
