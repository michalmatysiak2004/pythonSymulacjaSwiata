class Dziennik:

    def __init__(self):

        self.__komunikaty = []


    def wpisz(self, komunikat : str):

        self.__komunikaty.append(komunikat)

    def czysc(self):

        self.__komunikaty = []

    def wypisz(self) -> str:

        out = ""
        for kom in self.__komunikaty:

            out += f"{kom}\n"

        return out