import os
import sqlite3
from faker import Faker
import random

def create_database():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    # tworzenie tabeli
    cursor.execute("""CREATE TABLE KLUBY(nazwa text, trener text)""")
    conn.commit()


def insert(nazwa, trener, kraj, liczba_pilkarzy, najlepszy_zawodnik, sponsor_glowny):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO test (nazwa, trener) VALUES (nazwa, trener)")
    # zapisanie danych do bazy
    conn.commit()
    print("Dodano")


def select_all_klubs(nazwa):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM KLUBY"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def add_some_data():
    fake = Faker()
    liczba = random.randint(3,10)
    for x in range(liczba):
        nazwa = 'Klub ' + str(x)
        trener = fake.name()
        kraj = fake.locales
        liczba_pilkarzy = random.randint(10,15)
        najlepszy_zawodnik = fake.name()
        sponsor_glowny = fake.name()
        insert(nazwa, trener, kraj, liczba_pilkarzy, najlepszy_zawodnik, sponsor_glowny)




#nazwa = 'Nazwa Klubu'
#trener = 'Trener Klubu'
#kraj = 'Kraj Klubu'
#liczba_pilkarzy = '10'
#najlepszy_zawodnik = 'Zawodnik Klubu'
#sponsor_glowny = 'Sponsor Klubu'

if __name__ == '__main__':
    if not os.path.exists("mydatabase.db"):
        create_database()
    #insert(nazwa, trener, kraj, liczba_pilkarzy, najlepszy_zawodnik, sponsor_glowny)
    #insert(nazwa, trener, kraj, liczba_pilkarzy, najlepszy_zawodnik, sponsor_glowny)
    add_some_data()
    print(select_all_klubs('nazwa'))