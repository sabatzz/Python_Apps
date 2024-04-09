# Zmienną nonlocal w zagnieżdżonej funkcji
def licznik1() -> callable:
    licznik_stanu = 0
    def dodaj() -> int:
        nonlocal licznik_stanu
        licznik_stanu += 1
        return licznik_stanu
    return dodaj

l1 = licznik1()
for _ in range(10):
    print(l1()) 