from symulacja.organizm import Organizm
from symulacja.roslina import Roslina
from inne.wektor2d import Wektor2d
from symulacja.zwierze import Zwierze
class Barszcz_sosnowskiego(Roslina):
    SILA = 10
    def __init__ (self,polozenie : Wektor2d):
        super().__init__(polozenie, Barszcz_sosnowskiego.SILA)

    def akcja(self):

        for y in range(-1, 2):

            for x in range(-1, 2):

                org = self._swiat.getOrganizmNaPozycji(self.getPolozenie() + Wektor2d(y, x))

                if isinstance(org, Zwierze) and not org.isOdpornyNaToksyny():
                    org.zabij()

        super().akcja()


    def __str__(self):
        return "barszcz_sosnowskiego"