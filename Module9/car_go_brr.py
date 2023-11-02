import random
from tabulate import tabulate


class Auto:

    def __init__(self, licence_number, top_speed):
        self.licence_number = licence_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, amount):
        changed_speed = self.current_speed + amount
        if 0 >= changed_speed:
            self.current_speed = 0
        elif changed_speed >= self.top_speed:
            self.current_speed = self.top_speed
        else:
            self.current_speed = changed_speed

    def travel(self, hours):
        self.travelled_distance += self.current_speed * hours


class Electric(Auto):
    def __init__(self, licence_number, top_speed, capacity):
        super().__init__(licence_number, top_speed)
        self.battery_capacity = capacity

    def consume_fuel(self):
        self.battery_capacity -= self.current_speed / 7
    pass


class Combustion(Auto):
    def __init__(self, licence_number, top_speed, volume):
        super().__init__(licence_number, top_speed)
        self.tank_volume = volume

    def consume_fuel(self):
        self.tank_volume -= self.current_speed / 14


class Race:  # 0_O
    total_hours = 0

    def __init__(self, name, km_amount, cars):
        self.name = name
        self.km_amount = km_amount
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            if (
                    car.__class__.__name__ == "Electric" and car.battery_capacity > 0 or
                    car.__class__.__name__ == "Combustion" and car.tank_volume > 0 or
                    car.__class__.__name__ == "Auto"
            ):
                car.accelerate(random.randint(-10, 15))
                car.travel(1)
                if car.__class__.__name__ != "Auto":
                    car.consume_fuel()
            else:
                car.current_speed = 0
        self.total_hours += 1

    def print_standings(self):
        sorted_cars = sorted(self.cars, key=lambda x: x.travelled_distance, reverse=True)
        table_data = []
        for i, car in enumerate(sorted_cars):
            car_info = {'Place': f"{i + 1}"}
            car_info.update(vars(car))
            table_data.append(car_info)
        if any(car.travelled_distance >= self.km_amount for car in self.cars):
            print(f"{self.name} is over! The final standings:")
        else:
            print(f"{self.name} - Standings after {self.total_hours} hours:")
        print(tabulate(table_data, headers="keys", tablefmt="pretty"))

    def race_over(self):
        if (
            any(car.travelled_distance >= self.km_amount for car in self.cars)
            or (all(hasattr(car, "battery_capacity") and car.battery_capacity <= 0 or
                    hasattr(car, "tank_volume") and car.tank_volume <= 0 for car in self.cars))
        ):
            self.print_standings()
            return True
        else:
            return False


def init_demolition_derby():
    race_cars = []
    for iterator in range(10):
        race_cars.append(Auto(f"ABC-{iterator + 1}", random.randint(100, 200)))
    demolition_derby = Race("The Great Demolition Derby", 8000, race_cars)
    iterator = 1
    while not demolition_derby.race_over():
        demolition_derby.hour_passes()
        if iterator % 10 == 0:
            demolition_derby.print_standings()
        iterator += 1


def init_mixec_car_endurance_race():
    race_cars = []
    for iterator in range(10):
        if random.randint(0,1) == 1:
            race_cars.append(Electric(f"EV-{iterator + 1}", random.randint(100, 200), random.randint(50, 100)))
        else:
            race_cars.append(Combustion(f"ABC-{iterator + 1}", random.randint(100, 200), random.randint(40, 80)))
    endurance_race = Race("The Unfair Advantage", 9999999, race_cars)
    while not endurance_race.race_over():
        endurance_race.hour_passes()
        endurance_race.print_standings()


# init_demolition_derby()
init_mixec_car_endurance_race()
