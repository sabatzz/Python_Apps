from importlib import reload
import os
import time
import czas

#Moduły i przestrzenie nazw

current_path = os.getcwd()
#print(current_path)

print(czas.aktualny_czas)

time.sleep(5)
print(czas.aktualny_czas)

reload(czas)
print(czas.aktualny_czas)