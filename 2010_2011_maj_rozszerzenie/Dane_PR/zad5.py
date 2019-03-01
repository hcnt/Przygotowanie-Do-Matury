import datetime as dt

def main():
    wynik = open("zadanie4.txt","w")
    zad_a(wynik)
    # zad_b()

def zad_a(wyniki):
    data = dt.date(2011,4,1)
    data += dt.timedelta(days=1)
    print(data)

main()