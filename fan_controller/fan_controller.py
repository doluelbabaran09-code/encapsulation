class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST =  3
    def __init__(self, speed = SLOW, radius: float = 5.0, color: str = "blue", on: bool = False):
        self.__speed = speed
        self.__is_on = on
        self.__radius = float(radius)
        self.__color = color

    def get_speed(self):
        return self.__speed
    def get_is_on(self):
        return self.__is_on
    def get_radius(self):
        return self.__radius
    def get_color(self):
        return self.__color
    
    def set_speed(self, speed: int):
        self.__speed= speed
    def set_is_on(self, on: bool):
        self.__is_on = on
    def set_radius(self, radius: float):
        self.__radius = radius
    def set_color(self, color: str):
        self.__color = color

    def display_status(self, fan_id):
        status = "ON" if self.get_is_on() else "OFF"
        speed_map = {1: "SLOW", 2: "MEDIUM", 3: "FAST"}
        speed = speed_map.get(self.get_speed(), "UNKNOWN")
        
        print(f"===== Fan {fan_id} Status =====")
        print(f" Power  : {'ON' if self.get_is_on() else 'OFF'}")
        print(f" Speed  : {speed} (Level {self.get_speed()})")
        print(f" Radius : {self.get_radius()} inches")
        print(f" Color  : {self.get_color()}")
