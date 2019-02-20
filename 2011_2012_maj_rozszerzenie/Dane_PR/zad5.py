from math import factorial


def newton(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))


def trojkat(n):
    n = n - 1
    rzad = [int(newton(n, i)) for i in range(n + 1)]
    return rzad


def liczbaCyfr(tab):
    tab = map(str, tab)
    cyfry = 0
    for x in tab:
        cyfry += len(x)
    return cyfry


def zad5a(wynik):
    print("a)", max(trojkat(10)), max(trojkat(20)), max(trojkat(30)), file=wynik)


def zad5b(wynik):
    print("b)", file=wynik)
    cyfry = [liczbaCyfr(trojkat(a)) for a in range(1, 30)]
    for i, cyfra in enumerate(cyfry):
        print(i + 1, cyfra, file=wynik)


def czyZawieraLiczbePodzPrzez5(wiersz):
    for a in wiersz:
        if a % 5 == 0:
            return True
    return False


def zad5c(wynik):
    numery = [n if czyZawieraLiczbePodzPrzez5(trojkat(n)) else "" for n in range(1, 30)]
    print("c)", *numery, file=wynik)


def main():
    wyniki = open('wynik5.txt', 'w')
    zad5a(wyniki)
    zad5b(wyniki)
    zad5c(wyniki)


main()
