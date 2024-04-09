#Atrybut funkcji
def licznik4() -> int:

    licznik4.licznik_stanu = getattr(licznik4, 'licznik_stanu', 0) + 1
    return licznik4.licznik_stanu