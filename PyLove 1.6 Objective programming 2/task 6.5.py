# Zaimplementuj metodę set_time, która pozwoli nadpisać aktualne wartości czasu.


class Czas:

    def __init__(self, godzina, minuta, sekunda):
        self._godzina = godzina
        self._minuta = minuta
        self._sekunda = sekunda

    def set_time(self, godzina, minuta, sekunda):
        self._godzina = godzina
        self._minuta = minuta
        self._sekunda = sekunda