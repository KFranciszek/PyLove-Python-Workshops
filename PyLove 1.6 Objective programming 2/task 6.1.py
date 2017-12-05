# Stwórz klasę Czas,
# której konstruktor (__init__) będzie brał trzy opcjonalne argumenty,
# godzine, minuty, sekundy i zapisywal je w odpowiednich zmiennych w klasie.


class Czas:
    def __init__(self, godzina, minuta, sekunda):
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda