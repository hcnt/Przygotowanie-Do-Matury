def main():
    uczniowie = open("uczniowie.txt")
    oceny = open("oceny.txt")
    przedmioty = open("przedmioty.txt")
    wyniki = open("odp_6.txt", 'w')
    uczniowie.seek(1)
    oceny.seek(1)
    przedmioty.seek(1)
    zad6a(uczniowie, oceny, przedmioty, wyniki)


def zad6a(uczniowie, oceny, przedmioty, wyniki):
    liczbaUczniow = 0
    for uczen in uczniowie:
        uczen = uczen.rstrip()
        uczen = uczen.split(';')
        ulica = uczen[3]
        if ulica == "Worcella" or ulica == "Sportowa":
            liczbaUczniow += 1
    print("a)",liczbaUczniow,file=wyniki)


def zad6a(uczniowie, oceny, przedmioty, wyniki):
    liczbaUczniow = 0
    for uczen in uczniowie:
        uczen = uczen.rstrip()

main()
