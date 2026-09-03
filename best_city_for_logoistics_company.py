'''
You know the number of deliveries per week for each city. Using all this 
information, you can select the best city to create the Things Voadoras 
warehouse.

Find the city with the shortest total distance in the region.'''

# import libraries
import numpy as np
import pandas as pd
from scipy.spatial import distance

# Data for the cities
x_axis = np.array([0., 0.18078584, 9.32526599, 17.09628721,
                   4.69820241, 11.57529305, 11.31769349, 14.63378951])

y_axis = np.array([0.0, 7.03050245, 9.06193657, 0.1718145,
                   5.1383203, 0.11069032, 3.27703365, 5.36870287])

deliveries = np.array([5, 7, 4, 3, 5, 2, 1, 1])

town = [
    'Willowford',
    'Otter Creek',
    'Springfield',
    'Arlingport',
    'Spadewood',
    'Goldvale',
    'Bison Flats',
    'Bison Hills',
]

data = pd.DataFrame(
    {
        'x_coordinates_km': x_axis,
        'y_coordinates_km': y_axis,
        'Deliveries': deliveries,
    },
    index=town,
)

# Calculating the distance between each city and all others
vectors = data[['x_coordinates_km', 'y_coordinates_km']].values

distances = []
for town_from in range(len(town)):
    row = []
    for town_to in range(len(town)):
        value = distance.euclidean(vectors[town_from], vectors[town_to])
        row.append(value)
    distances.append(row)

# Calculating the total distance for each city based on the number of deliveries
deliveries_in_week = []
for town_from in range(len(town)):
    total = 0
    for town_to in range(len(town)):
        value = distances[town_from][town_to]*2*data['Deliveries'][town_to]
        total += value
    deliveries_in_week.append(total)

deliveries_in_week_df = pd.DataFrame(
    {'Distance': deliveries_in_week}, index=town
)

# Finding the city with the shortest total distance
print(deliveries_in_week_df)
print()
print('Warehouse City:',
      deliveries_in_week_df['Distance'].idxmin())
