import random as rand
import matplotlib.pyplot as plt
import matplotlib.axes as axes


def prostokaty(f, a, b, n):
    suma = 0
    dx = abs(a - b) / n
    x = a
    for i in range(n):
        suma += f(x + (dx / 2)) * dx
        x += dx
    return suma


def trapezy(f, a, b, n):
    suma = 0
    dx = abs(a - b) / n
    x = a
    for i in range(n):
        suma += ((f(x) + f(x + dx)) / 2) * dx
        x += dx
    return suma


def monteCarlo(f, a, b, n):
    suma = 0
    d = abs(a - b)
    for i in range(n):
        suma += f(rand.uniform(a, b))
    sredniaWartoscFunkcji = suma / n
    pole = sredniaWartoscFunkcji * d
    return pole


def funkcja(x):
    return (6 * x ** 3) + (3 * x ** 2) - (16 * x) + 12


def wykres():
    dolnaGranica = 1
    gornaGranica = 200
    wynik = prostokaty(funkcja, dolnaGranica, gornaGranica, 5000)
    wynikiProstokaty = []
    wynikiTrapezy = []
    wynikiMonteCarlo = []
    a,b = 1, 11
    for i in range(a, b):
        # print(i)
        wynikiProstokaty.append(prostokaty(funkcja, dolnaGranica, gornaGranica, i))
        wynikiTrapezy.append(trapezy(funkcja, dolnaGranica, gornaGranica, i))
        # wynikiMonteCarlo.append(monteCarlo(funkcja, dolnaGranica, gornaGranica, i))
    bledyProstokaty = [(abs(a - wynik) / abs(wynik)) for a in wynikiProstokaty]
    bledyTrapezy = [(abs(a - wynik) / abs(wynik))  for a in wynikiTrapezy]
    bledyMonteCarlo = [(abs(a - wynik) / abs(wynik)) for a in wynikiMonteCarlo]
    print(bledyProstokaty)
    print(bledyTrapezy)
    print(bledyMonteCarlo)
    plt.title("Porównanie metod całkowania")
    plt.xlabel('liczba przedziałów')
    plt.ylabel('błąd wzgłedny')
    x = range(a, b)
    plt.plot(x, bledyTrapezy, label='metoda trapezów')
    plt.plot(x, bledyProstokaty, label='metoda prostokatów')
    # plt.plot(x, bledyMonteCarlo, label='monte carlo')
    plt.legend()
    plt.show()


# print(prostokaty(funkcja, 0, 4, 10))
# print(trapezy(funkcja, 0, 4, 10))
# print(monteCarlo(funkcja, 0, 4, 10000))
wykres()
