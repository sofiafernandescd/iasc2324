'''
 # @ Author: Sofia Condesso
 # @ Description:
    O objetivo deste script é implementar uma rede neuronal multicamada,
    utilizando a plataforma Keras.
    Implementação e estudo do operador XOR, considerando os seguintes
aspectos:
• Efeito da taxa de aprendizagem
• Efeito da introdução de um termo de momento
• Efeito da apresentação das amostras de treino com ordem fixa ou aleatória
 '''


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())


class RedeNeuronal:
    def __init__(self):

        # Modelo sequencial vazio
        self.__modelo = Sequential()
           
    def juntar(
        self, camada: Dense
        ) -> None:
        """Adicionar camada ao modelo.

        Args:
            camada (Dense): Camada a adicionar.
        """

        # Adicionar camada ao modelo
        self.__modelo.add(camada)

    def treinar(
        self, X: np.array, y: np.array, epocas: int = 1000, 
        batch_size: int = 1, shuffle: bool = False, 
        learning_rate: float =0.01, momentum: float = 0.0
        ) -> None:
        """Treinar o modelo com os dados de treino.

        Args:
            X (np.array): Dados de treino.
            y (np.array): Rótulos dos dados de treino.
            epocas (int, optional): Número de épocas que o modelo treina, i.e. 
                número de vezes que o modelo passa pelos dados. Uma época é constituída por
                vários passos (steps). Defaults to 1000.
            batch_size (int, optional): Número de entradas lidas em cada passo. Defaults to 1.
            shuffle (bool, optional): Para os dados serem passados à rede de forma aleatória
                ou não. Defaults to False.
            learning_rate (float, optional): Taxa de aprendizagem. Defaults to 0.01.
            momentum (float, optional): Termo de momento. Defaults to 0.0.
        """

        # Otimizador: Descida de Gradiente Estocástica (SGD)
        sgd = SGD(learning_rate=learning_rate, momentum=momentum)

        # Compilar o modelo com o otimizador e a função de perda
        self.__modelo.compile(optimizer=sgd, loss='mean_squared_error', metrics=['accuracy'])
        
        # Treinar o modelo (verbose=1 para mostrar apenas uma barras de progresso)
        historico = self.__modelo.fit(X, y, epochs=epocas, batch_size=batch_size, shuffle=shuffle, verbose=0)

        # Mostrar gráfico da função de perda
        plt.plot(historico.history['loss'])
        plt.title(f'Função de perda (lr={learning_rate}, momentum={momentum}))')
        plt.ylabel('Perda')
        plt.xlabel('Época')
        plt.savefig(f"graficos-1.3/lr-{learning_rate}-momentum-{momentum}.png")

    
    def prever(
        self, X: np.array
        ) -> np.array:
        """Permite fazer previsões com o modelo treinado.
            Devolve as probabilidades, que podem depois ser arredondadas 
            para binário e ser interpretadas como as etiquetas que respondem ao problema.

        Args:
            X (np.array): Dados para fazer previsão.

        Returns:
            np.array: Probabilidades previstas pelo modelo, quando arredondadas, representam
                as etiquetas que respondem ao problema.
        """
        return self.__modelo.predict(X)


def testar_rede_xor(
    X: np.array,
    y: np.array,
    learning_rate: float,
    momentum: float
    ) -> None:
    """Função que testa a rede neuronal com os dados para o problema XOR.
        Teste com os dados com ordem fixa (pela qual foram treinados) e 
        com ordem aleatória (para testar a generalização).

    Args:
        X (np.array): Dados de treino (e usados para teste).
        y (np.array): Etiquetas dos dados de treino (não usados para teste).
        learning_rate (float): Taxa de aprendizagem.
        momentum (float): Termo de momento.
    """
     
    # Criar instâncias da rede neuronal com diferentes taxas de aprendizagem e momentum
    rede_neuronal = RedeNeuronal()

    # Juntar camadas
    # Dimensão do input: 2
    # Dimensão da camada escondida: 2
    # Dimensão do output: 1
    # Camada escondida com ativação tanh porque podemos ter valores positivos e negativos
    rede_neuronal.juntar(Dense(units=2, input_dim=2, activation='tanh'))
    # Camada de saída com ativação sigmoid porque queremos valores entre 0 e 1
    rede_neuronal.juntar(Dense(units=1, activation='sigmoid'))

    # Treinar a redes neuronal (shuffle False para manter a ordem dos inputs)
    rede_neuronal.treinar(
        X, y, epocas=2000, batch_size=1, shuffle=False,
        learning_rate=learning_rate, momentum=momentum
        )

    print("Inputs (ordem fixa):")
    print(X)
    # Obter as previsões da rede neuronal
    previsoes_probs = rede_neuronal.prever(X)
    print("Previsões (probabilidades):")
    print(previsoes_probs)

    # Converter probabilidades para binário
    previsoes_binario = np.round(previsoes_probs)
    print("Previsões (binário):")
    print(previsoes_binario)
    print()

    print("Inputs (ordem aleatória):")
    Xs = X.copy()
    np.random.shuffle(Xs) # Inputs aleatórios
    print(Xs)
    # Obter as previsões da rede neuronal
    previsoes_probs = rede_neuronal.prever(Xs)
    print("Previsões (probabilidades):")
    print(previsoes_probs)

    # Converter probabilidades para binário
    previsoes_binario = np.round(previsoes_probs)
    print("Previsões (binário):")
    print(previsoes_binario)

# Dados de treino para o operador XOR
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([[0], [1], [1], [0]])

### TESTES ###
# Todos os testes são realizados com treino de 2000 épocas e batch_size=1
# São mostrados os inputs, as previsões em probabilidade e em binário
# Os inputs são testados em ordem fixa e aleatória
print("----------- Learning rate = 0.1, Momentum = 0.0 -----------")
testar_rede_xor(X_train, y_train, 0.1, 0.0)
print()

print("----------- Learning rate = 0.1, Momentum = 0.5 -----------")
testar_rede_xor(X_train, y_train, 0.1, 0.5)
print()

print("----------- Learning rate = 0.1, Momentum = 0.9 -----------")
testar_rede_xor(X_train, y_train, 0.1, 0.9)
print()

print("----------- Learning rate = 0.5, Momentum = 0.0 -----------")
testar_rede_xor(X_train, y_train, 0.5, 0.0)
print()

print("----------- Learning rate = 0.5, Momentum = 0.5 -----------")
testar_rede_xor(X_train, y_train, 0.5, 0.5)
print()

print("----------- Learning rate = 0.5, Momentum = 0.9 -----------")
testar_rede_xor(X_train, y_train, 0.5, 0.9)
print()

print("----------- Learning rate = 0.9, Momentum = 0.0 -----------")
testar_rede_xor(X_train, y_train, 0.9, 0.0)
print()

print("----------- Learning rate = 0.9, Momentum = 0.5 -----------")
testar_rede_xor(X_train, y_train, 0.9, 0.5)
print()

print("----------- Learning rate = 0.9, Momentum = 0.9 -----------")
testar_rede_xor(X_train, y_train, 0.9, 0.9)
print()






