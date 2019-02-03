from collections import Counter
from itertools import combinations


def main():
    sygnaly = open('sygnaly.txt')
    przyklad = open('przyklad.txt')
    wyniki = open('wyniki4.txt', 'w')
    zad1(sygnaly, wyniki)
    zad2(sygnaly, wyniki)
    zad3(sygnaly, wyniki)
    sygnaly.close()
    przyklad.close()
    wyniki.close()


def zad1(dane, wyniki):
    napis = ""
    for i, line in enumerate(dane):
        if (i + 1) % 40 == 0 and i + 1 >= 40:
            napis += line[9]
    print("zad 4.1:", napis, file=wyniki)
    dane.seek(0)


def zad2(dane, wyniki):
    iloscLiterWSlowach = {}
    for line in dane:
        line = line.rstrip()
        x = dict(Counter(line))
        iloscLiter = len(x.keys())
        iloscLiterWSlowach[line] = iloscLiter
    maxSlowo = max(iloscLiterWSlowach, key=iloscLiterWSlowach.get)
    dlogosc = iloscLiterWSlowach.get(maxSlowo)
    print("zad 4.2:", maxSlowo, dlogosc, file=wyniki)
    dane.seek(0)


def zad3(dane, wyniki):
    print("zad 4.3: ", file=wyniki)
    for line in dane:
        line = line.rstrip()
        if czyLiterySaOddaloneOMax10(line):
            print(line, file=wyniki)
    dane.seek(0)


def czyLiterySaOddaloneOMax10(string):
    litery = list(dict(Counter(string)).keys())
    litery = list(map(ord, litery))
    kombinacjeLiter = list(combinations(litery, 2))
    for c in kombinacjeLiter:
        if abs(c[0] - c[1]) >= 10:
            return False
    return True


main()
