from tkinter import *

from wizualizacja import Wizualizacja
from wektor2d import Wektor2d
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkinter.messagebox import showinfo
from symulacja.swiat import Swiat
from symulacja.zwierzeta.czlowiek import Czlowiek


class Aplikacja(Tk):


    TYTUL = "Symulacja"
    DOMYSLNA_WYSOKOSC = 600
    DOMYSLNA_SZEROKOSC = 600


    def __init__(self, wysokosc: int, szerokosc: int):

        super().__init__()

        self._wizualizacja = Wizualizacja(self, int(Aplikacja.DOMYSLNA_WYSOKOSC * 9 / 10), self.__bazowySwiat())
        #self._menedzerPlikow = MenedzerPlikow()

        self.geometry(f"{szerokosc}x{wysokosc}")
        self.minsize(szerokosc, wysokosc)


        self.title(Aplikacja.TYTUL)

        self.__inicjujMenuGorne()

        self.__inicjujPanelGlowny()

        self._wizualizacja.paint()


    def __inicjujMenuGorne(self):

        menuBar = Menu(self)
        menuNowy = Menu(menuBar, tearoff=False)
        menuPlik = Menu(menuBar, tearoff=False)

        menuNowy.add_command(label="Bazowy_Kartezjanski", command=self.__bazowyCallback)

        menuNowy.add_command(label="Bazowy_Hex", command=self.__bazowyHexCallback)

        menuPlik.add_command(label="Wczytaj", command=self.__wczytajCallback)
        menuPlik.add_command(label="Zapisz", command=self.__zapiszCallback)

        menuBar.add_cascade(label="Nowy", menu=menuNowy)
        menuBar.add_cascade(label="Plik", menu=menuPlik)

        self.config(menu=menuBar)


    def __inicjujPanelGlowny(self):

        self._wizualizacja.pack()

        panelGuziki = PanedWindow()


        turaButton = Button(panelGuziki, text="nastepna tura", command=self.__nastepnaTuraCallback)
        dziennikButton =  Button(panelGuziki, text="dziennik", command=self.__dziennikCallback)

        panelGuziki.add(turaButton)
        panelGuziki.add(dziennikButton)
        panelGuziki.pack()


    def __bazowyCallback(self):

        self._wizualizacja.setSwiat(self.__bazowySwiat())


    def __wczytajCallback(self):

        fname = filedialog.askopenfilename()

        if fname == "":
            return

        sw = self._menedzerPlikow.wczytaj(fname)

        if sw is None:
            messagebox.showerror("Blad","blad pliku")
            return

        self._wizualizacja.setSwiat(sw)

    def __bazowyHexCallback(self):

        self._wizualizacja.setSwiat(self.__bazowySwiat(Swiat.Typ.HEX))


    def __zapiszCallback(self):

        fname = filedialog.asksaveasfilename()

        if fname == "":
            return

        self._menedzerPlikow.zapisz(self._wizualizacja.getSwiat(), fname)


    def __nastepnaTuraCallback(self):

        self._wizualizacja.nastepnaTura()
        self._wizualizacja.paint()

    def __dziennikCallback(self):
        dziennik = self._wizualizacja.getDziennik().wypisz()
        showinfo("Dziennik", dziennik)

    def __bazowySwiat(self, typ = Swiat.Typ.KARTEZJANSKI):
        return Swiat(20, 20, [

           # Wilk(Wektor2d(1,1)),
           # Wilk(Wektor2d(2, 2)),
            #Trawa(Wektor2d(4,4)),
           # Trawa(Wektor2d(4, 2)),
           # Trawa(Wektor2d(10, 10)),
           # Owca(Wektor2d(14,14)),
           # Mlecz(Wektor2d(9,4)),
           # WilczeJagody(Wektor2d(12,14)),
           # Guarana(Wektor2d(17,17)),
           # BarszczSosnowskiego(Wektor2d(17, 5)),
           # Antylopa(Wektor2d(13,4)),
           # Lis(Wektor2d(12, 12)),
            Czlowiek(Wektor2d(5,5)),
           # Cyberowca(Wektor2d(7,9)),

        ], typ)

    def __pustySwiat(self):

        return Swiat(20,20)
