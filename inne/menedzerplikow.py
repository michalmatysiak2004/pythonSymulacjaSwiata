
from symulacja.swiat import Organizm
from symulacja.zwierzeta.czlowiek import Czlowiek
from symulacja.zwierzeta.wilk import Wilk
from symulacja.zwierzeta.owca import Owca
from symulacja.zwierzeta.lis import Lis
from symulacja.zwierzeta.antylopa import Antylopa
from symulacja.zwierzeta.zolw import Zolw
from symulacja.rosliny.guarana import Guarana
from symulacja.rosliny.mlecz import Mlecz
from symulacja.rosliny.trawa import Trawa
from symulacja.rosliny.barszcz_sosnowskiego import Barszcz_sosnowskiego
from symulacja.rosliny.wilcze_jagody import Wilcze_Jagody
from symulacja.swiat import Swiat
from symulacja.organizm import Organizm
from symulacja.zwierzeta.czlowiek import Czlowiek
from inne.wektor2d import Wektor2d
import copy
from symulacja.zwierzeta.cyberowca import Cyberowca
class MenedzerPlikow:

    def zapisz(self, swiat: Swiat, name: str):

        with open(name, "w") as out:

            out.write(f"{swiat.getNrTury()} {swiat.getWysokosc()} {swiat.getSzerokosc()} \n")

            for org in swiat.getOrganizmy():

                out.write(f"{str(org)} {org.getWiek()} {org.getPolozenie().getY()} {org.getPolozenie().getX()}")

                if isinstance(org, Czlowiek):
                    out.write(f" {org.getTurySpecjalne()}")

                out.write("\n")

    def wczytaj(self, name):

        try:

            with open(name, "r") as input:

                r = input.read().split("\n")

                r = [el for el in r if el != ""]

                t, h, w, typ = [el for el in r[0].split(" ")]

                sw = Swiat(int(h), int(w), None)
                sw.setNrTury(int(t))


                for i in range(1, len(r)):
                    org = self.__wczytajOrganizm(r[i])

                    sw.addOrganizm(org)

                return sw


        except:

            return None

    def __wczytajOrganizm(self, line: str) -> Organizm:

        args = line.split(" ")

        org = self.__alokujPoNazwie(args[0])

        if org is None:
            raise Exception

        org.setWiek(int(args[1]))
        org.setPolozenie(Wektor2d(int(args[2]),int(args[3])))

        if isinstance(org, Czlowiek):
            org.setTurySpecjalne(int(args[4]))

        return org

    def __alokujPoNazwie(self, nazwa: str):

        p0 = Wektor2d(0, 0)

        organizmy = [
            Czlowiek(p0),
            Wilk(p0),
            Owca(p0),
            Lis(p0),
            Zolw(p0),
            Antylopa(p0),
            Trawa(p0),
            Mlecz(p0),
            Guarana(p0),
            Wilcze_Jagody(p0),
            Barszcz_sosnowskiego(p0),
            Cyberowca(p0)

        ]

        for org in organizmy:

            if str(org) == nazwa:

                return copy.deepcopy(org)


        return None