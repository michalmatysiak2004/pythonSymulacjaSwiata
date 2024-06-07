import copy
from random import randint

from dziennik import Dziennik
from wektor2d import Wektor2d
from symulacja.organizm import Organizm
from enum import Enum

class Swiat:

    class Typ(Enum):
        KARTEZJANSKI = 0,
        HEX = 1

    class Ruch(Enum):
        GORA = 0
        DOL = 1
        LEWO = 2
        PRAWO = 3
        SPECJALNY = 4
        STOJ = 5

    def getTyp(self):
        return self.__typ
    def __init__(self, wysokosc: int, szerokosc: int, organizmy=None, typ = Typ.KARTEZJANSKI):

        if organizmy is None:
            organizmy = []
        else:
            for organizm in organizmy:
                organizm.setSwiat(self)

        self.__wysokosc = wysokosc
        self.__szerokosc = szerokosc
        self.__organizmy = organizmy
        self.__nrTury = 0
        self.__dziennik = Dziennik()
        self.__ruch = Swiat.Ruch.STOJ
        self.__typ = typ



    def getWysokosc(self):
        return self.__wysokosc

    def getSzerokosc(self):
        return self.__szerokosc

    def getDziennik(self):
        return self.__dziennik

    def getOrganizmNaPozycji(self, pozycja: Wektor2d) -> Organizm:

        szukany = None

        for organizm in self.__organizmy:

            if organizm.getPolozenie() == pozycja and organizm.isZywy():

                if szukany is None or szukany.getSila() < organizm.getSila():

                    szukany = organizm

        return szukany

    def wykonajTure(self):

        #self.__dziennik.czysc()

        for org in self.__organizmy:
            org.nowaTura()

        self.__nrTury+=1
        self.__ruchOrganizmow()

        self.__organizmy = [x for x in self.__organizmy if x.isZywy()] # pozbadz sie zwlok

    def addOrganizm(self, org: Organizm):
        org.setSwiat(self)
        self.__organizmy.append(org)

    def __ruchOrganizmow(self):


        self.__organizmy = sorted(self.__organizmy,reverse=True, key= lambda x: x.getWiek())
        self.__organizmy = sorted(self.__organizmy, reverse=True, key= lambda x: x.getInicjatywa())

        for org in self.__organizmy:

            if org.isZywy():

                org.akcja()
                org.kolizja()

            org.starzejSie()

    def getWolnePoleObok(self, p : Wektor2d, zasieg = 1):

        for dy in [-1 * zasieg, 0, zasieg]:

            for dx in [-1 * zasieg, 0, zasieg]:

                if self.__typ == Swiat.Typ.HEX and ( (dy == -1 and dx == -1) or (dy == 1 and dx == -1)):
                    continue

                punkt =  Wektor2d(dy,dx) + p

                if punkt != p \
                        and self.getOrganizmNaPozycji(punkt) is None \
                        and not punkt.pozaGranicami(self.getWysokosc(),self.getSzerokosc()):
                    return punkt

        return p

    def getLosoweWolnePoleObok(self, p : Wektor2d, zasieg = 1):

        punkty = []

        for dy in [-1 * zasieg, 0, zasieg]:

            for dx in [-1 * zasieg, 0, zasieg]:

                punkt =  Wektor2d(dy,dx) + p

                if punkt != p \
                        and self.getOrganizmNaPozycji(punkt) is None \
                        and not punkt.pozaGranicami(self.getWysokosc(),self.getSzerokosc()):
                    punkty.append(punkt)

        if len(punkty):
            return punkty[randint(0,len(punkty) - 1)]

        return None


    def getOrganizmy(self):

        return self.__organizmy


    def getKolidujacy(self, org):

        temp =  [x for x in self.__organizmy if x.getPolozenie() == org.getPolozenie() and x != org]

        if len(temp):
            return temp[0]

        return None

    def setRuch(self, ruch : Ruch):

        self.__ruch = ruch

    def popRuch(self):

        obecny = copy.deepcopy(self.__ruch)
        self.__ruch = Swiat.Ruch.STOJ

        return obecny

    def getRuch(self):

        return self.__ruch

    def getNrTury(self):
        return self.__nrTury

    def setNrTury(self, t):
        self.__nrTury = t