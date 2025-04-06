# Zadanie 2 - Zaawanasowane techniki programowania - laboratorium

## Instalacja
#1. Utwórz wirtualne środowisko Pythona.
#2. Zainstaluj wymagane biblioteki z pliku `requirements.txt`.
#3. Uruchom program za pomocą komendy `python main.py`.

## Autor - Maciej Rudy
## Licencja - Licencja Open Source

from zadania import Zadanie, ZadaniePriorytetowe, ZadanieRegularne, ManagerZadan
from dekorator import time_consumption
import sys

def is_virtualenv():
    return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)

@time_consumption
def main():
    print("Co zamierzasz zrobic?")
    work = True
    manager = ManagerZadan()

# check if virtual environment is active or not

    if is_virtualenv():
        print("Running inside a virtual environment.")
    else:
        print("Not running inside a virtual environment.")

    while work == True:
        
        print("1 - Dodaj nowe zadanie")
        print("2 - Edytuj zadanie")
        print("3 - Usun zadanie")
        print("4 - Oznacz zadanie jako wykonane")
        print("5 - wyswietl parametry zadania")
        print("6 - wyswietl zadania")
        print("7 - Zapisz zadania do pliku")
        print("8 - Odczytaj zadania z pliku")
        print("X - Zakoncz program")

        choice = input("Wybierz opcje: ")

        if choice == "1":

            tytul = input("Podaj tytul zadania: ")
            opis = input("Podaj opis zadania: ")
            termin = input("Podaj termin wykonania zadania (dd-mm-yyyy): ")
            loop = True
            while loop == True:
                type = input("Zadanie priorytetowe, czy regularne? a/b: ")
                if type == "a":
                    priorytet = input("Podaj priorytet (0-5): ")
                    tytul = ZadaniePriorytetowe(tytul, opis, termin, priorytet)
                    loop = False
                elif type == "b":
                    powtarzalnosc = input("Podaj powtarzalnosc: ")
                    tytul = ZadanieRegularne(tytul, opis, termin, powtarzalnosc)
                    loop = False
                else:
                    print("Podano zly typ priorytetu / powtarzalnosci")
                    print("Podaj ponownie")
                    

            manager.dodaj_zadanie(tytul)

        elif choice == "2":
            tytul = input("Podaj tytul zadania, ktore chcesz edytowac: ")
            for zadanie in manager.zadania:
                if zadanie.tytul == tytul:
                    nowy_tytul = input("Podaj nowy tytul (lub zostaw puste): ")
                    nowy_opis = input("Podaj nowy opis (lub zostaw puste): ")
                    nowy_termin = input("Podaj nowy termin wykonania (lub zostaw puste): ")
                    kwargs = {}
                    if nowy_tytul:
                        kwargs['tytul'] = nowy_tytul
                    if nowy_opis:
                        kwargs['opis'] = nowy_opis
                    if nowy_termin:
                        kwargs['termin_wykonania'] = nowy_termin
                    manager.edytuj_zadanie(zadanie, **kwargs)
                    print("Zadanie zostalo zaktualizowane.")
                    break
                else:
                    print("Zadanie o podanym tytule nie istnieje.")
        elif choice == "3":
            tytul = input("Podaj tytul zadania, ktore chcesz usunac: ")
            for zadanie in manager.zadania:
                if zadanie.tytul == tytul:
                    manager.usun_zadanie(zadanie)
                    print("Zadanie zostalo usuniete.")
                    break
            else:
                print("Zadanie o podanym tytule nie istnieje.")

        elif choice == "4":
            tytul = input("Ktore zadanie ma zostac oznaczone jako wykonane? (tytul): ")
            for zadanie in manager.zadania:
                if zadanie.tytul == tytul:
                    manager.oznacz_jako_wykonane(zadanie)
                    print("Zadanie zostalo oznaczone jako wykonane.")
                    break
            else:
                print("Zadanie o podanym tytule nie istnieje.")
    
                
        elif choice == "5":
            tytul = input("Podaj tytul zadania, ktore chcesz wyswietlic: ")
            
            for zadanie in manager.zadania:
                if zadanie.tytul == tytul:
                    print(str(zadanie))
                    break
            else:
                print("Zadanie o podanym tytule nie istnieje.")
                print(str(zadanie))
            

        elif choice == "6":
            for zadanie in manager.zadania:
                print(str(zadanie))
                
        elif choice == "7":
            nazwa_pliku = input("Podaj nazwe pliku: ")
            if nazwa_pliku != "":
                manager.zapisz_zadania_do_pliku(nazwa_pliku)
                print(f"Zadania zostaly zapisane do pliku {nazwa_pliku}")
            else:
                manager.zapisz_zadania_do_pliku()
                print("Uzyto domyslnej nazwy pliku.")
            
        elif choice == "8":
            nazwa_pliku = input("Podaj nazwe pliku: ")
            if nazwa_pliku != "":
                manager.odczytaj_zadania_z_pliku(nazwa_pliku)
                print(f"Zadania zostaly pomyslnie odczytane z pliku {nazwa_pliku}")
            else:
                manager.odczytaj_zadania_z_pliku()
                print("Zadania zostaly pomyslnie odczytane z domyslnego pliku.")

        elif choice == "X" or choice == "x":
            work = False
            print("Koniec programu")

if __name__ == "__main__":
    main()