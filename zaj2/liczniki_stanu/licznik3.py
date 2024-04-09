#Klasę z atrybutem instancji.
class licznik3:
    def _init_(self) -> None:
        self.licznik_stanu = 0

        def _call_(self) -> int:
            self.licznik_stanu += 1
            return self.licznik_stanu
    
    licznik3 = licznik3()

    for  _ in range(10):
        print(licznik3())
