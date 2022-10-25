# Autoluokka, jossa ominaisuudet; rekkari, huippunopeus, tämänhetkinen nopeus,
# ja kuljettu matka

class Car:
    def __init__(self, registerplate, top_speed):
        self.reg = registerplate
        self.top_speed = top_speed
        self.speed = 0
        self.Tripmeter = 0

    def print_info(self):
        print(f"Auton {self.reg}, "
              f"huippunopeus on:{self.top_speed}, "
              f"matkamittari: {self.Tripmeter}, "
              f"Tämän hetkinen nopeus: {self.speed}.")


car1 = Car("ABC-123", 142)
car2 = Car("XYZ-987", 150)

car1.print_info()
car2.print_info()
