from collections import Counter


def get_2_najmniejsze_argumenty(slownik):
    slownikKopia = slownik.copy()
    min1 = min(slownikKopia, key=slownikKopia.get)
    wartosc1 = slownikKopia.get(min1)
    slownikKopia.pop(min1)
    min2 = min(slownikKopia, key=slownikKopia.get)
    wartosc2 = slownikKopia.get(min2)
    return (min1, min2), wartosc1 + wartosc2


def dodajDoWszystkichElementow(tablica, slownik, znak):
    for x in tablica:
        if type(x) == str:
            slownik[x] += znak
        else:
            dodajDoWszystkichElementow(x, slownik, znak)


def wypelnijSlownik(drzewo, slownik):
    for i, x in enumerate(drzewo):
        if type(x) == str:
            slownik[x] += str(i)
        elif type(x) == tuple:
            dodajDoWszystkichElementow(x, slownik, str(i))
            wypelnijSlownik(x, slownik)


def utworzSlownikCzestosciWystepowaniaLiter(probka):
    ilosci_liter = Counter(probka)
    prawdopodobienstwa = {}
    for a in ilosci_liter:
        prawdopodobienstwa[a] = ilosci_liter.get(a) / len(probka)
    return dict(prawdopodobienstwa)


def utworz_drzewo(probka):
    ilosci_liter = Counter(probka)
    prawdopodobienstwa = utworzSlownikCzestosciWystepowaniaLiter(probka)
    print(prawdopodobienstwa)
    for i in range(len(list(prawdopodobienstwa.keys())) - 1):
        wezel, suma_prawdop = get_2_najmniejsze_argumenty(prawdopodobienstwa)
        prawdopodobienstwa.pop(wezel[0])
        prawdopodobienstwa.pop(wezel[1])
        prawdopodobienstwa[wezel] = suma_prawdop
    litery = list(ilosci_liter.keys())
    slownik = {x: '' for x in litery}
    drzewo = list(prawdopodobienstwa.keys())[0]
    wypelnijSlownik(drzewo, slownik)
    return drzewo, slownik


def koduj_H(napis, slownik):
    return ''.join([slownik[x] for x in napis])


def dekoduj_H(napis, drzewo):
    napis_zdekodowany = ''
    pozycja_w_drzewie = drzewo
    for x in napis:
        pozycja_w_drzewie = pozycja_w_drzewie[int(x)]
        if type(pozycja_w_drzewie) == str:
            napis_zdekodowany += pozycja_w_drzewie
            pozycja_w_drzewie = drzewo
    return napis_zdekodowany


text = 'A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED'
drzewo, slownikLiter = utworz_drzewo(text)
print(drzewo)
zakodowany_tekst = koduj_H(text, slownikLiter)
print(zakodowany_tekst)
# print(dekoduj_H(zakodowany_tekst, drzewo))
