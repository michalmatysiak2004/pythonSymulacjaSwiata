from symulacja.roslina import Roslina
from inne.wektor2d import Wektor2d
from symulacja.organizm import Organizm
class Wilcze_Jagody(Roslina):
    SILA = 0

    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Wilcze_Jagody.SILA)

    def dodajModyfikator(self, other: Organizm):
        other.zabij()


    def __str__(self):
        return "wilcze_jagody"

    def rysowanie(self) -> str:
        return "XD"