# Physics class for calculating tension force, torques and equations
# of rotational motion
#
# November 2025
# Kristaps Grava


from math import cos, sin, pi
import config


class Physics:
  def __init__(self, k, b):
    # Mechanism properties
    self.angular_acceleration = 0
    self.angular_velocity = 0
    self.theta = pi/2
    self.torque = 0
    self.tension = 0
    self.k = k
    self.b = b

    self.mass_moment_of_inertia = 0

  def drum_radius(self):
    return self.k*(self.theta-pi/2)+self.b

  def calculate_moment_of_inertia(self):
    self.mass_moment_of_inertia = config.weight_mass*self.drum_radius()**2

  def calculate_tension(self):
    self.tension = config.weight_mass*9.81 - self.angular_acceleration*config.weight_mass*self.drum_radius()
    if self.tension < 0: self.tension = 0

  def calculate_torque(self):
    self.calculate_tension()
    self.calculate_moment_of_inertia()
    self.torque = self.drum_radius()*self.tension + config.hammer_length*9.81*config.hammer_mass*cos(self.theta)

  def rotation_dynamics(self):
    self.angular_acceleration = self.torque/(config.moment_of_inertia+self.mass_moment_of_inertia)
    self.angular_velocity += self.angular_acceleration * config.dt
    self.theta -= self.angular_velocity * config.dt

  def print_values(self):
    print(f"torque: {self.torque}")
    print(f"drum torque: {self.drum_radius()*self.tension}")
    print(f"hammer torque: {config.hammer_length*9.81*config.hammer_mass*cos(self.theta)}")
    print(f"angular velocity: {self.angular_velocity}")
    print(f"angular acceleration: {self.angular_acceleration}")
    print(f"theta: {self.theta}")