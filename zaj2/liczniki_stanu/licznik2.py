#Zmienną global
licznik_stanu = 0

def licznik2() -> int:
    global licznik_stanu
    licznik_stanu += 1
    return licznik_stanu

for _ in range(10):
    print(licznik2())
