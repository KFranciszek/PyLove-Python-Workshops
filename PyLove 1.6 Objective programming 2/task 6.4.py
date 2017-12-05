# Zaimplementuj metodę magiczną __str__, która wyświetli aktualne wartości np. <zeg h=0, m=3, s=5>


class Czas:
    def __init__(self, godzina, minuta, sekunda):
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda

    def __str__(self):
        print("<zeg h={}, m={}, s={}>".format(self.godzina, self.minuta, self.sekunda))


czas = Czas(15, 20, 15)
str(czas)