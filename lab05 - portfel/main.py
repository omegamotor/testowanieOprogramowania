class Portfel():
    def __init__(self, ile):
        self.wartosc = ile
        print('Nowy portfel, niestety jest pusty!\n')
        print(self.wartosc)

    def wydaj(self, ile):
        if self.wartosc > ile:
            self.wartosc -= ile
            print('Wydano pieniądze!\nZostało ci')
            print(self.wartosc)
        else:
            print('Nie masz takich pieniędzy')
        return self.wartosc

    def dodaj(self, ile):
        self.wartosc += ile
        print('Dodano pieniądze!\nTeraz masz')
        print(self.wartosc)
        return self.wartosc

    def ileMam(self):
        return self.wartosc



if __name__ == '__main__':
    p = Portfel(0)
    p.dodaj(50)
    p.wydaj(10)