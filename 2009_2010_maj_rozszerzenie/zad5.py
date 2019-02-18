def main():
    pesel = open('pesel.txt')
    wynik = open('odp_5.txt', 'w')
    zad5a(pesel, wynik)
    zad5b(pesel, wynik)
    zad5c(pesel, wynik)
    zad5d(pesel, wynik)


def zad5a(plik, wynik):
    liczbaOsob = 0
    for line in plik:
        line = line.rstrip()
        miesiac = line[2:4]
        if miesiac == '12':
            liczbaOsob += 1
    print("a)", liczbaOsob, file=wynik)
    plik.seek(0)


def zad5b(plik, wynik):
    liczbaOsob = 0
    for line in plik:
        line = line.rstrip()
        plec = line[-2]
        if int(plec) % 2 == 0:
            liczbaOsob += 1
    print("b)", liczbaOsob, file=wynik)
    plik.seek(0)


def zad5c(plik, wynik):
    liczbaOsob = {}
    for line in plik:
        line = line.rstrip()
        rok = line[:2]
        if rok in liczbaOsob.keys():
            liczbaOsob[rok] += 1
        else:
            liczbaOsob[rok] = 1
    maxRok = max(liczbaOsob, key=liczbaOsob.get)
    print("c)", maxRok, file=wynik)
    plik.seek(0)


def prawdilowaCyfraKontrolna(pesel):
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    pesel = list(pesel)
    pesel = list(map(int, pesel))[:-1]
    suma = sum(a * b for a, b in zip(pesel, wagi))
    reszta = suma % 10
    cyfra = (10 - reszta) % 10
    return cyfra


print(prawdilowaCyfraKontrolna("75121968629"))  # 9


def zad5d(plik, wynik):
    niepoprawne = []
    for line in plik:
        line = line.rstrip()
        cyfraK = line[-1]
        prawidlowaCyfraK = prawdilowaCyfraKontrolna(line)
        if cyfraK != prawidlowaCyfraK:
            niepoprawne.append(line)
    niepoprawne.sort()
    print("d)", *niepoprawne, file=wynik, sep='\n')


main()
