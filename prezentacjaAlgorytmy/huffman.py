from collections import Counter


def get_2_najmniejsze_argumenty(slownik):
    slownikKopia = slownik.copy()
    min1 = min(slownikKopia, key=slownikKopia.get)
    wartosc1 = slownikKopia.get(min1)
    slownikKopia.pop(min1)
    min2 = min(slownikKopia, key=slownikKopia.get)
    wartosc2 = slownikKopia.get(min2)
    return (min2, min1), wartosc1 + wartosc2


def dodajDoWszystkichElementow(tablica, slownik, znak):
    for x in tablica:
        if type(x) == str:
            slownik[x] += znak
        else:
            dodajDoWszystkichElementow(x, slownik, znak)


def wypelnijSlownik(drzewo,slownik):
    for i, x in enumerate(drzewo):
        if type(x) == str:
            slownik[x] += str(i)
        elif type(x) == tuple:
            dodajDoWszystkichElementow(x, slownik, str(i))
            wypelnijSlownik(x, slownik)

def utworz_drzewo(probka):
    ilosci_liter = Counter(probka)
    prawdopodobienstwa = {}
    for a in ilosci_liter:
        prawdopodobienstwa[a] = ilosci_liter.get(a) / len(probka)
    print(dict(prawdopodobienstwa))
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


drzewo, slownikLiter = utworz_drzewo('PIEEES')
zakodowany_pies = koduj_H('PIEEES', slownikLiter)
print(zakodowany_pies)
print(dekoduj_H(zakodowany_pies, drzewo))
