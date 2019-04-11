import pprint
from copy import deepcopy


def main():
    a, b = 5, 5
    x = [[0 for i in range(a)] for j in range(b)]
    x[2][2] = 1
    x[2][3] = 1
    # pprint.pprint(x)
    gol(x,4)


def gol(tab, steps):
    pprint.pprint(tab)
    for i in range(steps):
        tab = golStep(tab)
        print()
        pprint.pprint(tab)


def golStep(tab):
    tabCopy = deepcopy(tab)
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tabCopy[i][j] = determineCellState(tab, i, j)
    return tabCopy


def determineCellState(tab, a, b):
    neighbours = []
    for i in range(a - 1, a + 2):
        for j in range(b - 1, b + 2):
            try:
                if i != a or j != b:
                    neighbours.append(tab[i][j])
            except IndexError:
                pass
    if sum(neighbours) == 2 or sum(neighbours) == 3:
        return 1
    else:
        return 0


main()
