class Vehicle:
    def __init__(self, speed):
        self.speed = speed


class SportsEquipment:
    def __init__(self, weight):
        self.weight = weight


class Bicycle(Vehicle, SportsEquipment):
    def __init__(self, speed, weight, gears):
        Vehicle.__init__(self, speed)
        SportsEquipment.__init__(self, weight)

        self.gears = gears


bc = Bicycle(45, 18.7, 4)
print(bc.gears)
print(bc.speed)
print(bc.weight)
