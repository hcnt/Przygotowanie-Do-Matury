def horner(x, tablica):
    wsp = [tablica[0]]
    for i in range(1, len(tablica)):
        wsp.append(x * wsp[-1] + tablica[i])
    return wsp


print(horner(-2, [1, 4, 4]))


def hornerZamianaNaDziesietny(system, liczba):
    liczba = list(map(int, liczba))
    return horner(system, liczba)[-1]


print(hornerZamianaNaDziesietny(2, '10101'))
