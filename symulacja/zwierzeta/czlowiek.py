from random import random

from wektor2d import Wektor2d
from symulacja.zwierze import Zwierze

from symulacja.swiat import Swiat


class Czlowiek(Zwierze):


    SILA = 5
    INICJATYWA = 4
    SPECJALNY_TURY = 5
    SPECJALNY_MNIEJ = 2
    P_MNIEJ = 0.5


    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Czlowiek.SILA, Czlowiek.INICJATYWA)
        self.__turySpecjalne = 0


    def akcja(self):

        zasieg = 1
        if self.__turySpecjalne > Czlowiek.SPECJALNY_MNIEJ or \
            (self.__turySpecjalne > 0 and random() < Czlowiek.P_MNIEJ):

            zasieg = 2


        self.__turySpecjalne -= 1
        self.__turySpecjalne = 0 if self.__turySpecjalne <= 0 else self.__turySpecjalne

        ruch = self._swiat.popRuch()

        if ruch == Swiat.Ruch.GORA:

            self._zmienPolozenie(Wektor2d(zasieg * -1, 0))

        elif ruch == Swiat.Ruch.DOL:

            self._zmienPolozenie(Wektor2d(zasieg, 0))

        elif ruch == Swiat.Ruch.LEWO:

            self._zmienPolozenie(Wektor2d(0, -1 * zasieg))

        elif ruch == Swiat.Ruch.PRAWO:

            self._zmienPolozenie(Wektor2d(0, zasieg))

        elif ruch == Swiat.Ruch.SPECJALNY:

            self.__turySpecjalne = Czlowiek.SPECJALNY_TURY if self.__turySpecjalne == 0 else self.__turySpecjalne


    def rysowanie(self) -> str:

        return "#FFFD96"


    def __str__(self):
        return "CZLOWIEK"

    def getTurySpecjalne(self):
        return self.__turySpecjalne

    def setTurySpecjalne(self, tury : int):
        self.__turySpecjalne = tury