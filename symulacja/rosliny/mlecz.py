from symulacja.roslina import Roslina
from inne.wektor2d import Wektor2d


class Mlecz(Roslina):
    SILA = 0

    PROBY = 3



    def __init__(self, polozenie: Wektor2d):
        super().__init__(polozenie, Mlecz.SILA)


    def akcja(self):
        for i in range(Mlecz.PROBY):
            self.rozsiej()


    def __str__(self):
        return "mlecz"




