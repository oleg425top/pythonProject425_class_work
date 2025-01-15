import time
class Vehicle:
    def change_direction(self):
        pass

    def turn(self):
        self.change_direction(self, True)
        time.sleep(0.5)
        self.change_direction(self, False)


class TrackVehicle(Vehicle):
    def control_track(self, stop):
        pass
    def change_direction(self, on):
        self.control_track()



class WheledVehicle:
    def turn_front_wheels(self, on):
        pass

