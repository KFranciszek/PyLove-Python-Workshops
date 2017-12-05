'''Zaimplementuj metodę pozwalającą zwiększyć czas o minutę, sekundę, godzinę, a w przypadku
Dokładnego Zegara dodatkowo milisekundy. Pamiętaj że przekraczając 60 minutę lub sekundę
powinna też odpowiednio zwiększyć odpowiednio godzinę lub minutę.
Przykład zeg = Zegar(0, 2, 45) zeg.add_time(second=20) print(zeg) >>> <zeg h=0, m=3, s=5>'''


class Czas:

    def __init__(self, godzina=0, minuta=0, sekunda=0):
        self._godzina = godzina
        self._minuta = minuta
        self._sekunda = sekunda

    def zwieksz_czas(self, minuta=0, sekunda=0, godzina=0):
        if self._sekunda + sekunda >= 60:
            self._minuta += (int(((self._sekunda + sekunda) / 60)))
            self._sekunda = (self._sekunda + sekunda) % 60
        else:
            self._sekunda += sekunda

        if self._minuta + minuta >= 60:
            self._godzina += (int(((self._minuta + minuta) / 60)))
            self._godzina = (self._minuta + minuta) % 60
        else:
            self._minuta += minuta

        if self._godzina + godzina > 24:
            self._godzina = (self._godzina + godzina) % 24
        else:
            self._godzina += godzina

class DokladnyZegar(Czas):
    def __init__(self, milisekunda=0, **kwargs):
        self._milisekunda = milisekunda
        super().__init__(**kwargs)

    def zwieksz_czas(self, milisekunda=0, **kwargs):
        if self._milisekunda + milisekunda >= 1000:
            self._sekunda += (int(((self._milisekunda + milisekunda) / 1000)))
            self._milisekunda = (self._milisekunda + milisekunda) % 1000
        else:
            self._milisekunda += milisekunda
        super().zwieksz_czas(**kwargs)