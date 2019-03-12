def main():
    plik = open('NAPIS.TXT')
    wyniki = open('ZADANIE5.TXT')


def czyPierwsza(liczba):
    if liczba == 2:
        return True
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True



def zad5a(plik,wynik):
    for linia in plik:
        linia

