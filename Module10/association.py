class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.floor = bottom_floor
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor

    def go_up(self):
        if self.floor < self.top_floor:
            self.floor += 1
            print(f"Floor {self.floor}")

    def go_down(self):
        if self.floor > self.bottom_floor:
            self.floor -= 1
            print(f"Floor {self.floor}")

    def goto_floor(self, target_floor):
        if self.bottom_floor <= target_floor <= self.top_floor:
            while self.floor != target_floor:
                if self.floor < target_floor:
                    self.go_up()
                elif self.floor > target_floor:
                    self.go_down()


class House:

    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.elevators = []
        for iterator in range(elevator_count):
            self.elevators.append(Elevator(self.bottom_floor, self.top_floor))

    def drive_elevator(self, elevator_id, target_floor):
        self.elevators[elevator_id].goto_floor(target_floor)

    def fire_alarm(self):
        for index, elevator in enumerate(self.elevators):
            self.drive_elevator(index, self.bottom_floor)


new_elevator = Elevator(1, 10)
new_elevator.goto_floor(5)
new_elevator.goto_floor(1)

new_house = House(1, 10, 3)
new_house.drive_elevator(0, 3)
new_house.drive_elevator(2, 10)
new_house.drive_elevator(1, 7)

new_house.fire_alarm()
