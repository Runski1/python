import math
import numpy
from tabulate import tabulate


# Tehtävä 1


def rad2deg(angles):
    degrees = []
    for alfa in angles:
        degrees.append(round(((alfa * 360) / (2 * math.pi)), 3))
    return degrees


def deg2rad(angles):
    rads = []
    for alfa in angles:
        rads.append(round((alfa * 2 * math.pi) / 360, 3))
    return rads


def create_list():
    angles = []
    print("Input angles. To stop adding angles input empty row.")
    while True:
        user_input = input("Angle: ")
        if user_input != "":
            angles.append(float(user_input))
        else:
            break
    return angles


# if input("Input R to convert rads to degrees. anything else for deg>rad: ").lower() == "r":
#     angles = create_list()
#     converted = rad2deg(angles)
# else:
#     angles = create_list()
#     converted = deg2rad(angles)
# table = [angles, converted]
# print(tabulate(table, tablefmt="rounded_outline"))

#Jos ne pitää olla valmiiksi laskettuna niin:
list1 = [2.493, 0.911]
list2 = [137.7, 62.3]
print(tabulate([list1, rad2deg(list1)]))
print(tabulate([list2, deg2rad(list2)]))

# Tehtävä 2
print(numpy.hypot(1.6, 2.3))
