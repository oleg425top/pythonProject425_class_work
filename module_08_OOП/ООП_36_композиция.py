import time


class Tracks:
    def change_direct(self, left, on):
        print('tracks: ', left, on)

class Wheels:
    def change_direct(self, left, on):
        print('wheels: ', left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direct(left, True)
        time.sleep(2)
        self.controller.change_direct(left, False)

tracked = Vehicle(Tracks())
wheeled = Vehicle(Wheels())
tracked.turn(True)
wheeled.turn(False)