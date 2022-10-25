class Car:

    def __init__(self, reg, top_speed):
        self.reg = reg
        self.top_speed = top_speed
        self.speed = 0
        self.tripmeter = float(0)

    def print_info(self):
        print(f"Auton {self.reg}, "
              f"huippunopeus on:{self.top_speed}Km/h, "
              f"matkamittari: {self.tripmeter:.1f}Km, "
              f"Tämän hetkinen nopeus: {self.speed}Km/h")

    # muokattu self.tripmeter tulostamaan yhden desimaalin tarkkuudella

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


car1 = Car("ABC-123", 142)
car1.tripmeter = 2000
car1.accelerate(60)
car1.travel(1.5)
car1.print_info()
# -> printtaa: Auton ABC-123, huippunopeus on:142Km/h, matkamittari: 2090.0Km, Tämän hetkinen nopeus: 60Km/h
