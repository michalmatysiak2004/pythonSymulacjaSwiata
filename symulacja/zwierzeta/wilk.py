from inne.wektor2d import Wektor2d
from symulacja.zwierze import Zwierze



class Wilk(Zwierze):

    INICJATYWA = 5
    SILA = 9


    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Wilk.SILA, Wilk.INICJATYWA)


    def __str__(self):
        return "wilk"


    def rysowanie(self) -> str:
        return "red"