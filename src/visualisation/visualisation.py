import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin


class Visualise:
  def __init__(self, k, b):
    self.k = k
    self.b = b
    self.theta = [i * (np.pi / 180) for i in range(180)]

  def _drum_radius(self, angle):
    return self.k * (angle - pi / 2) + self.b

  def plot_drum(self):
    x = [cos(angle) * self._drum_radius(angle) for angle in self.theta]
    y = [sin(angle) * self._drum_radius(angle) for angle in self.theta]

    plt.title("Most optimal drum geometry")
    plt.xlabel("X position, m")
    plt.ylabel("Y position, m")
    plt.plot(x, y, color = "blue")
    plt.fill_between(x,y,color = "cyan")
    plt.plot([-0.001,0.001],[0,0], color="red")
    plt.plot([0, 0],[-0.001, 0.001], color="red")
    plt.show()