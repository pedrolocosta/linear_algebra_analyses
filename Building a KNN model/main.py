import numpy as np
import pandas as pd
from scipy.spatial import distance


def nearest_neighbor_predict(train_features, train_target, new_features):
 # faça uma lista com distâncias até todas as observações do conjunto de treinamento
    distances = []
    for i in range(train_features.shape[0]):
        calc = distance.euclidean(new_features, train_features.iloc[i])
        distances.append(calc)

    # encontre o índice da observação com a distância mais curta
    best_index = np.argmin(distances)

    # encontre o valor objetivo para esta observação
    answer = train_target[best_index]
    return answer
