from tkinter import *
from wizualizacja import Wizualizacja
from wektor2d import Wektor2d
from tkinter import ttk, messagebox, filedialog
from tkinter.messagebox import showinfo
from symulacja.swiat import Swiat
from symulacja.zwierzeta.czlowiek import Czlowiek
from symulacja.zwierzeta.wilk import Wilk
class Aplikacja(Tk):

    TYTUL = "Symulacja"
    DOMYSLNA_WYSOKOSC = 1080
    DOMYSLNA_SZEROKOSC = 1920

    def __init__(self):
        super().__init__()
        self.withdraw()  # Ukryj główne okno aplikacji na czas wprowadzania wymiarów

        self.__wysokosc_swiata = None
        self.__szerokosc_swiata = None

        self.__pytajOWymiarySwiata()  # Pokaż okno dialogowe

    def __pytajOWymiarySwiata(self):
        dialog = Toplevel(self)
        dialog.geometry("200x200")
        dialog.title("Wymiary świata")

        Label(dialog, text="Wysokość świata:").pack(pady=10)
        self.wysokoscEntry = Entry(dialog)
        self.wysokoscEntry.pack(pady=5)

        Label(dialog, text="Szerokość świata:").pack(pady=10)
        self.szerokoscEntry = Entry(dialog)
        self.szerokoscEntry.pack(pady=5)

        Button(dialog, text="OK", command=lambda: self.__zapiszWymiarySwiata(dialog)).pack(pady=20)

    def __zapiszWymiarySwiata(self, dialog):
        try:
            self.__wysokosc_swiata = int(self.wysokoscEntry.get())
            self.__szerokosc_swiata = int(self.szerokoscEntry.get())

            if self.__wysokosc_swiata <= 0 or self.__szerokosc_swiata <= 0:
                raise ValueError

            dialog.destroy()  # Zamknij okno dialogowe
            self.deiconify()  # Pokaż główne okno aplikacji
            self.__inicjujAplikacje()

        except ValueError:
            messagebox.showerror("Błąd", "Proszę wprowadzić prawidłowe wymiary świata.")

    def __inicjujAplikacje(self):
        self._wizualizacja = Wizualizacja(self, int(Aplikacja.DOMYSLNA_WYSOKOSC * 9 / 10), self.__bazowySwiat())

        self.geometry(f"{Aplikacja.DOMYSLNA_SZEROKOSC}x{Aplikacja.DOMYSLNA_WYSOKOSC}")
        self.minsize(Aplikacja.DOMYSLNA_SZEROKOSC, Aplikacja.DOMYSLNA_WYSOKOSC)

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
        self._wizualizacja.pack(side=LEFT, fill=BOTH, expand=True)

        # Tworzenie panelu dla przycisków
        panelGuziki = Frame(self)
        panelGuziki.pack(side=BOTTOM, fill=X)

        turaButton = Button(panelGuziki, text="nastepna tura", command=self.__nastepnaTuraCallback)
        turaButton.pack(side=LEFT, padx=5, pady=5)

        # Tworzenie dziennika
        textFrame = Frame(self)
        textFrame.pack(side=RIGHT, fill=BOTH, expand=True)

        # Tworzenie paska przewijania
        scrollbar = Scrollbar(textFrame)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Tworzenie widgetu Text do wyświetlania komunikatów
        self.dziennikText = Text(textFrame, bg="yellow", wrap=WORD, yscrollcommand=scrollbar.set)
        self.dziennikText.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.config(command=self.dziennikText.yview)
        self.dziennikText.config(text="Komunikaty")
        # Wyłączenie bezpośredniej edycji w widgetcie Text
        self.dziennikText.config(state=DISABLED)

    def __bazowyCallback(self):
        self._wizualizacja.setSwiat(self.__bazowySwiat())

    def __wczytajCallback(self):
        fname = filedialog.askopenfilename()
        if fname == "":
            return

        sw = self._menedzerPlikow.wczytaj(fname)
        if sw is None:
            messagebox.showerror("Błąd", "Błąd pliku")
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



    def __bazowySwiat(self, typ=Swiat.Typ.KARTEZJANSKI):
        return Swiat(self.__wysokosc_swiata, self.__szerokosc_swiata, [
            Czlowiek(Wektor2d(5, 5)),
            Wilk(Wektor2d(3,3))
        ], typ)

    def __pustySwiat(self):
        return Swiat(self.__wysokosc_swiata, self.__szerokosc_swiata)


