class Car:

    def __init__(self, reg, top_speed):
        self.reg = reg
        self.top_speed = top_speed
        self.speed = 0
        self.tripmeter = 0

    def print_info(self):
        print(f"Auton {self.reg}, "
              f"huippunopeus on:{self.top_speed}Km/h, "
              f"matkamittari: {self.tripmeter}Km, "
              f"Tämän hetkinen nopeus: {self.speed}Km/h")

    def accelerate(self, speed_change):
        if 0 < self.speed + speed_change <= self.top_speed:
            self.speed = self.speed + speed_change
        elif self.speed + speed_change <= 0:
            self.speed = 0
        elif self.speed + speed_change > self.top_speed:
            self.speed = self.top_speed


car1 = Car("ABC-123", 142)

car1.accelerate(30)
car1.print_info()
car1.accelerate(70)
car1.print_info()
car1.accelerate(50)
car1.print_info()
car1.accelerate(-200)
car1.print_info()
