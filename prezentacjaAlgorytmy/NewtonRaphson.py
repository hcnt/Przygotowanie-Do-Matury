def pierwiastek(x, epsilon):
    a, b = 1, x
    while abs(a - b) > epsilon:
        a = (a + b) / 2
        b = x / a
    return a



