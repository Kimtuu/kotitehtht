class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

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
                print("Can't go that high")

            elif floor_number > self.top_floor:
                print("Can't go that high")


if __name__ == '__main__':
    hissi = Elevator(1,10)

    hissi.move_to_floor(-1)
# infinite loop for print if floor numbers over or under limit?
