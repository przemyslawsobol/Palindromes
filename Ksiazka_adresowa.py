
from faker import Faker
from faker.providers import person
from faker.providers import address
from faker.providers import phone_number
from faker.providers import internet
from faker.providers import company
from faker.providers import job
fake = Faker()

class BaseContact:
    def __init__(self, name, surname, email, phone):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.label_lenght = len(self.name + ' ' + self.surname)


    def contact(self):
        return print(f'Wybieram numer {self.phone} i dzwonię do {self.name} {self.surname}')

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.email}, {self.phone}'

    def __repr__(self):
        return repr((self.name, self.surname, self.email, self.phone))

 
    

class BusinessContact(BaseContact):
    def __init__(self, company, position, job_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.job_phone = job_phone
        self.label_lenght = len(self.name + ' ' + self.surname)
    
    
    def contactBusiness(self):
        return print(f'Wybieram numer {self.job_phone} i dzwonię do {self.name} {self.surname}')
    def __str__(self):
        return f'{self.name}, {self.surname}, {self.email}, {self.phone}, {self.company}, {self.position}, {self.job_phone}'

    def __repr__(self):
        return repr((self.name, self.surname, self.email, self.phone, self.company, self.position, self.job_phone))

    



first_A = BaseContact(name = "Beatrycze", surname = "Walczak", email = "BeatryczeKaminska@teleworm.us", phone = "+48 60 929 64 64")
second_A = BaseContact(name = "Rościsław", surname = "Wieczorek", email = "RoscislawZajac@rhyta.com", phone = "+48 60 519 24 51")
third_A = BaseContact(name = "Hendrych", surname = "Dąbrowski", email = "HendrychMajewski@jourrapide.com", phone = "+48 66 377 39 80")
fourth_A = BaseContact(name = "Tomica", surname = "Ivanec", email = "TomicaJerkovic@rhyta.com", phone = "+48 78 559 38 98")
fifth_A = BaseContact(name = "Jana", surname = "Brkic", email = "JanaPopovic@rhyta.com", phone = "+48 88 189 96 09")

first_B = BusinessContact(name = "Beatrycze", surname = "Walczak", company = "Buena Vista Realty Service", position = "Carpenter", email = "BeatryczeKaminska@teleworm.us", job_phone = "+48 60 749 79 70", phone = "+48 60 929 64 64" )
second_B = BusinessContact(name = "Rościsław", surname = "Wieczorek", company = "Farmer Jack", position = "Packaging and filling machine operator", email = "RoscislawZajac@rhyta.com", job_phone = "+48 69 692 14 24", phone = "+48 60 519 24 51")
third_B = BusinessContact(name = "Hendrych", surname = "Dąbrowski", company = "AJ Bayless", position = "Roof Bolter", email = "HendrychMajewski@jourrapide.com", job_phone = "+48 79 697 25 10", phone = "+48 66 377 39 80")
fourth_B = BusinessContact(name = "Tomica", surname = "Ivanec", company = "System Star Solutions", position = "Budget manager", email = "TomicaJerkovic@rhyta.com", job_phone = "+48 60 182 24 40", phone = "+48 78 559 38 98" )
fifth_B = BusinessContact(name = "Jana", surname = "Brkic", company = "Joseph Magnin", position = "Forest fire inspector", email = "JanaPopovic@rhyta.com", job_phone = "+48 72 801 17 69", phone = "+48 88 189 96 09")





def create_contacts(klasa, i):
    for i in range(0, i):
        klasy_dict = {
    "BaseContact" : BaseContact(name = fake.first_name(), surname =  fake.last_name(), email = fake.email(), phone =  fake.phone_number()),
    "BusinessContact" : BusinessContact(name = fake.first_name(), surname =  fake.last_name(), email = fake.email(), phone =  fake.phone_number(), company = fake.company(), position = fake.job(), job_phone = fake.phone_number()  )
        }
        fakeperson = klasy_dict[klasa]
        print(fakeperson)
        

create_contacts('BaseContact', 5)
