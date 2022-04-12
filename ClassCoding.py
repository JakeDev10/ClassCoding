class Animal:
    """Animal class"""
    def __init__(self, genus, species, color):
        self.__genus = genus
        self.__species = species
        self.__color = color

    def move(self):
        print(f'{self.__species} is moving')
    
    def eat(self):
        print(f'{self.__species} is eating')

    def sleep(self):
        print(f'{self.__species} is sleeping')

class Book:
    """Books class"""
    def __init__(self, title, author, genre):
        self.__author = author
        self.__genre = genre
        self.__title = title
    
    def title(self):
        print(f"My title is {self.__title}")

    def restock(self):
        print("There's more stock")

    def sell(self):
        print("There's less stock")

class Vehicle:
    """Vehicle class"""
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def accelerate(self):
        print("*zoom*")

    def brake(self):
        print("skrrrrrrrt")

class Fish(Animal):
    def __init__(self,genus,species,color):
        super().__init__(genus, species, color)
        self.__species = species        #Example of using attribute of superclass

    def move(self):                     #Example of polymorphism, overwriting parent's move()
        print(f"{self.__species} is swimming")

class Snake(Animal):
    def shed(self):
        print("Snake has shed")

class Person(Animal):
    def write(self):
        print("Look ma, I have opposable thumbs!")

class Textbook(Book):
    def __init__(self, title, author, genre, subject):
        super().__init__(title, author, genre)
        self.__subject = subject

class AddressBook(Book):
    def __init__(self, title, author, genre, region):
        super().__init__(title, author, genre, region)
        self.__region = region

class Car(Vehicle):
    def honk():
        print("Honk honk")

    def blinker(self):
        print("tick tock")

class Bicycle(Vehicle):
    def popWheelie():
        print("Totally radical bro")

class Boat(Vehicle):
    def __init__(self, make, model, year, boatClass):
        super().__init__(make, model, year)
        self.__boatClass = boatClass

class HotAirBalloon(Vehicle):
    def vent():
        print("We're descending")


fishie = Fish('aGenus','someFish','someColor')
fishie.move()           #Example of referencing superclass attribute and polymorphism