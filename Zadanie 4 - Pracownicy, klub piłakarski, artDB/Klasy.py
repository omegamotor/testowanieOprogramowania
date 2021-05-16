import os


class Pracownik:

    def __init__(self):
        self.name = 'Jan'
        self.lastname = 'Kowalski'
        self.salary = 2000
        self.job_raise = self.salary *2
        self.email = self.name + '.' + self.lastname + '@testemail.com'

    def Email(self):
        return self.email

    def Fullname(self):
        return self.name + ' ' + self.lastname

    def Job_raise(self):
        return self.job_raise


class KlubPilkarski:
    def __init__(self):
        self.name = 'Nazwa'
        self.has_trener = False

    def AddTrener(self):
        self.has_trener = True

    def RemoveTrener(self):
        self.has_trener = False

    def CreateTxt(self):
        f = open("Kluby.txt", "a")
        f.write("Manchester City, Bayern")
        f.close()
