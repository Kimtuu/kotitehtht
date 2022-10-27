class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor != self.top_floor:
            self.current_floor = self.current_floor + 1
            print(f"Moving up to floor:{self.current_floor}")
        elif self.current_floor >= self.bottom_floor:
            print("Can't go higher")

    def floor_down(self):
        if self.current_floor != self.bottom_floor:
            self.current_floor = self.current_floor - 1
            print(f"Moving down to floor:{self.current_floor}")
        elif self.current_floor <= self.bottom_floor:
            print("Can't go lower")

    def move_to_floor(self, floor_number):
        if self.current_floor > floor_number:
            while self.current_floor > floor_number:
                self.floor_down()
        elif self.current_floor < floor_number:
            while self.current_floor < floor_number:
                self.floor_up()


elevator = Elevator(1, 10)

elevator.move_to_floor(3)
elevator.move_to_floor(1)

# infinite loop for print if floor numbers over or under limit?
