from random import randint


class Car:

    def __init__(self, reg, top_speed):
        self.reg = reg
        self.top_speed = top_speed
        self.speed = 0
        self.tripmeter = 0

    def print_info(self):
        print(f"Auton {self.reg}, "
              f"huippunopeus on:{self.top_speed}Km/h, "
              f"matkamittari: {self.tripmeter:.1f}Km, "
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


# generoidaan 10 autoa

cars = []
for i in range(10):
    cars.append(Car("ABC-" + str(i + 1), randint(100, 201)))
    #for car in cars:
    #    print(car.print_info())

for Car in cars:
    while Car.tripmeter <= 10000:
        for Car in cars:
            Car.accelerate(randint(-10, 15))
            Car.travel(1)
            if Car.tripmeter >= 10000:
                break

for car in cars:
    print(car.print_info())
