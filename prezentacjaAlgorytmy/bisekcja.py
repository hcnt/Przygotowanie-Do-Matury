def bisekcja(f, a, b, d):
    while abs(b - a) > d:
        x = (a + b) / 2
        if f(x) == 0:
            return x
        elif f(x) * f(a) < 0:
            b = x
        elif f(x) * f(b) < 0:
            a = x
    return a


def funkcja(x):
    # x^2 - 6x + 8
    # miejsca zerowe: 2 i 4
    return x * x - 6 * x + 8


print(bisekcja(funkcja, -2, 3, 0.0001))

print(bisekcja(funkcja, 3, 6, 0.0001))
