
from abc import ABC, abstractmethod

from inne.wektor2d import Wektor2d


class Organizm(ABC):


    def __init__(self, polozenie : Wektor2d, sila : int, inicjatywa : int):

        self._polozenie = polozenie
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._zywy = True
        self._wiek = 0



    def getPolozenie(self):

        return self._polozenie


    def setPolozenie(self, polozenie: Wektor2d):

        self._polozenie = polozenie


    def getInicjatywa(self):

        return self._inicjatywa


    def getSila(self):

        return self._sila


    def setSila(self, sila : int):

        self._sila = sila


    def getWiek(self):

        return self._wiek

    def setWiek(self, wiek: int):

        self._wiek = wiek


    def isZywy(self) -> bool:

        return self._zywy


    def zabij(self):

        self._swiat.getDziennik().wpisz(f"{str(self)} umiera")
        self._zywy = False


    def dodajModyfikator(self, other):

        pass


    def czyOdbilAtak(self,other) -> bool:

        return False

    def isOdpornyNaToksyny(self) -> bool:

        return False


    def czyUciekl(self) -> bool:

        return False

    def ucieczka(self) -> bool:

        if self.czyUciekl():

            nowePole = self._swiat.getWolnePoleObok(self._polozenie)

            if nowePole == self._polozenie:

                return False

            self.setPolozenie(nowePole)

            return True

        return False



    def czyMaDobryWech(self):

        return False


    def starzejSie(self):

        self._wiek+=1


    def setSwiat(self, swiat):

        self._swiat = swiat
    def getSwiat(self):
        return self._swiat
    @abstractmethod
    def __str__(self):
        pass


    @abstractmethod
    def akcja(self):

        pass


    @abstractmethod
    def kolizja(self):

        pass





    @abstractmethod
    def nowaTura(self):

        pass
