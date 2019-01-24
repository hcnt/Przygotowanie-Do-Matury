def zad_a(slowa):
    hasla = []
    slowa.seek(0)
    hasla_a = open("hasla_a.txt", "w")
    for line in slowa:
        haslo = line.rstrip()[::-1]
        hasla.append(haslo)
        print(haslo, file=hasla_a)
        minHaslo = min(hasla, key=len)
        maxHaslo = max(hasla, key=len)
    print("najkrótsze haslo:", minHaslo, "długość:", len(minHaslo), file=hasla_a)
    print("najdłóższe haslo:", maxHaslo, "długość:", len(maxHaslo), file=hasla_a)
    slowa.seek(0)


def zad_b(slowa):
    hasla_b = open("hasla_b.txt", "w")
    hasla = []
    sumaDlogosci = 0
    haslaODlugosci12 = []
    for line in slowa:
        line = line.rstrip()
        anchor = znajdzNajdlozszyPalindrom(line)
        koncowka = line[len(anchor):]
        haslo = koncowka[::-1] + line
        sumaDlogosci += len(haslo)
        hasla.append(haslo)
        if len(haslo) == 12:
            haslaODlugosci12.append(haslo)
        print(haslo, file=hasla_b)
    minHaslo = min(hasla, key=len)
    maxHaslo = max(hasla, key=len)
    print("1.", file=hasla_b)
    print(*haslaODlugosci12,file=hasla_b)
    print("2.", file=hasla_b)
    print("najkrótsze haslo:", minHaslo, "długość:", len(minHaslo), file=hasla_b)
    print("najdłóższe haslo:", maxHaslo, "długość:", len(maxHaslo), file=hasla_b)
    print("3.", file=hasla_b)
    print(sumaDlogosci,file=hasla_b)


def znajdzNajdlozszyPalindrom(line):
    palindromy = []
    for i in range(len(line) + 1):
        if czyJestPalidromem(line[:i]):
            palindromy.append(line[:i])
    return max(palindromy, key=len)


def czyJestPalidromem(string):
    if string == string[::-1]:
        return True
    else:
        return False


# print(czyJestPalidromem("kajak"))  # t
# print(czyJestPalidromem("xddd"))  # f
# print(czyJestPalidromem("kaja"))  # f
# print(czyJestPalidromem("toppot"))  # t


def main():
    slowa = open("slowa.txt")
    test = open("testSlowa.txt")
    zad_a(slowa)
    zad_b(slowa)


main()
