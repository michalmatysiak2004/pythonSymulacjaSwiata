from random import random

from inne.wektor2d import Wektor2d
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
        if(self.__turySpecjalne > 0):
            self.getSwiat().getDziennik().wpisz({"Pozostałe tury specjalne: " +  str(self.__turySpecjalne)})

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

            if(self.__turySpecjalne == 0):
                self.__turySpecjalne = Czlowiek.SPECJALNY_TURY
                self.getSwiat().getDziennik().wpisz({"aktywowano umiejestnosc specjalna"})


    def rysowanie(self) -> str:
        return "FFFFFF"


    def __str__(self):
        return "czlowiek"

    def getTurySpecjalne(self):
        return self.__turySpecjalne

    def setTurySpecjalne(self, tury : int):
        self.__turySpecjalne = tury