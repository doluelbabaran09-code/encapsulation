from fan_controller import Fan


def display_status(self, fan_id):
    status = "ON" if self.get_is_on() else "OFF"
    speed_map = {1: SLOW, 2:MEDIUM, 3: FAST}
    speed = speed_map.get(self.get_speed(), UNKNOWN)
    

