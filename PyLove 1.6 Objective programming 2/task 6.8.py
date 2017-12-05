# Zaimplementuj metodę get_minutes(), która zwróci dokładną wartość minut całego czasu (sekundy jako ułamek)


class Czas:
    def __init__(self, godzina=0, minuta=0, sekunda=0):
        self._godzina = godzina
        self._minuta = minuta
        self._sekunda = sekunda

    def get_minutes(self):
        return round(self._sekunda / 60, 3) + self._minuta + self._godzina * 60


czas = Czas(godzina = 10, minuta = 10, sekunda = 10)
print(czas.get_minutes())