'''Crie duas listas separadas de vetores bidimensionais contendo as avaliações 
dos visitantes: para aqueles que vieram do agregador do mercado atacadista e para 
aqueles que chegaram do agregador de luxo. Nomeie as variáveis visitors_1 e 
visitors_2. Para fazer isso, você vai precisar especificar os limiares de preço 
e qualidade que dividem os visitantes de ambos os agregadores. Depois, precisa 
aplicar esses limiares para separá-los nas variáveis mencionadas anteriormente.
Imprima seus valores na tela.'''

# Importing the necessary modules
import numpy as np
import pandas as pd

# Adding the data
ratings_values = [
    [68, 18], [81, 19], [81, 22], [15, 75], [75, 15], [17, 72],
    [24, 75], [21, 91], [76, 6], [12, 74], [18, 83], [20, 62],
    [21, 82], [21, 79], [84, 15], [73, 16], [88, 25], [78, 23],
    [32, 81], [77, 35]]
ratings = pd.DataFrame(ratings_values, columns=['Price', 'Quality'])

# Sorting visitors into two separate lists based on price and quality thresholds
visitors_1 = []
visitors_2 = []
for visitor in list(ratings.values):
    if (visitor[0] < 40) and (visitor[1] > 60):
        visitors_1.append(visitor)
    else:
        visitors_2.append(visitor)

print('First Aggregator Visitor Reviews:', visitors_1)
print('Reviews from visitors to the second aggregator:', visitors_2)
