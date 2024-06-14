import copy
import math
from tkinter import *
from symulacja.organizm import Organizm
from inne.wektor2d import Wektor2d
from symulacja.zwierzeta.czlowiek import Czlowiek
from symulacja.swiat import Swiat
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
import random
from symulacja.zwierzeta.cyberowca import Cyberowca
from PIL import Image, ImageTk
class Wizualizacja(Canvas):

    __KOLOR_TLA = "white"

    def __init__(self, master, wysokoscOkienka: int, swiat: Swiat):
        self.__wysokoscOkienka = wysokoscOkienka
        self.__wysokosc = swiat.getWysokosc()
        self.__szerokosc = swiat.getSzerokosc()

        self.__swiat = swiat

        self.__rozmiarZwierzecia = 50
        self.__images = {}
        super().__init__(master, height=wysokoscOkienka, width=self.__rozmiarZwierzecia * self.__szerokosc)

        self.__eventy()

        self.focus_set()

        self.pack()

    def paint(self):
        self.create_rectangle(0, 0, self.__rozmiarZwierzecia * self.__szerokosc, self.__rozmiarZwierzecia * self.__wysokosc, fill=Wizualizacja.__KOLOR_TLA)
        self.__draw_cartesian()

        if self.__maCzlowieka():
            self.czlowiekInfo()

    def __load_images(self):
        nazwy_organizmow = [
            "czlowiek", "wilk", "owca", "antylopa", "wilcze_jagody",
            "lis", "guarana", "barszcz_sosnowskiego", "trawa", "mlecz", "zolw", "cyberowca"
        ]
        for nazwa in nazwy_organizmow:
            image_path = f"C:/Users/polsk/PycharmProjects/pythonProject/gui/zdjecia/{nazwa}.png"
            image = Image.open(image_path)  # Otwórz obraz za pomocą PIL
            image = image.resize((self.__rozmiarZwierzecia, self.__rozmiarZwierzecia))

            self.__images[nazwa] = ImageTk.PhotoImage(image)  # Konwertuj obraz do formatu obsługiwanego przez tkinter
    def __draw_cartesian(self):
        self.__load_images()  # Load images before drawing

        for y in range(self.__wysokosc):
            for x in range(self.__szerokosc):
                org = self.__swiat.getOrganizmNaPozycji(Wektor2d(y, x))

                x1 = x * self.__rozmiarZwierzecia
                y1 = y * self.__rozmiarZwierzecia
                x2 = x1 + self.__rozmiarZwierzecia
                y2 = y1 + self.__rozmiarZwierzecia

                # Draw the border for each cell
                self.create_rectangle(x1, y1, x2, y2, outline="black")

                if org is not None:
                    image_path = org.__str__()
                    if image_path in self.__images:
                        image = self.__images[image_path]

                        self.create_image(x1, y1, anchor='nw', image=image)


    def __eventy(self):
        def klik(event):
            self.__initPopup(event)

        def klawisz(event):
            if event.keysym == "Up":
                self.__swiat.setRuch(Swiat.Ruch.GORA)
            elif event.keysym == "Down":
                self.__swiat.setRuch(Swiat.Ruch.DOL)
            elif event.keysym == "Left":
                self.__swiat.setRuch(Swiat.Ruch.LEWO)
            elif event.keysym == "Right":
                self.__swiat.setRuch(Swiat.Ruch.PRAWO)
            elif event.keysym == "z":
                self.__swiat.setRuch(Swiat.Ruch.SPECJALNY)

            self.paint()

        self.bind("<Button-1>", klik)
        self.bind("<Key>", klawisz)

    def nastepnaTura(self):
        self.__swiat.wykonajTure()

    def getDziennik(self):
        return self.__swiat.getDziennik()

    def setSwiat(self, swiat: Swiat):
        self.__swiat = swiat
        self.__wysokosc = swiat.getWysokosc()
        self.__szerokosc = swiat.getSzerokosc()
        self.paint()

    def czlowiekInfo(self):
        ruch = self.__swiat.getRuch()
        komunikat = "Ruch czlowieka: "

        if ruch == Swiat.Ruch.GORA:
            komunikat += "do gory"
        elif ruch == Swiat.Ruch.DOL:
            komunikat += "na dol"
        elif ruch == Swiat.Ruch.STOJ:
            komunikat += "bedzie stal"
        elif ruch == Swiat.Ruch.LEWO:
            komunikat += "w lewo"
        elif ruch == Swiat.Ruch.PRAWO:
            komunikat += "w prawo"
        elif ruch == Swiat.Ruch.SPECJALNY:
            komunikat += "uruchomi umiejetnosc specjalna"

        self.create_text(10, 10, text=komunikat, fill="pink", anchor=W)

    def getSwiat(self):
        return self.__swiat

    def __maCzlowieka(self) -> bool:
        for org in self.__swiat.getOrganizmy():
            if isinstance(org, Czlowiek):
                return True
        return False

    def __initPopup(self, event):

        popup = Toplevel(self)
        popup.title("Organizmy")

        popup.geometry(f"150x350+{self.winfo_x() + event.x}+{self.winfo_y() + event.y}")
        popup.bind("<FocusOut>", lambda ev: ev.widget.destroy())
        popup.focus_set()
        popup.resizable(False, False)
        popup.wm_transient(self)

        p0 = Wektor2d(0, 0)

        organizmy = [
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

        if not self.__maCzlowieka():
            organizmy.append(Czlowiek(p0))

        for i in range(len(organizmy)):
            org = organizmy[i]
            Button(popup, text=str(org),
                   bg="white",
                   command=lambda o=copy.deepcopy(org): self.__polozOrganizm(o, Wektor2d(event.y, event.x), popup)).pack()

    def __polozOrganizm(self, org: Organizm, pos: Wektor2d, main):
        print(org)
        main.destroy()

        nowePolozenie = Wektor2d(int(pos.getY() / self.__rozmiarZwierzecia), int(pos.getX() / self.__rozmiarZwierzecia))

        kolidujacy = self.__swiat.getOrganizmNaPozycji(nowePolozenie)

        while kolidujacy is not None:
            kolidujacy.zabij()
            kolidujacy = self.__swiat.getOrganizmNaPozycji(nowePolozenie)

        org.setPolozenie(nowePolozenie)
        self.__swiat.addOrganizm(org)

        self.paint()
