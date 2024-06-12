from inne.wektor2d import Wektor2d
from symulacja.zwierze import Zwierze
from symulacja.organizm import Organizm
from symulacja.rosliny.barszcz_sosnowskiego import Barszcz_sosnowskiego

class Cyberowca(Zwierze):
    SILA = 11
    INICJATYWA = 4

    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie,Cyberowca.SILA,Cyberowca.INICJATYWA)


    def akcja(self):
        barszcze = [organizm for organizm in self.getSwiat().getOrganizmy() if isinstance(organizm, Barszcz_sosnowskiego)]

        if barszcze:
            najblizszy= min(barszcze, key=lambda b: abs(b.getPolozenie().getX() - self.getPolozenie().getX()) + abs(b.getPolozenie().getY()) - self.getPolozenie().getY())
            x = najblizszy.getPolozenie().getX()
            y = najblizszy.getPolozenie().getY()

            if self.getPolozenie().getX() < x:
                move_x = 1
            elif self.getPolozenie().getX() > x:
                move_x = -1
            else:
                move_x = 0


            if self.getPolozenie().getY() < y:
                move_y = 1
            elif self.getPolozenie().getX() > y:
                move_y = -1
            else:
                move_y = 0

            przemieszczenie = Wektor2d(move_y, move_x)
            self._zmienPolozenie(przemieszczenie)




    def isOdpornyNaToksyny(self) -> bool:
        return True



    def __str__(self):
        return "cyberowca"



