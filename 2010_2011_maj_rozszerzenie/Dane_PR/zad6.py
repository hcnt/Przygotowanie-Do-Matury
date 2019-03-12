def main():
    dane = open('liczby.txt')
    wyniki = open('zadanie6.txt', 'w')
    zad6a(dane, wyniki)
    zad6b(dane, wyniki)
    zad6c(dane, wyniki)


def zad6a(dane, wyniki):
    parzyste = 0
    for line in dane:
        line = line.rstrip()
        liczba = int(line, 2)
        if liczba % 2 == 0:
            parzyste += 1

    print("a)", parzyste, file=wyniki)
    dane.seek(0)


def zad6b(dane, wyniki):
    tab = [int(linia.rstrip(), 2) for linia in dane]
    maxliczba = max(tab)
    maxliczbabin = bin(maxliczba)
    print("b)", "dziesiętny:", maxliczba, ",dwójokwy:", maxliczbabin[2:], file=wyniki)
    dane.seek(0)



def zad6c(dane, wyniki):
    liczba = 0
    suma = 0
    for line in dane:
        line = line.rstrip()
        if len(line) == 9:
            liczba += 1
            suma += int(line, 2)
    print("c)", "liczba:", liczba, ",suma:", bin(suma)[2:], file=wyniki)



main()

