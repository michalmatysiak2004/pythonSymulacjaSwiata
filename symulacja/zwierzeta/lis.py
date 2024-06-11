from symulacja.zwierze import Zwierze
from wektor2d import Wektor2d

class Lis(Zwierze):
    INICJATYWA = 7
    SILA = 3


    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Lis.SILA, Lis.INICJATYWA)



    def CzyMaDobryWech(self):
        return True



    def __str__(self):
        return "LIS"