import this
from typing import Any 

#Przypisania
#6
dane = (2024, 'Python', 3.8)
rok, jezyk, wersja = dane
print(f"Rok: {rok}, język: {jezyk}, wersja: {wersja}")

#7
oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny
print(f"Pierwsza: {pierwsza}, środkowe: {srodek}, ostatnia: {ostatnia}")

#8
info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
imie, nazwisko, _, _, zawod = info
print(f"Imię: {imie}, nazwisko: {nazwisko}, zawód: {zawod}")

#9
dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
rok, lista = dane
jezyk, wersja, opis = lista
print(f"Rok: {rok}, jezyk: {jezyk}, wersja: {wersja}, opis: {opis}")

#Przypisania z wieloma celami
#10
a = b = [1,2,3]
b[0] = "zmieniono"
print(f"b[0] = {b[0]}")
print(a, b)
#Pierwszy wyraz na liście a i b został zmieniony
#Zmienne wskazują na ten sam obiekt (listę)
#Gdy zmienimy wartość obiektu, to wartośc wszyskich zmiennych
#odwołujących się do do niego zostanie zmieniona.
#Listy są obiektami mutowalnymi -> po stworzeniu można modyfikować ich zawartość.

#11
c = a[:]
c[0] = "nowa wartość"
print(a,b,c)
#Kopia jest nowym obiektem, 
#a i b nie wskazują na c, więc nie zmienią zawartości

#12
x = y = 10
y += 1
print(x, y)
#Integery nie są obiektami mutowalnymi.
#Na początku x i y wskazują na ten sam obiekt, 
#Inkrementacja sprawia, ze tworzy sie nowy obiekt


#Przypisania rozszerzone
#13
K = [1, 2]
L = K 
K = K + [3, 4] 
M = [1, 2]
N = M #
M += [3, 4] 

# Konkatenacja za pomocą operatora + tworzy nową listę,
# co powoduje zmianę przypisanej zmiennej
# operator += modyfikuje istniejącą listę, 
# wpływając na wszystkie zmienne wskazujące na nią.

print(K,L,M,N)


#Techniki tworzenia pętli
#14
imiona = ['Anna', 'Jan', 'Ewa']
oceny = [5, 4, 3]

for z in zip(imiona, oceny):
    print(z)

#Jeśli listy będą miały różne długości to zip() będzie parował 
#elementy  do wspólnego największego indeksu

#15
liczby = [1, 2, 3, 4, 5]

def kwadrat(x):
    return x**2

print(list(map(kwadrat, liczby)))


# #Iteratory
# #Dokumentowanie kodu
# #Funkcje
# #Argumenty
# #16
def zmien_wartosc(arg):
    if isinstance(arg, list):
        arg[0] = 'kalafior'
    elif isinstance(arg, int):
        arg = 65482652
    return arg

a = [1,2,3]
b = 1

print(f"Wynik funkcji z argumentem a = {a}: {zmien_wartosc(a)}") #pierwszy element listy się zmienił
print(f"Wynik funkcji z argumentem b = {b}: {zmien_wartosc(b)}") 
#Dla listy zwracany jest ten sam obiekt:
print(id(a) == id(zmien_wartosc(a)))
#Dla int zostaje zwrócony nowy obiekt:
print(id(b) == id(zmien_wartosc(b)))

#17
def zamowienie_produktu(nazwa_produktu, *, cena, ilosc):
    pass
    podsumowanie = f"Zamówiono: {nazwa_produktu}, Cena: {cena*ilosc} zł, Ilość: {ilosc} sztuk."
    return podsumowanie

#a
zamowienia = []

for produkt, dane in {"Bluzka":[90,3], "Spodnie":[120,2], "Buty":[300,1]}.items():
    raport = zamowienie_produktu(produkt, cena=dane[0], ilosc=dane[1])
    zamowienia.append(raport)
#b
for i in zamowienia:
    print(i)

#c
def zamowienie_produktu2(nazwa_produktu, *, cena, ilosc=1):
    pass
    podsumowanie = f"Zamówiono: {nazwa_produktu}, Cena za sztukę: {cena} zł, Ilość: {ilosc} szt."
    suma = f"Koszt zamówienia: {cena*ilosc} zł."
    raport = (podsumowanie, suma)
    return raport
#d
zamowienia2 = []
#e
for produkt, dane in {"Bluzka":90, "Spodnie":120, "Buty":300}.items():
    raport= zamowienie_produktu2(produkt, cena=dane)
    zamowienia2.append(raport)

for i in zamowienia2:
    print(i)


#18
def stworz_raport(*args, **kwargs):
    for prod_id in args:
        raport = f"ID produktu: {prod_id} "
        nazwa = kwargs.get(f'nazwa_{prod_id}', '')
        cena = kwargs.get(f'cena_{prod_id}', '')
        raport += f"| Nazwa: {nazwa} | Cena: {cena}"
        print(raport)

stworz_raport(101, 102, nazwa_101="Kubek termiczny", cena_101="45.99 zł", nazwa_102="Długopis", cena_102="4.99 zł")


#Zasięgi

#Funkcje fabrykujące - obiekty funkcji, które pamiętają wartości w otaczających zasięgach
#19
def stworz_funkcje_potegujaca(wykladnik):
    def potega(podstawa):
         return podstawa**wykladnik
    return potega


print(f"Wynik 4^2: {stworz_funkcje_potegujaca(2)(4)}")
#albo
potega_2 = stworz_funkcje_potegujaca(2)
print(potega_2(4)) # Wynik: 16


#Funkcje anonimowe lambda
    
#22
ksiazki = [
    {"tytul": "Zbrodnia i Kara", "autor": "Fiodor Dostojewski", "rok_wydania": 1866},
    {"tytul": "Pan Tadeusz", "autor": "Adam Mickiewicz", "rok_wydania": 1834},
    {"tytul": "Bieguni", "autor": "Olga Tokarczuk", "rok_wydania": 2007},
]

#a - sortowanie po roku
sorted(ksiazki, key= lambda d: d['rok_wydania'])

#b - książki wydane  po 2000
publ_after_2000 = list(filter(lambda d: d['rok_wydania'] > 2000, ksiazki))

#c - lista tytułów
ksiazki = list(map(lambda d: d['tytul'], ksiazki))
ksiazki


#Generatory

#23
def dni_tygodnia():
    yield 'Poniedziałek'
    yield 'Wtorek'
    yield 'Środa'
    yield 'Czwartek'
    yield 'Piątek'
    yield 'Sobota'
    yield 'Niedziela'


for day in dni_tygodnia():  
    print(day)

days = dni_tygodnia()
pon_wt_sr = [next(days) for _ in range(3)]
pon_wt_sr
