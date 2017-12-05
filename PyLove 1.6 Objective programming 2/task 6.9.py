# Zaimplementuj metodę get_hours(), która zwróci dokładną wartość godzin całego czasu (sekundy, minuty jako ułamek)


class Czas:
    def __init__(self, godzina=0, minuta=0, sekunda=0):
        self._godzina = godzina
        self._minuta = minuta
        self._sekunda = sekunda

    def get_hours(self):
        return round(self._sekunda / 3600, 3) + round(self._minuta / 60, 3) + self._godzina


czas = Czas(godzina = 10, minuta = 10, sekunda = 10)
print(czas.get_hours())