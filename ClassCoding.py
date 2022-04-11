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

class Books:
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
        print("Vroom vroom")

    def brake(self):
        print("skrrrrrrrt")

    def blinker(self):
        print("tick tock")


snake = Animal('Thamnophis', 'couchii', 'black')
snake.move()
snake.eat()

myCar = Vehicle("Nissan", "Altima", "some year")
myCar.accelerate()
myCar.brake()