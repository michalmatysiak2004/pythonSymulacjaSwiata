from symulacja.roslina import Roslina
from wektor2d import Wektor2d


class Guarana(Roslina):

    SILA = 0
    ZWIEKSZENIE_SILY = 3

    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Guarana.SILA)


    def dodajModyfikator(self, other):
        other.setSila(Guarana.ZWIEKSZENIE_SILY + other.getSila)


    def __str__(self):
        return "GUARANA"