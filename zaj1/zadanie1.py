import json
import math
import random
import re
import numpy as np

#Praca z plikami
with open('wastewater.txt', 'r') as file:
 content = file.read()


#ZADANIA SPRAWDZAJĄCE
with open("teksty.json", "r") as file:
    cat_lovers = json.load(file)

zadanie = {}

#Zamień wszystkie duże litery na małe
zadanie['1'] = [{key.lower() : value.lower() for key, value in tekst.items()}
                for tekst in cat_lovers["teksty"]]

#Podziel go na wyrazy - będzie to najprawdopodobniej lista
zadanie['2'] = [{key : value.split() for key, value in tekst.items()} 
                 for tekst in cat_lovers["teksty"]]

#Usuń znaki interpunkcyjne – w tekście występują jedynie kropki i przecinki
zadanie['3'] = [{key: [word.strip(".,") for sentence in value for word in re.findall(r"[\w]+|[^\w\s]", sentence) if word.strip(".,")] 
                for key, value in tekst.items()} 
                for tekst in zadanie['2']]

#Zmodyfikuj tak każdy wyraz, żeby w każdym ostatni znak był w formacie dużej litery np. wyraz KozA
zadanie['4'] = [{key: [word[:-1]+word[-1].upper() for word in value]
                 for key, value in tekst.items()}
                 for tekst in zadanie['2']]

#Z listy usuń wyrazy, które nie posiadają w sobie znaku a lub A - można wykorzystać składnię list składanych
zadanie['5'] = [{key: [word for word in value if 'a' in word or 'A' in word]
                 for key, value in tekst.items()}
                 for tekst in zadanie['2']]

#Stwórz zmienną, które będzie przechowywać wszystkie unikatowe wyrazy - można wykorzystać zbiory
zadanie['6'] = list(set(word for i in zadanie['3'] 
                        for word_list in i.values() 
                        for word in word_list))

#stwórz zmienną, która będzie przetrzymywać ilość wystąpień dla każdego ze słów występujących w tekście - można wykorzystać słowniki
zadanie['7'] = [{key: {word: value.count(word) for word in value} 
                 for key, value in text.items()} 
                 for text in zadanie['3']]