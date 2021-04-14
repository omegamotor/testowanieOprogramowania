# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Klasy


if __name__ == '__main__':
    p1 = Klasy.Pracownik()
    print(p1.Email())
    print(p1.Fullname())
    print(p1.Job_raise())

    p2 = Klasy.KlubPilkarski()
    print(p2.CreateTxt())

