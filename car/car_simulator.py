import time
class Car:
    def __init__(self, year_model: int, make: str):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0 
    
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0
    
    def get_speed(self):
        return self.__speed
    def get_year_model(self):
        return self.__year_model
    def get_make(self):
        return self.__make

    def print_dashboard(self, action: str):
        bar_count = self.__speed // 5
        speed_bar = "█" * bar_count + "-" * (10 - bar_count)
        print(f"{action:^12}] Speed: [{speed_bar}] {self.__speed: 02d} mph")
        time.sleep(0.3)
    

