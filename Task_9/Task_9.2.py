class Car:
    def __init__ (self, reg, top_speed):
        self.reg = reg
        self.top_speed = top_speed
        self.current_speed = 0
        self.d_travelled = 0

    def print_info(self):
        print(f"Auton {self.reg}, "
              f"huippunopeus on:{self.top_speed}Km/h, "
              f"matkamittari: {self.d_travelled}Km, "
              f"Tämän hetkinen nopeus: {self.current_speed}Km/h")

    def accelerate(self, speed_change):
        if 0 < self.current_speed + speed_change <= self.top_speed:
            self.current_speed = self.current_speed + speed_change
        elif: self.current_speed + speed_change <= 0
            self.current_speed = 0
        #TODO: jos uusinopeus > maksimi: nopeus = maksimi

car1 = Car("ABC-123", 142)
car2 = Car("XYZ-987", 150)
car1.accelerate(2330)
car1.print_info()
car1.accelerate(15)
car1.print_info()
car1.accelerate(-200)
car1.print_info()

#car2.print_info()


