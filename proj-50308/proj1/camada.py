import numpy as np

class Camada:
    def __init__(self, funcao_ativacao, dim_entrada, dim_saida):
        self.__func_ativacao = funcao_ativacao
        self.__pesos = np.random.randn(dim_entrada, dim_saida)
        self.__pendores = np.random.randn(dim_saida)

    def actualizar(self, pesos, pendores):
        self.__pesos = pesos
        self.__pendores = pendores

    def activar(self, entradas):
        # Ensure entradas is a 2D array (column vector)
        # entradas = np.array(entradas).reshape((-1, 1))
        
        y = np.dot(entradas, self.__pesos) + self.__pendores
        return self.__func_ativacao.aplicar(y)
