from car_simulator import Car

def test_car():
    my_car = Car(2026, "Nissan Skyline")
    print(f"--- Starting {my_car.get_year_model()} {my_car.get_make()} ---\n")
    for _ in range(5):
        my_car.accelerate()
        my_car.print_dashboard("Accelerate")
    
    print("\n--- Applying brakes ---\n")
    for _ in range(5):
        my_car.brake()
        my_car.print_dashboard("Applying Brakes")
if __name__ == "__main__":
    test_car()