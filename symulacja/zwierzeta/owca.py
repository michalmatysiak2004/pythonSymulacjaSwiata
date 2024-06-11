from wektor2d import Wektor2d
from symulacja.zwierze import Zwierze


class Owca(Zwierze):
    INICJATYWA = 4
    SILA = 4

    def __init__(self,polozenie: Wektor2d):
        super().__init__(polozenie,Owca.SILA, Owca.INICJATYWA)


    def __str__ (self):
        return "OWCA"