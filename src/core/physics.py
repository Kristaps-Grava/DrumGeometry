# Physics class for calculating tension force, torques and equations
# of rotational motion
#
# November 2025
# Kristaps Grava


from math import cos, sin, pi
import config


class Physics:
  def __init__(self, mode, a, r0):
    # Mechanism properties
    self.angular_acceleration = 0
    self.angular_velocity = 0
    self.theta = pi/2
    self.torque = 0
    self.tension = 0
    self.mode = mode

    self.a = a
    self.r0 = r0

    self.mass_moment_of_inertia = 0

  def drum_radius(self):
    if self.mode == "linear":
      if self.a*(self.theta-pi/2)+self.r0 > 0:
        return self.a*(self.theta-pi/2)+self.r0
      else: return 0

    elif self.mode == "parabolic":
      if self.a * (self.theta-pi/2)**2 + self.r0 > 0:
        return self.a * (self.theta-pi/2)**2 + self.r0
      else: return 0

  def calculate_moment_of_inertia(self):
    self.mass_moment_of_inertia = config.weight_mass*self.drum_radius()**2

  def calculate_tension(self):
    self.tension = config.weight_mass*9.81 - self.angular_acceleration*config.weight_mass*self.drum_radius()
    if self.tension < 0: self.tension = 0

  def calculate_torque(self):
    self.calculate_tension()
    self.calculate_moment_of_inertia()

    drum_torque = self.drum_radius()*self.tension
    hammer_torque = config.hammer_length*9.81*config.hammer_mass*cos(self.theta)
    self.torque = drum_torque + hammer_torque

  def rotation_dynamics(self):
    """Apply equations of rotation"""
    # α = τ / (I_h + m*r**2)
    self.angular_acceleration = self.torque/(config.moment_of_inertia+self.mass_moment_of_inertia)
    # ω = ω + α * dt
    self.angular_velocity += self.angular_acceleration * config.dt
    # θ = θ - ω * dt
    self.theta -= self.angular_velocity * config.dt
    #print(self.drum_radius())

  def print_values(self):
    print(f"torque: {self.torque}")
    print(f"drum torque: {self.drum_radius()*self.tension}")
    print(f"hammer torque: {config.hammer_length*9.81*config.hammer_mass*cos(self.theta)}")
    print(f"angular velocity: {self.angular_velocity}")
    print(f"angular acceleration: {self.angular_acceleration}")
    print(f"theta: {self.theta}")