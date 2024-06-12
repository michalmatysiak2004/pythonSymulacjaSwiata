from inne.wektor2d import Wektor2d
from symulacja.zwierze import Zwierze
import random
from symulacja.organizm import Organizm


class Zolw(Zwierze):
    SILA = 2
    INICJATYWA = 1
    P_RUCHU = 0.25

    OBRONA = 5

    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Zolw.SILA, Zolw.INICJATYWA)

    def __str__(self):
        return "zolw"

    def akcja(self):
        if random.random() < self.P_RUCHU:
            self.losowyruch(1)

    def czyOdbilAtak(self, other: Organizm) -> bool:
        return other.getSila() < Zolw.OBRONA
