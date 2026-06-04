
class Car:
    def __init__(self, year_model: int, make: str):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0 
    
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
        else:
            self.__speed = 0
    