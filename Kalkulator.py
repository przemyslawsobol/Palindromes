import logging
logging.basicConfig(level=logging.DEBUG)

dzialanie = int(input("Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

def calculate():
    a = int(input("Podaj pierwszy składnik: "))
    b =  int(input("Podaj drugi składnik: "))
    if dzialanie == 1:
        trzeci = input("Czy chcesz dodać trzeci składnik? Y/N: ")
        if trzeci == "Y":
            c = int(input("Podaj trzeci składnik: "))
            logging.info(f"Dodaję {a}, {b} i {c}")
            print(f"Wynik to {a + b + c}")
        else:
            logging.info(f"Dodaję {a} i {b}")
            print(f"Wynik to {a + b}")
    elif dzialanie == 2:
        logging.info(f"Od {a} odejmuję {b} ")
        print(f"Wynik to {a - b}")
    elif dzialanie == 3:
        trzeci = input("Czy chcesz dodać trzeci składnik? Y/N: ")
        if trzeci == "Y":
            c = int(input("Podaj trzeci składnik: "))
            logging.info(f"Mnożę {a}, {b} i {c}")
            print(f"Wynik to {a * b * c}")
        else:
            logging.info(f"Mnożę {a} i {b}")
            print(f"Wynik to {a * b}")
    elif dzialanie == 4:
        if b == 0:
            print("Cholero nie dziel przez zero!")
        else:
            logging.info(f"Dzielę {a} przez {b}")
            print(f"Wynik to {a / b}")

calculate()
