import copy
from random import random

from wektor2d import Wektor2d
from organizm import Organizm


class Roslina(Organizm):
    DOMYSLNA_INICJATYWA = 0
    P_ROZSIANIA = 0.05

    def __init__(self, polozenie: Wektor2d, sila: int):
        super().__init__(polozenie, sila, Roslina.DOMYSLNA_INICJATYWA)

    def akcja(self):

        self.rozsiej()

    def kolizja(self):

        pass

    def nowaTura(self):

        pass

    def rozsiej(self):

        if random() >= Roslina.P_ROZSIANIA:
            return

        pNowy = self._swiat.getLosoweWolnePoleObok(self.getPolozenie())

        if pNowy is None:
            return

        org = copy.deepcopy(self)

        org.setWiek(0)
        org.setPolozenie(pNowy)

        self._swiat.addOrganizm(org)
