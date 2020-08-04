import logging

dzialanie = int(input("Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

def calculate():
    a = int(input("Podaj pierwszy składnik: "))
    b =  int(input("Podaj drugi składnik: "))
    if dzialanie == 1:
        print(f"Dodaję {a} i {b}")
        print(f"Wynik to {a + b}")
    elif dzialanie == 2:
        print(f"Od {a} odejmuję {b} ")
        print(f"Wynik to {a - b}")
    elif dzialanie == 3:
        print(f"Mnożę {a} i {b}")
        print(f"Wynik to {a * b}")
    elif dzialanie == 4:
        print(f"Dzielę {a} przez {b}")
        print(f"Wynik to {a / b}")

calculate()
