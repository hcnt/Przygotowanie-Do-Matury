from collections import Counter


def main():
    anagram = open('anagram.txt')
    wyniki4a = open('odp_4a.txt', 'w')
    wyniki4b = open('odp_4b.txt', 'w')
    zad4a(anagram, wyniki4a)
    zad4b(anagram, wyniki4b)
    wyniki4a.close()
    wyniki4b.close()


def zad4a(plik, wynik):
    for line in plik:
        line = line.rstrip()
        wyrazy = line.split()
        dlugoscWyrazow = list(map(len, wyrazy))
        if all(dlugoscWyrazow[0] == x for x in dlugoscWyrazow):
            print(line, file=wynik)
    plik.seek(0)


def zad4b(plik, wynik):
    for line in plik:
        line = line.rstrip()
        wyrazy = line.split()
        litery = list(map(Counter, wyrazy))
        if all(litery[0] == x for x in litery):
            print(line, file=wynik)
    plik.seek(0)


main()
