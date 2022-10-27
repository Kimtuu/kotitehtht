class House:
    def __init__(self, bottom_floor, top_floor, elevator_number):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator_number = elevator_number
        self.elevator = []

        for i in range(elevator_number):
            self.elevator.append(Elevator(bottom_floor, top_floor))

    def use_elevator(self, elevator_number, target_floor):

        pass



class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = bottom
        self.top_floor = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor != self.top_floor:
            self.current_floor = self.current_floor + 1
            print(f"Moving up to floor:{self.current_floor}")
        elif self.current_floor >= self.bottom_floor:
            print("No more floors up that way")
            # return self.current_floor

    def floor_down(self):
        if self.current_floor != self.bottom_floor:
            self.current_floor = self.current_floor - 1
            print(f"Moving down to floor:{self.current_floor}")
        elif self.current_floor <= self.bottom_floor:
            print(f'No more floors down that way')
            # return self.current_floor

    def move_to_floor(self, floor_number):
        if self.current_floor > floor_number:
            while self.current_floor > floor_number:
                self.floor_down()
        elif self.current_floor < floor_number:
            while self.current_floor < floor_number:
                self.floor_up()

elevator = Elevator
talo = House(1, 2, 3)
print(talo)
