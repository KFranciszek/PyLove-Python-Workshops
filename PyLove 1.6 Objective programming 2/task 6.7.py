# Zaimplementuj metodę get_seconds(), która zwróci dokładną wartość sekund całego czasu.


class Czas:
    def __init__(self, godzina=0, minuta=0, sekunda=0):
        self._godzina = godzina
        self._minuta = minuta
        self._sekunda = sekunda

    def get_seconds(self):
        return self._sekunda + self._minuta * 60 + self._godzina * 3600


czas = Czas(godzina = 10, minuta = 10, sekunda = 10)
print(czas.get_seconds())