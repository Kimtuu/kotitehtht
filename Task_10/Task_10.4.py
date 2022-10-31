from random import randint


class Race:

    def __init__(self, race_name, distance, participants):
        self.race_name = race_name
        self.distance = distance
        self.participants = participants

    def hour_pass(self):
        for car in self.participants:
            car.accelerate(randint(-10, 15))
            car.travel(1)

    def print_status(self):
        for car in self.participants:
            car.print_info()

    def race_over(self):
        for car in self.participants:
            if car.tripmeter >= self.distance:
                return True
            else:
                continue


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


if __name__ == '__main__':
    cars = []
    for i in range(10):
        cars.append(Car("ABC-" + str(i + 1), randint(100, 200)))

    name = "Suuri romuralli"
    race_distance = 8000

    race = Race(name, race_distance, cars)

    hour = 0

    while True:
        race.hour_pass()

        if race.race_over():
            print("Kilpailu päättyi!\n")
            race.print_status()
            break

        else:
            hour += 1

            if hour % 10 == 0:
                print(f"Tunteja:{hour}\n")
                race.print_status()

            else:
                continue

""""
stop = False
while not stop:
    for Car in cars:
        Car.accelerate(randint(-10, 15))
        Car.travel(1)
        if Car.tripmeter >= 10000:
            stop = True
            break
"""
