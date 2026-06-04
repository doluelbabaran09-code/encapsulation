from pet_manager import Pet
def register_pet():
    my_pet = Pet()
    print("\n ---- Welcome to the Virtual Pet Registration! ----")
    user_name = input("Enter your pet's name: ")
    user_type = input("Enter your pet's type (e.g., Dog, Cat, Bird): ")

    while True:
        try:
            use_age = int(input("Enter your pet's age in years: "))
            break
        except ValueError:
            print("Please enter a valid integer for the age.")
    
    my_pet.set_name(user_name)
    my_pet.set_animal_type(user_type)
    my_pet.set_age(use_age)

    print("\n Generating your pet's ID card...")
    my_pet.display_pet_id()

if __name__ == "__main__":
    register_pet()