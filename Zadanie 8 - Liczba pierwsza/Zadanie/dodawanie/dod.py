
class dodaj:
    def dodaj(self, a, b):
        return a+b

class LiczbaPierwsza:
    def pierwsza(self, liczba):
        if liczba > 1:
            for i in range(2, liczba):
                if (liczba % i) == 0:
                    #print(liczba, "to nie jest liczba pierwsza")
                    return False
            #print(liczba, "to jest liczba pierwsza")
            return True
        else:
            #print(liczba, "to nie jest liczba pierwsza")
            return False

    def suma_liczb_pierwszych(self, liczby):
        suma = 0
        for liczba in liczby:
            if self.pierwsza(liczba):
                suma += liczba
        return suma

