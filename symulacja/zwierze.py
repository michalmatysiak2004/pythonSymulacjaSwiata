import copy
from random import randint

from symulacja.organizm import Organizm
from wektor2d import Wektor2d


class Zwierze(Organizm):
    def __init__(self, polozenie: Wektor2d, sila: int, inicjatywa: int):
        super().__init__(polozenie, sila, inicjatywa)

    def kolizja(self):

        drugi = self._swiat.getKolidujacy(self)

        if drugi is None:
            return

        if str(drugi) == str(self):
            self._rozmnozSie(drugi)
            return

        self._walcz(drugi)

    def nowaTura(self):

        self._rozmnozylSie = False
    def losowyruch(self, zasieg: int):
        # dodac warunek czyMadobrywech i czy wszyzcy sasiedzi sa silniejsi

        kordynaty = [-1 * zasieg, 0, zasieg]
        wczesniejsze = Wektor2d(self._polozenie.getY(), self._polozenie.getX())

        while True:
            randx = kordynaty[randint(0, 2)]
            randy = kordynaty[randint(0, 2)]

            przemieszczenie = Wektor2d(randy, randx)
            self._zmienPolozenie(przemieszczenie)

            if not (wczesniejsze == self._polozenie or
                    (self.czyMaDobryWech() and
                    self._swiat.getKolidujacy(self) is not None and
                    self._swiat.getkolidujacy(self).getSila() > self.getSila(self))):
                break


    def akcja(self):
        self.losowyruch(1)

    def _zmienPolozenie(self, przemieszczenie):

        if not (self.getPolozenie() + przemieszczenie) \
                .pozaGranicami(self._swiat.getWysokosc(), self._swiat.getSzerokosc()):
            self._wczesniejszePolozenie = Wektor2d(self._polozenie.getY(), self._polozenie.getX())
            self._polozenie += przemieszczenie



    def _rozmnozSie(self, drugi):

        if drugi.getWiek() == 0:
            return

        org = copy.deepcopy(self)
        self.__cofnijSie()

        miejsceNarodzin = self._swiat.getWolnePoleObok(drugi.getPolozenie())

        if miejsceNarodzin == drugi.getPolozenie() or drugi._rozmnozylSie or self._rozmnozylSie:
            return


        org.setPolozenie(miejsceNarodzin)
        org.setWiek(-1)

        self._swiat.addOrganizm(org)


        self._rozmnozylSie = True
        drugi._rozmnozylSie = True



    def __cofnijSie(self):

        self.setPolozenie(self._wczesniejszePolozenie)

    def _walcz(self, drugi : Organizm):

        if self.ucieczka() or drugi.ucieczka():
            return

        if self.getSila() < drugi.getSila():

            if self.czyOdbilAtak(drugi):

                self.__cofnijSie()
                return

            self._swiat.getDziennik().wpisz(f"{str(drugi)} zjada {str(self)}")
            self.zabij()
            self.dodajModyfikator(drugi)

            return

        if drugi.czyOdbilAtak(self):

            self.__cofnijSie()
            return

        self._swiat.getDziennik().wpisz(f"{str(self)} zjada {str(drugi)}")
        drugi.zabij()
        drugi.dodajModyfikator(self)

    def wszyscySasiedziSilniejsi(self) -> bool:

        for y in range(-1,2):
            for x in range(-1,2):

                pol = Wektor2d(y,x)

                org = self._swiat.getOrganizmNaPozycji(self.getPolozenie() + pol)

                if org != self and (org is None or org.getSila() <= self.getSila()):

                    return False


        return True

