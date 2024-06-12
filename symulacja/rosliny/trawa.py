from symulacja.roslina import Roslina
from inne.wektor2d import Wektor2d


class Trawa(Roslina):
    SILA = 0;

    def __init__(self, polozenie : Wektor2d ):
        super().__init__(polozenie, Trawa.SILA)


    def __str__(self):
        return "trawa"