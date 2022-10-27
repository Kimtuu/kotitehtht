from random import randint


class Car:

    def __init__(self, reg, top_speed):
        self.reg = reg
        self.top_speed = top_speed
        self.speed = 0
        self.tripmeter = 0

    def print_info(self):
        print(f"Auton {self.reg:6}; "
              f"huippunopeus on:{self.top_speed:0}Km/h, "
              f"matkamittari: {self.tripmeter:5}Km, "
              f"Tämän hetkinen nopeus: {self.speed}Km/h")

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change <= self.top_speed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0
        elif self.speed + speed_change > self.top_speed:
            self.speed = self.top_speed

    def travel(self, hours):
        if hours < 0:
            self.tripmeter = self.tripmeter
        elif hours > 0:
            self.tripmeter = self.tripmeter + (self.speed * hours)


cars = []
for i in range(1, 11):
    cars.append(Car("ABC-" + str(i), randint(100, 200)))

stop = False
while not stop:
    for Car in cars:
        Car.accelerate(randint(-10, 15))
        Car.travel(1)
        if Car.tripmeter >= 10000:
            stop = True
            break
""""
for Car in cars:
    while Car.tripmeter <= 10000:
        for Car in cars:
            Car.accelerate(randint(-10, 15))
            Car.travel(1)
            if Car.tripmeter >= 10000:
                break
"""
for Car in cars:
    Car.print_info()
