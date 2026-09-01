# Construa todos os vetores bidimensionais com as avaliações dos visitantes da LuxForVIP usando pontos no plano.

# Importing the necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Adding the data
ratings_values = [
    [68, 18], [81, 19], [81, 22], [15, 75], [75, 15], [17, 72],
    [24, 75], [21, 91], [76, 6], [12, 74], [18, 83], [20, 62],
    [21, 82], [21, 79], [84, 15], [73, 16], [88, 25], [78, 23],
    [32, 81], [77, 35]]
ratings = pd.DataFrame(ratings_values, columns=['Price', 'Quality'])

# Creating the vectors
price = ratings['Price'].values
quality = ratings['Quality'].values

# Assembling the Cartesian plane with vectors
plt.figure(figsize=(3.5, 3.5))
plt.axis([0, 100, 0, 100])
plt.plot(price, quality, 'ro')
plt.xlabel('Price')
plt.ylabel('Quality')
plt.grid(True)
plt.show()
