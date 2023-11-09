import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3 * np.pi, 3 * np.pi, 100, endpoint=True)
C, S = np.cos(X), np.sin(X)
fig = plt.figure(figsize=(19.5, 15))
ax = fig.subplots()
xticks_values = np.arange(-3 * np.pi, 3 * np.pi + 1e-9, np.pi / 2)
xticks_labels = ['-3π', '-5π/2', '-2π', '-3π/2', '-π', '-π/2', '0', 'π/2', 'π', '3π/2', '2π', '5π/2', '3π']
plt.plot(X, C, 'c--', linewidth=3, xunits='radians')
plt.plot(X, S, 'm:', linewidth=3)
plt.xticks(xticks_values, xticks_labels)
plt.show()
