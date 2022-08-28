import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("star_with_gravity.csv")

dist = df['Distance'].to_list()
grav = df['Gravity'].to_list()

suitable = [] #We will leave suitable planet list as it is
temp_goldilock_planets = list(df) 
for planet_data in temp_goldilock_planets:
  if planet_data[2] <= 100 and planet_data[5] > 2:
    suitable.append(planet_data)
