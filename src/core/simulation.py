# Simulation class for interacting with the physics class and
# performing the main loop of the simulation
#
# November 2025
# Kristaps Grava


from core.physics import Physics
from math import pi

class Simulation:
  def __init__(self, mode, a, r0):
    self.physics = Physics(mode, a, r0)

  def run(self):
    while self.physics.theta > -pi/2:
      self.physics.calculate_torque()
      self.physics.rotation_dynamics()
    return self.physics.angular_velocity
