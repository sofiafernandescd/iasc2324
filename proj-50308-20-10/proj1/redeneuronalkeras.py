## From project 1.3

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import numpy as np
import matplotlib.pyplot as plt



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
        #plt.plot(historico.history['loss'])
        #plt.title(f'Função de perda (lr={learning_rate}, momentum={momentum}))')
        #plt.ylabel('Perda')
        #plt.xlabel('Época')
        #plt.savefig(f"graficos-1.3/lr-{learning_rate}-momentum-{momentum}.png")

    
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