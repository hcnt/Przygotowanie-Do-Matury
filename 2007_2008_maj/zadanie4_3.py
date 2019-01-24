dane = open('dane.txt')
wynik = open("wynik.txt", 'w')

wszystkieGlosy = []
mandatyWOkregu = []

for line in dane:
    line = line.rstrip().split()
    wszystkieGlosy.append(list(map(int, line[:-1])))
    mandatyWOkregu.append(int(line[-1]))


def zliczMandaty(glosyWOkregu, iloscMandatow):
    mandaty = [0, 0, 0, 0, 0, 0]
    startoweGlosy = glosyWOkregu.copy()
    for i in range(iloscMandatow):
        for j in range(len(glosyWOkregu)):
            glosyWOkregu[j] = startoweGlosy[j] / (mandaty[j] + 1)
        mandaty[glosyWOkregu.index(max(glosyWOkregu))] += 1
    return mandaty


glosy6 = zliczMandaty(wszystkieGlosy[5], mandatyWOkregu[5])

print('zad 3 - liczba glosow w 6 okregu',
      '; '.join(['{0}: {1}'.format(a, b) for (a, b) in zip(['A', 'B', 'C', 'D', 'E', 'F'], glosy6)]), file=wynik)




def wszystkieMandaty():
    suma = [0, 0, 0, 0, 0, 0]
    for glosy, limitMandatow in zip(wszystkieGlosy, mandatyWOkregu):
        mandaty = zliczMandaty(glosy, limitMandatow)
        suma = [a + b for a, b in zip(suma, mandaty)]

    print('zad 4 - suma glosow we wszystkich okregach',
          '; '.join(['{0}: {1}'.format(a, b) for (a, b) in zip(['A', 'B', 'C', 'D', 'E', 'F'], suma)]), file = wynik)


wszystkieMandaty()
