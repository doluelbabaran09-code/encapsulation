from fan_controller import Fan

def test_fan():
    fan1 = Fan(speed=Fan.FAST, radius=10, color="yellow", on=True)
    fan2 = Fan(speed=Fan.MEDIUM, radius=5, color="blue", on=False)
    
    fan1.display_status(1)
    fan2.display_status(2)

if __name__ == "__main__":
    test_fan()