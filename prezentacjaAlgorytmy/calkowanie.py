import random as rand


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
    return x ** 2


print(prostokaty(funkcja, 0, 4, 10))
print(trapezy(funkcja, 0, 4, 10))
print(monteCarlo(funkcja, 0, 4, 10000))
