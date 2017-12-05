# Stwórz klasę DokładnyZegar, która dziedziczy po Zegar i która jeszcze będzie przyjmowała opcjonalnie milisekundy.


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



class DokladnyZegar(Zegar):
    def __init__(self, format1, godzina, minuta, sekunda, milisekundy=0):
        self.milisekundy = milisekundy
        super().__init__(format1, godzina, minuta, sekunda)
