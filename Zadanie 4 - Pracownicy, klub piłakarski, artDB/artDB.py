import os
import sqlite3
from faker import Faker
import random


def create_database():
    conn = sqlite3.connect("myDB.db")
    cursor = conn.cursor()
    # tworzenie tabeli
    cursor.execute("""CREATE TABLE Kluby
    (nazwa text, trener text, kraj text, liczba_pilkarzy INTEGER,  najlepszy_zawodnik text, sponsor_glowny text)
    """)
    conn.commit()


def insert(nazwa, trener, kraj, liczba_pilkarzy, najlepszy_zawodnik, sponsor_glowny):
    # insert
    conn = sqlite3.connect("myDB.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Kluby VALUES "
                   "('" + nazwa + "', '" + trener + "', '" + kraj + "', '" + liczba_pilkarzy + "', '" + najlepszy_zawodnik + "', '" + sponsor_glowny + "')")
    # zapisanie danych do bazy
    conn.commit()


def delete(nazwa):
    conn = sqlite3.connect("myDB.db")
    cursor = conn.cursor()
    sql = "DELETE FROM Kluby WHERE nazwa=?"
    cursor.execute(sql, [(nazwa)])

    conn.commit()
    conn.close()


def update(nazwa):
    # połącz z bazą
    # zapytanie sql
    return nazwa


def select_klub(nazwa):
    conn = sqlite3.connect("myDB.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM Kluby WHERE nazwa=?"
    cursor.execute(sql, [(nazwa)])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def select_all():
    conn = sqlite3.connect("myDB.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM Kluby"
    cursor.execute(sql, [])
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    for i in range(len(result)):
        for j in range(len(result[i])):
            if(j==0):
                opis = 'Nazwa Klubu'
            elif(j==1):
                opis = 'Trener'
            elif(j==2):
                opis = 'Kraj'
            elif(j==3):
                opis = 'Liczba piłkaży'
                print(opis + ' : ' + str(result[i][j]))
                continue
            elif(j==4):
                opis = 'Najlepszy zawodnik'
            elif(j==5):
                opis = 'Główny sponsor'

            print(opis + ' : ' + result[i][j])
        print('--------------------')
    return result


def add_some_data():
    fake = Faker()
    liczba = random.randint(3,10)
    for x in range(liczba):
        nazwa = 'Klub ' + str(x)
        trener = fake.name()
        kraj = fake.locales[0]
        liczba_pilkarzy = str(random.randint(10,15))
        najlepszy_zawodnik = fake.name()
        sponsor_glowny = fake.name()
        insert(nazwa, trener, kraj, liczba_pilkarzy, najlepszy_zawodnik, sponsor_glowny)


#nazwa = 'N1'
#trener = 'trener  '
#kraj = 'Kraj Klubu  '
#liczba_pilkarzy = '1012'
#najlepszy_zawodnik = 'Zawodnik Klubu '
#sponsor_glowny = 'Sponsor Klubu '

if not os.path.exists("myDB.db"):
    create_database()

#add_some_data()
select_all()


#insert(nazwa, trener, kraj, liczba_pilkarzy, najlepszy_zawodnik, sponsor_glowny)

#print(select_klub('N3'))

#x = input('Jaki klub chcesz zmodyfikować? \nPodaj nazwę:')
#update(x)

# test update i brak klubu / Select