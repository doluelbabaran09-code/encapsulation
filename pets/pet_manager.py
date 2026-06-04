class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0
    def set_name(self, name: str):
        self.__name = name
    def set_animal_type(self, animal_type: str):
        self.__animal_type = animal_type
    def set_age(self, age: int):
        self.__age = age

    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
    
    def display_pet_id(self):
        print("\n" "="*40)
        print(f" 🐾 VIRTUAL PET ID CARD 🐾".center(40))
        print("="*40)
        print(f"║ Name    : {self.get_name()}")
        print(f"║ Type    : {self.get_animal_type()}")
        print(f"║ Age     : {self.get_age()} years old")
        print("="*40 + "\n")
