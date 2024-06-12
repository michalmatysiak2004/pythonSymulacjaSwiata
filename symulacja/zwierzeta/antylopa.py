from symulacja.zwierze import Zwierze
from inne.wektor2d import Wektor2d


class Antylopa(Zwierze):
    INICJATYWA = 4
    SILA = 4

    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie,Antylopa.SILA, Antylopa.INICJATYWA)


    def akcja(self):
        self.losowyruch(2)


    def __str__(self):
        return "antylopa"
    def rysowanie(self) -> str:
        return "XD"
