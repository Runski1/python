import numpy as np  # Miksi ihmeessä numpylle käytetään aina np-aliasta? Olisivat nimenneet koko moduulin sitten np
from matplotlib import pyplot as plt, patches
import math
fig = plt.figure()
ax = fig.subplots()
circle = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(circle)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.axis('equal')
plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])
angles = [30, 45, 60, 90, 120, 150, 180, 270]
my_array = np.array([])
for angle in angles:
    new_angle = math.radians(angle)
    print(new_angle)
    my_array = (np.append(my_array, [math.cos(new_angle), math.sin(new_angle)]))
my_array = my_array.reshape(-1, 2)
plt.scatter(my_array[:, 0], my_array[:, 1], marker='x', c='red')
print(my_array)
plt.show()
