# Classes

class Car:
    # Constructor
    def __init__(self, color, combustible):
        self.color = color
        self.combustible = combustible

    def paint_car(self, color):
        self.color = color

    def turn_on_car(self):
        self.combustible += 10

    @staticmethod
    def turn_on_sound(self):
        print('ringggggg!')


teslaModel3 = Car("Black")
teslaModel3.turn_on_sound()
# print(teslaModel3.color)
