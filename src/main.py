# Program for calculating the optimal drum geometry for the hammer design
#
# November 2025
# Kristaps Grava


from core.simulation import Simulation
import numpy as np

results = []

# k and b are values determining the shape of the spiral. for example k=0 means
# that radius is constant. k=0.01 would mean that for every radian the radius decreases by 1 cm
for k in np.linspace(-0.03, 0.03, num=100):
  sim = Simulation(k, b=0.1)
  results.append([k, sim.run()])

best_row = max(results, key=lambda row: row[1])
print(best_row)