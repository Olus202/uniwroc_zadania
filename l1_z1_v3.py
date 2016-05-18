# Zadanie z listy zadań kursu 'Rozszerzony kurs języka Python' prowadzonego na Uniwersytecie Wrocławskim.
# Lista 1 - zadanie 1

# Wersja 3 - obiektowa + poprawki

import random

class Player(object):
    """Klasa gracza"""
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.zwyciestwa = 0
        self.porazki = 0
        self.ranking = [nazwa, ["Zwyciestwa", self.zwyciestwa], ["Porazki", self.porazki]]

    def rzut_kostka(self):
        self.rzut1 = random.randint(1, 6)
        self.rzut2 = random.randint(1, 6)
        self.suma = self.rzut1 + self.rzut2
#        return self.rzut1, self.rzut2, self.suma

def main():

    tury = int(input("Wprowadz liczbe tur: "))

    gracz1 = Player("Gracz 1")
    gracz2 = Player("Gracz 2")

    for tura in range(1, tury + 1):

        gracz1.rzut_kostka()
        gracz2.rzut_kostka()

        print("\nTura:", tura)
        print(gracz1.nazwa, "- Rzut 1:", gracz1.rzut1, "- Rzut 2:", gracz1.rzut1, "- Suma:", gracz1.suma)
        print(gracz2.nazwa, "- Rzut 1:", gracz2.rzut1, "- Rzut 2:", gracz2.rzut2, "- Suma:", gracz2.suma)

        if gracz1.suma > gracz2.suma:
            print("\nWygral gracz 1\n")
            gracz1.zwyciestwa += 1
            gracz2.porazki += 1
        elif gracz1.suma < gracz2.suma:
            print("\nWygral gracz 2\n")
            gracz2.zwyciestwa += 1
            gracz1.porazki += 1
        else:
            print("\nRemis\n")

        gracz1.ranking[1][1] = gracz1.zwyciestwa
        gracz2.ranking[1][1] = gracz2.zwyciestwa
        gracz1.ranking[2][1] = gracz1.porazki
        gracz2.ranking[2][1] = gracz2.porazki

        print("Ranking ogolny:")
        print(gracz1.ranking)
        print(gracz2.ranking)
        print("\n--------------------------------")

    if gracz1.zwyciestwa > gracz2.zwyciestwa:
        print("\nGre wygral gracz 1\n")
    elif gracz1.zwyciestwa < gracz2.zwyciestwa:
        print("\nGre wygral gracz 2\n")
    else:
        print("\nDogrywka do pierwszego zwyciestwa!\n")
        dogrywka()

def dogrywka():

    Gracz1 = Player("Gracz 1")
    Gracz2 = Player("Gracz 2")

    while True:

        Gracz1.rzut_kostka()
        Gracz2.rzut_kostka()

        print(Gracz1.nazwa, "- Rzut 1:", Gracz1.rzut1, "- Rzut 2:", Gracz1.rzut1, "- Suma:", Gracz1.suma)
        print(Gracz2.nazwa, "- Rzut 1:", Gracz2.rzut1, "- Rzut 2:", Gracz2.rzut2, "- Suma:", Gracz2.suma)

        if Gracz1.suma > Gracz2.suma:
            print("\nWygral gracz 1!\n")
            break
        elif Gracz1.suma < Gracz2.suma:
            print("\nWygral gracz 2!\n")
            break
        else:
            print("\nKolejna tura\n")
#            continue

main()