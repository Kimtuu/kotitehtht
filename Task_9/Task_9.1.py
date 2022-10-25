#Autoluokka, jossa ominaisuudet; rekkari, huippunopeus, tämänhetkinen nopeus,
#ja kuljettu matka

class Car:
    def __init__ (self, reg, top_speed):
        self.reg = reg
        self.top_speed = top_speed
        self.current_speed = 0
        self.d_travelled = 0

    def print_info(self):
        print(f"Auton {self.reg}, "
              f"huippunopeus on:{self.top_speed}, "
              f"matkamittari: {self.d_travelled}, "
              f"Tämän hetkinen nopeus: {self.current_speed}.")

car1 = Car("ABC-123", 142)
car2 = Car("XYZ-987", 150)

car1.print_info()
car2.print_info()


