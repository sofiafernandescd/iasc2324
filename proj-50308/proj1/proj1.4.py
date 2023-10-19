'''
 # @ Author: Sofia Condesso - 50308
 # @ Create Time: 2023-10-10 20:31:35
 # @ Description:  Estudo com rede neuronal para classificação de um padrão A ou B 
 # A rede deve ser representada com base numa classe designada RedeNeuronal         
 '''

from redeneuronalkeras import RedeNeuronal # RedeNeuronal feita em 1.3
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import numpy as np
import matplotlib.pyplot as plt


padrao_A = np.array([[1, 1, 1, 1],
                      [1, 0, 0, 1],
                      [1, 0, 0, 1],
                      [1, 1, 1, 1]])

padrao_B = np.array([[1, 0, 0, 1],
                      [0, 1, 1, 0],
                      [0, 1, 1, 0],
                      [1, 0, 0, 1]])

# etiqueta 0 para o padrão A (vetor de zeros)
labels_A = np.zeros(1)  
# etiqueta 1 para o padrão B (vetor de uns)
labels_B = np.ones(1)  

## Combinar tudo no mesmo conjunto de dados
# os padrões são colocados em linhas (2x16)
#data = np.vstack((padrao_A.reshape(-1, 15), padrao_B.flatten()))
data = np.vstack((padrao_A.reshape(-1, 16), padrao_B.reshape(-1, 16)))
labels = np.vstack((labels_A, labels_B))

print("data examples")
print(data)
print("labels examples")
print(labels)

rede_neuronal = RedeNeuronal()

# Juntar camadas
# Dimensão do input: 16
# Dimensão da camada escondida: 8
# Dimensão do output: 1
# Camada de entrada com ativação relu
rede_neuronal.juntar(Dense(units=16, input_dim=16, activation='relu'))
# Camada escondida com ativação relu
rede_neuronal.juntar(Dense(units=8, activation='relu'))
# Camada de saída com ativação sigmoid porque queremos valores entre 0 e 1
rede_neuronal.juntar(Dense(units=1, activation='sigmoid'))

# Treinar a redes neuronal (shuffle False para manter a ordem dos inputs)
rede_neuronal.treinar(
    data, labels, epocas=2000, batch_size=1, shuffle=False,
    learning_rate=0.1, momentum=0.0
    )

# Obter as previsões da rede neuronal
previsoes_probs = rede_neuronal.prever(data)
print("Previsões (probabilidades):")
print(previsoes_probs)

# Converter probabilidades para binário
previsoes_binario = np.round(previsoes_probs)
print("Previsões (binário):")
print(previsoes_binario)

# Previsões com dados em diferente ordem
data_rev = data[-1::-1]
print("Previsões com dados em diferente ordem:")
print(data_rev)
previsoes_probs = rede_neuronal.prever(data_rev)
print("Previsões (probabilidades):")
print(previsoes_probs)
# Converter probabilidades para binário
previsoes_binario = np.round(previsoes_probs)
print("Previsões (binário):")
print(previsoes_binario)


