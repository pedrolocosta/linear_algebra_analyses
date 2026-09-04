'''In a given area of ​​Manhattan, we will find the closest taxi out of 
three available. Declared variables:
	• avenues_df — list of avenues with coordinates
	• streets_df — list of streets with coordinates
	• address — customer location (avenue and street)
	• taxis — location of taxis
Calculate the distances and store the result in the taxis_distance 
variable. Determine the serial number of the nearest taxi. Print the 
car's location (avenue and street) on the screen.'''

# Importing libraries
import numpy as np
import pandas as pd
from scipy.spatial import distance

# Data for avenues and streets
avenues_df = pd.DataFrame(
    [0, 153, 307, 524], index=['Park', 'Lexington', '3rd', '2nd'], columns=['Distance']
)
streets_df = pd.DataFrame(
    [0, 81, 159, 240, 324], index=['76', '75', '74', '73', '72'], columns=['Distance']
)

# Declaring the address and taxis
address = ['Lexington', '74']
taxis = [
    ['Park', '72'],
    ['2nd', '75'],
    ['3rd', '76'],
]

# Address position vector
address_vector = np.array(
    [avenues_df.loc[address[0], 'Distance'], streets_df.loc[address[1], 'Distance']])

# Taxi position vector
taxi_position = []
for taxi in taxis:
    position = np.array([avenues_df.loc[taxi[0], 'Distance'],
                        streets_df.loc[taxi[1], 'Distance']])
    taxi_position.append(position)

# Calculating the Manhattan distance between the address and each taxi
taxi_distances = []
for position in range(len(taxi_position)):
    calc = distance.cityblock(address_vector, taxi_position[position])
    taxi_distances.append(calc)

# Finding the nearest taxi and printing its location
index = np.argmin(taxi_distances)
print(taxis[index])
