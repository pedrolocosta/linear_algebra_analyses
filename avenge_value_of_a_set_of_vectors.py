'''	Find the average quality rating, combine the average ratings
of quality and price for all visitors in one vector, and in the plan 
Cartesian, indicate the value obtained. The resulting vector will be 
considered the average visitor rating.'''

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

# Average price value
price = ratings['Price'].values
sum_prices = sum(price)
average_price_rat = sum(price) / len(price)

# Average quality value
quality = ratings['Quality'].values
average_quality_rat = sum(quality) / len(quality)

# Constructing the mean vector
average_rat = np.array([average_price_rat, average_quality_rat])

# Plotting the mean vector
plt.figure(figsize=(7, 7))
plt.axis([0, 100, 0, 100])
plt.plot(0,
         0,
         average_rat[0],
         average_rat[1],
         'mo', markersize=15)
plt.plot(price, quality, 'ro')
plt.xlabel('Price')
plt.ylabel('Quality')
plt.grid(True)
plt.title('Distribution of evaluations and the average value for the entire sample')
plt.show()
