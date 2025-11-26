# Program for calculating the optimal drum geometry for the hammer design
#
# November 2025
# Kristaps Grava


from core.simulation import Simulation

# k and b are values determining the shape of the spiral. for example k=0 means
# that radius is constant. k=0.01 would mean that for every radian the radius decreases by 1 cm
sim = Simulation(k=0, b=0.07)

final_angular_velocity = sim.run()

print(final_angular_velocity)