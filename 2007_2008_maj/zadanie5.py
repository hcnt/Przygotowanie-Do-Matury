def zad_a(slowa):
    maxHaslo = ""
    minHaslo = slowa.getline().rstrip()
    slowa.seek(0)
    hasla_a = open("hasla_a.txt", "w")
    for line in slowa:
        print(line.rstrip()[::-1], file=hasla_a)
    slowa.seek(0)


def zad_b(slowa):
    hasla_b = open("hasla_b.txt", "w")
    for line in slowa:
        line = line.rstrip()
        anchor = znajdzNajdlozszyPalindrom(line)
        koncowka = line[len(anchor):]
        haslo = koncowka[::-1] + line
        print(haslo, file=hasla_b)


def znajdzNajdlozszyPalindrom(line):
    palindromy = []
    for i in range(len(line) + 1):
        if czyJestPalidromem(line[:i]):
            palindromy.append(line[:i])
    return max(palindromy)


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
