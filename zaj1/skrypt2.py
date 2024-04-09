import math
import random

#Działania matematyczne
x = 100
dodawanie = x + 123.15
potega = dodawanie**12
tekst = str(potega)
wartosc_pi = math.pi
losowa = random.randint(1,5)

#Łańcuchy znaków
tekst = f"Wartość: {tekst}" #f wyswietla wartosci float w tekscie
print(tekst)
tekst_len = len(tekst)
print(dir(tekst))
print(tekst[1:4])
tekst = tekst.upper()

#Listy
lista = list(tekst)
lista = lista[0:8]
print(lista)
lista_ex = [1,2,3,4,5]
#lista = lista + lista_ex
lista.extend(lista_ex)
lista.remove(":")
print('lista1: ' + str(lista))

lista2 = [1,2,3,"banan",100]
print('lista2: ' + str(lista2))

lista3 = [x**2 for x in lista2 if x != 'banan']
print('lista3: ' + str(lista3))

my_range = range(2,17,2)
lista4 = list(my_range)
print('lista4: ' + str(lista4))

#Słowniki
ja = {}
ja['Imię'] = 'Zuzanna'
ja['Nazwisko'] = 'Sabat'
ja['Wiek'] = 22
ja['Rodzice'] = {'Rodzic1': {'Imię': 'Magdalena', 'Wiek': 45},
                 'Rodzic2': {'Imię':'Grzegorz', 'Wiek': 50}}
print(ja)
print(ja['Rodzice'])
print(ja['Rodzice']['Rodzic1']['Imię'])
print(ja.keys())
print('Rodzeństwo' in ja)

#Krotki
krotka1 = (1, 2, "3", 4, 2, 5)
print('Długość: ' + str(len(krotka1)) + ', pierwszy wyraz: ' + str(krotka1[0]))
print('Wartość 2 występuje ' + str(krotka1.count(2)) + ' razy')
#krotka1[0] = 2

#Zbiory
X = set('kalarepa')
Y = set('lepy')

print(Y.intersection(X))

#Instrukcje
#1
# imiona = ['Emilia', 'Natalia', 'Filip', 'Zuza', 'Mateusz', 'Ania']

# for index, x in enumerate(imiona):
#     print(index+1, x)

#a

# liczba = random.randint(-10, 10)
# print(liczba)
# if liczba > 0 and liczba % 2 == 0:
#     print("Liczba jest dodatnia i parzysta")
# elif liczba > 0 :
#     print("Liczba jest dodatnia")
# elif liczba % 2 == 0:
#     print("Liczba jest parzysta")
# else:
#     print("Liczba nie jest dodatnia lub parzysta")

#b
# number = input("Wprowadź liczbę: ")
# number = int(number)
# if number != 0:
#     print("Liczba jest różna od zera")
# else:
#     print("Liczba jest równa 0")

# #c
# owoce = ['jabłko', 'banan', 'pomarańcza']
# owoc = input("Wprowadź owoc: ")
# if owoc in owoce:
#     print("Owoc dostępny")
# else:
#     print("Owoc niedostępny")

#3
# suma = 0
# while suma <= 100:
#     num = input("Wprowadź liczbę: ")
#     num = int(num)
#     suma = suma + num
# print(suma)

#Dziwactwa
L = [1,2,3,4]
M = [1,2,3,L,4]
print(f"Wartość zmiennej M przed zmianą L: {M}")
L[1] = "woooow"
print(f"Wartość zmiennej M po zmianie L: {M}")

L = [4,5,6]
X = L * 4
Y = [L] * 4
print(f"X: {X}, Y: {Y}")
L[1] = "wow"
print(f"X: {X}, Y: {Y}")
L = [4,5,6]
Y = [list(L)] * 4
L[1] = "wow"
print(f"Y: {Y}")
Y[0][1] = "wow"
print(f"Y: {Y}")