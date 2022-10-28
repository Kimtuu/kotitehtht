class House:
    def __init__(self, bottom, top, nbr_of_elevators):
        self.bottom = bottom
        self.top = top
        self.nbr_of_elevators = nbr_of_elevators
        self.elevators = []

        for i in range(nbr_of_elevators):
            self.elevators.append(Elevator(bottom, top, i + 1))

    def use_elevator(self, elevator_number, target_floor):
        hissi = self.elevators[elevator_number - 1]
        hissi.move_to_floor(target_floor)
        print(f"Hissi, joka liikkui:{elevator_number}")

    def print_info(self):
        print(f"Talon alin:{self.bottom}")
        print(f"talon ylin:{self.top}")
        print(f"Hissien määrä:{self.nbr_of_elevators}\n")
        for i in self.elevators:
            i.print_info()

    def fire_alarm(self):
        print("PALOHÄLYTYS")
        for elevator in self.elevators:
            self.use_elevator(elevator.number, self.bottom)


class Elevator:
    def __init__(self, bottom_floor, top_floor, number):
        self.number = number
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def print_info(self):
        print(f"Hissi:{self.number}")
        print(f"Nykyinen kerros:{self.current_floor}\n")

    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print(f"Moving up to floor{self.current_floor}")

    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print(f"Moving down to floor:{self.current_floor}")

    def move_to_floor(self, floor_number):
        if self.current_floor < floor_number <= self.top_floor:
            while self.current_floor < floor_number and self.current_floor <= self.top_floor:
                self.floor_up()

        elif self.current_floor > floor_number >= self.bottom_floor:
            while self.current_floor > floor_number and self.current_floor >= self.bottom_floor:
                self.floor_down()

        else:
            if floor_number < self.bottom_floor:
                print("Can't go that low")

            elif floor_number > self.top_floor:
                print("Can't go that high")


if __name__ == '__main__':
    talo = House(1, 10, 3)
    talo.use_elevator(2, 3)
    talo.use_elevator(1, 2)
    talo.fire_alarm()

