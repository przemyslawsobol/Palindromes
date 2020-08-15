import logging
logging.basicConfig(level=logging.DEBUG)



def calculate():
    dzialanie = int(input("Podaj działanie posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    a = int(input("Podaj pierwszy składnik: "))
    b =  int(input("Podaj drugi składnik: "))
    if dzialanie == 1:
        trzeci = input("Czy chcesz dodać trzeci składnik? Y/N: ")
        if trzeci == "Y":
            c = int(input("Podaj trzeci składnik: "))
            logging.info(f"Dodaję {a}, {b} i {c}")
            result = a + b + c
        else:
            logging.info(f"Dodaję {a} i {b}")
            result = a + b
    elif dzialanie == 2:
        logging.info(f"Od {a} odejmuję {b} ")
        result = a - b
    elif dzialanie == 3:
        trzeci = input("Czy chcesz dodać trzeci składnik? Y/N: ")
        if trzeci == "Y":
            c = int(input("Podaj trzeci składnik: "))
            logging.info(f"Mnożę {a}, {b} i {c}")
            result = a * b * c
        else:
            logging.info(f"Mnożę {a} i {b}")
            result = a * b
    elif dzialanie == 4:
        if b == 0:
            print("Cholero nie dziel przez zero!")
        else:
            logging.info(f"Dzielę {a} przez {b}")
            result = a / b
    else:
        print("Nie rozpoznano działania")
    print(f"Wynik to {result}")

calculate()
