'''Separately calculate average reviews for arriving visitors from the 
wholesale market aggregator and for those who came from the aggregator
of luxury brands. In the diagram with individual visitor reviews, indicate 
the values obtained. Each of the averages obtained will be considered 
the rating of the average visitor for the respective group.'''

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
price = ratings['Price'].values
quality = ratings['Quality'].values

# Classifying visitors into two separate groups based on price and quality thresholds
clients_1 = []
clients_2 = []
for client in list(ratings.values):
    if client[0] < 40 and client[1] > 60:
        clients_1.append(client)
    else:
        clients_2.append(client)

# Calculating the average for each group
average_client_1 = sum(clients_1)/len(clients_1)
average_client_2 = sum(clients_2)/len(clients_2)

# Plotting the mean vectors for each group
plt.figure(figsize=(7, 7))
plt.axis([0, 100, 0, 100])

# Draw the average for group 1 - blue
plt.plot(average_client_1[0],
         average_client_1[1],
         'bo', markersize=15)
# Draw the average for group 2 - green
plt.plot(average_client_2[0],
         average_client_2[1],
         'go', markersize=15)
plt.plot(price, quality, 'ro')
plt.xlabel('Price')
plt.ylabel('Quality')
plt.grid(True)
plt.title('Distribution of reviews and the average value for each group')
plt.show()
