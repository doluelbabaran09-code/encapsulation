class fan:
    SLOW = 1
    MEDIUM = 2
    FAST =  3
    def __init__(self, speed = SLOW, radius: float = 5.0, color: str = "blue", on: bool = False):
        self.__speed = speed
        self.__is_on = on
        self.__radius = float(radius)
        self.__color = color
        