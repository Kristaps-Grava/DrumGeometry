# Program for calculating the optimal drum geometry for the hammer design
#
# November 2025
# Kristaps Grava


from core.simulation import Simulation


sim = Simulation(k=0, b=0.07)

final_angular_velocity = sim.run()

print(final_angular_velocity)