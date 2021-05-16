# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def exponentiation(num1):
    return num1**2


def squareRoot(num1):
    return math.sqrt(num1)


def percent(num1, num2):
    return num1 % num2


def start():
    print("Wybierz operacje.")
    print("1.Dodawanie")
    print("2.Odejmowanie")
    print("3.Mnożenie")
    print("4.Dzielenie")
    print("5.Potęgowanie")
    print("6.Pierwiastek")
    print("7.Reszta z dzielenia")


    while True:
        choice = input("Enter choice(1/2/3/4/5/6/7): ")

        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

            elif choice == '5':
                print(num1, "^2 = ", exponentiation(num1))

            elif choice == '6':
                print(num1, "sqrt =", squareRoot(num1))

            elif choice == '7':
                print(num1, "%", num2, "=", percent(num1, num2))
            break
        else:
            print("Invalid Input")


if __name__ == '__main__':
    start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/





