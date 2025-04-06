from dekorator import time_consumption, log_arguments
import pydoc

# Krok 1: Tworzenie klas zadania (w pliku zadania.py)
class Zadanie:
    '''
    Klasa reprezentująca zadanie.
    Jest to klasa nadrzędna.
    '''

    def __init__(self, tytul, opis, termin_wykonania):
        '''
        Implementacja kontruktora klasy Zadanie.
        Konstruktor przyjumje podstawowe parametry zadania oraz
        inicjalizuje atrybuty podczas tworzenia obiektu.

        :param tytul: tytuł zadania
        :param opis: opis zadania
        :param termin_wykonania: termin wykonania zadania
        :param wykonane: czy zadanie jest wykonane
        '''
        self.tytul = tytul
        self.opis = opis
        self.termin_wykonania = termin_wykonania
        self.wykonane = False



    def __str__(self):
        '''
        Implementacja metody __str__.
        Metoda zwraca stringa z danymi zadania.
        '''
        return f"{self.tytul} - {self.opis} - {self.termin_wykonania} - Wykonane?: {self.wykonane}"


class ZadaniePriorytetowe(Zadanie):
    '''
    Klasa reprezentująca zadanie priorytetowe.
    Jest to klasa pochodna.
    '''

    def __init__(self, tytul, opis, termin_wykonania, priorytet):
        '''
        Implementacja konstruktora klasy ZadaniePriorytetowe.
        :param priorytet: priorytet zadania
        '''
        super().__init__(tytul, opis, termin_wykonania)
        self.priorytet = priorytet


    def __str__(self):
        '''
        Implementacja metody __str__.
        '''
        return f"{super().__str__()} - Priorytet: {self.priorytet}"


class ZadanieRegularne(Zadanie):
    '''
    Klasa reprezentująca zadanie regularne.
    Jest to klasa pochodna.
    '''

    def __init__(self, tytul, opis, termin_wykonania, powtarzalnosc):
        '''
        Implementacja konstruktora klasy ZadanieRegularne.
        :param powtarzalnosc: powtarzalnosc zadania
        '''
        super().__init__(tytul, opis, termin_wykonania)
        self.powtarzalnosc = powtarzalnosc


    def __str__(self):
        '''
        Implementacja metody __str__.
        '''
        return f"{super().__str__()} - Powtarzalnosc: {self.powtarzalnosc}"


class ManagerZadan:
    '''
    Klasa reprezentująca managera zadań.
    Klasa zawiera metody do zarządzania zadaniami oraz przechowuje listę zadań.
    W jej skład wchodzą również metody, które pozwalają na zapisywanie i odczytywanie zadań z pliku.
    '''

    def __init__(self):
        '''
        Implementacja konstruktora klasy ManagerZadan.
        Konstruktor inicjalizuje pustą listę zadań.
        '''
        self.zadania = []


    #@time_consumption
    @log_arguments
    def dodaj_zadanie(self, zadanie):
        '''
        Implementacja metody dodaj_zadanie.
        Metoda dodaje zadanie do listy zadań.
        :param zadanie: obiekt, który reprezentuje jedno zadanie
        '''
        self.zadania.append(zadanie)


    #@time_consumption
    def usun_zadanie(self, zadanie):
        '''
        Implementacja metody usun_zadanie.
        Metoda usuwa zadanie z listy zadań.
        :param zadanie: obiekt, który reprezentuje jedno zadanie
        '''
        self.zadania.remove(zadanie)

    
    #@time_consumption
    def oznacz_jako_wykonane(self, zadanie):
        '''
        Implementacja metody oznacz_jako_wykonane.
        Metoda oznacza zadanie jako wykonane.
        :param zadanie: obiekt, który reprezentuje jedno zadanie
        '''
        zadanie.wykonane = True


    #@time_consumption
    def edytuj_zadanie(self, zadanie, **kwargs):
        '''
        Implementacja metody edytuj_zadanie.
        Metoda pozwala na edycję zadania. Na podstawie podanych argumentów podczas wywołania można zmienić tytuł, opis lub termin wykonania zadania.
        :param zadanie: obiekt, który reprezentuje jedno zadanie
        :param **kwargs: lista argumentów
        '''
        for key, value in kwargs.items():
            if hasattr(zadanie, key):
                setattr(zadanie, key, value)


    def __contains__(self, item):
        '''
        Implementacja metody __contains__.
        Metoda sprawdza, czy zadanie znajduje się na liście zadań.
        :param item: reprezentuje element w liscie zadania
        '''
        return item in self.zadania

    @time_consumption
    def zapisz_zadania_do_pliku(self, filename = 'zadania.txt'):
        '''
        Implementacja metody zapisz_zadania_do_pliku.
        Metoda zapisuje zadania do pliku.
        Domyślnie zapisuje do pliku 'zadania.txt'.
        '''
        with open(filename, 'w', encoding='utf-8') as file:
            for zadanie in self.zadania:
                file.write(str(zadanie) + '\n')

    @time_consumption
    def odczytaj_zadania_z_pliku(self, filename = 'zadania.txt'):
        '''
        Implementacja metody odczytaj_zadania_z_pliku.
        Metoda odczytuje zadania z pliku.
        Domyślny odczyt z pliku zadania.txt.
        '''
        self.zadania.clear()

        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(' - ')
                if len(parts) == 4:
                    tytul, opis, termin_wykonania, wykonane = parts
                    zadanie = Zadanie(tytul, opis, termin_wykonania)
                    zadanie.wykonane = (wykonane == 'Wykonane?: True')
                    self.zadania.append(zadanie)
                elif len(parts) == 5 and 'Priorytet' in parts[4]:
                    tytul, opis, termin_wykonania, wykonane, priorytet = parts
                    zadanie = ZadaniePriorytetowe(tytul, opis, termin_wykonania, priorytet.split(': ')[1])
                    zadanie.wykonane = (wykonane == 'Wykonane?: True')
                    self.zadania.append(zadanie)
                elif len(parts) == 5 and 'Powtarzalnosc' in parts[4]:
                    tytul, opis, termin_wykonania, wykonane, powtarzalnosc = parts
                    zadanie = ZadanieRegularne(tytul, opis, termin_wykonania, powtarzalnosc.split(': ')[1])
                    zadanie.wykonane = (wykonane == 'Wykonane?: True')
                    self.zadania.append(zadanie)



pydoc.writedoc('zadania')