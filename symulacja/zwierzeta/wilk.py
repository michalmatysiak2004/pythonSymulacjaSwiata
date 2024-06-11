from wektor2d import Wektor2d
from symulacja.zwierze import Zwierze



class Wilk(Zwierze):

    INICJATYWA = 4
    SILA = 9


    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Wilk.SILA, Wilk.INICJATYWA)


    def __str__(self):
        return "WILK"


    def rysowanie(self) -> str:
        return "red"