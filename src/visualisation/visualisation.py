import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos, sin


class Visualise:
  def __init__(self, mode, a, r0):
    self.mode = mode
    self.a = a
    self.r0 = r0
    self.theta = [i * (np.pi / 180) for i in range(-90,90)]

  def _drum_radius(self, angle):
    if self.mode == "linear":
      if self.a * (angle - pi/2) + self.r0 > 0:
        return self.a * (angle - pi/2) + self.r0
      else:
        return 0

    elif self.mode == "parabolic":
      if self.a * (angle - pi/2)**2 + self.r0 > 0:
        return self.a * (angle - pi/2)**2 + self.r0
      else:
        return 0

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
    plt.axis('equal')
    plt.show()