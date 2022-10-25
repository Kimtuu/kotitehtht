#Autoluokka, jossa ominaisuudet; rekkari, huippunopeus, tämänhetkinen nopeus,
#ja kuljettu matka

class Car:
    def __init__ (self, reg, top_speed, current_speed, d_travelled):
        self.reg = reg
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.d_travelled = d_travelled

    def printcar(self):
        print(self.reg,self.top_speed,self.current_speed,self.d_travelled)

newcar = Car("ABC-123", 142, 0, 0)
oldcar = Car("LVG-933,", 120, 0, 0)

newcar.printcar()
oldcar.printcar()