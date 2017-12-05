# Stwórz klasę Zegar, która dziedziczy po Czas
# a konstruktor (__init__) będzie brał obowiązkowo parametr format (12H lub 24H) oprócz tych co Czas.

class Czas:
    def __init__(self, godzina, minuta, sekunda):
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda


class Zegar(Czas):
    def __init__(self, format1, godzina, minuta, sekunda):
        if format1 == "12H" or format1 == "24H":
            self.format1 = format1
        else:
            print("Błędny format")
        super().__init__(godzina, minuta, sekunda)
