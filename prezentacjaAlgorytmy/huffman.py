from collections import Counter


def get_2_najmniejsze_argumenty(slownik):
    slownikKopia = slownik.copy()
    min1 = min(slownikKopia, key=slownikKopia.get)
    wartosc1 = slownikKopia.get(min1)
    slownikKopia.pop(min1)
    min2 = min(slownikKopia, key=slownikKopia.get)
    wartosc2 = slownikKopia.get(min2)
    return (min1, min2), wartosc1 + wartosc2


# get_2_najmniejsze_argumenty(


def stworzSlownik(drzewo, slownik):
    if type(drzewo[0]) == str:
        slownik[drzewo[0]] += '0'
    elif type(drzewo[0]) == tuple:
        slownik[drzewo[0]] += '0'
        stworzSlownik(drzewo[0], slownik)

    if type(drzewo[1]) == str:
        slownik[drzewo[1]] += '1'
    elif type(drzewo[0]) == tuple:
        slownik[drzewo[1]] += '1'
        stworzSlownik(drzewo[1], slownik)


def utworz_drzewo(probka):
    ilosci_liter = Counter(probka)
    # prawdopodobienstwa = map(lambda a: ilosci_liter.get(a) / len(text), ilosci_liter)
    prawdopodobienstwa = {}
    for a in ilosci_liter:
        prawdopodobienstwa[a] = ilosci_liter.get(a) / len(probka)
    print(dict(prawdopodobienstwa))
    for i in range(len(list(prawdopodobienstwa.keys())) - 1):
        wezel, suma_prawdop = get_2_najmniejsze_argumenty(prawdopodobienstwa)
        prawdopodobienstwa.pop(wezel[0])
        prawdopodobienstwa.pop(wezel[1])
        prawdopodobienstwa[wezel] = suma_prawdop
    return list(prawdopodobienstwa.keys())[0]


drzewo = utworz_drzewo('PIEEES')
slownik = {}
slownik.setdefault('')

print(stworzSlownik(drzewo, slownik))
print(slownik)
