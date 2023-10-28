import random
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


new_car = Auto("ABC-123", 142)
car_properties = vars(new_car)
print(f"New car has these attributes:")
for car_property, value in car_properties.items():
    print(f"{car_property:<20}: {value}")
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print(new_car.current_speed)
new_car.accelerate(-200)
print(new_car.current_speed)
cars = []
for iterator in range(10):
    cars.append(Auto(f"ABC-{iterator+1}", random.randint(100, 200)))
while True:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.travel(1)
    if any(car.travelled_distance >= 10000 for car in cars):
        break

sorted_cars = sorted(cars, key=lambda x: x.travelled_distance, reverse=True)
for i, car in enumerate(sorted_cars):
    if i + 1 == 1:
        print(f"{i+1}st place:")
        for car_property, value in vars(car).items():
            print(f"{car_property:<20}: {value}")
    elif i + 1 == 2:
        print(f"{i + 1}nd place:")
        for car_property, value in vars(car).items():
            print(f"{car_property:<20}: {value}")
    elif i + 1 == 3:
        print(f"{i + 1}rd place:")
        for car_property, value in vars(car).items():
            print(f"{car_property:<20}: {value}")
    else:
        print(f"{i + 1}th place:")
        for car_property, value in vars(car).items():
            print(f"{car_property:<20}: {value}")

