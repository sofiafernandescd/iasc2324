from camada import Camada
import numpy as np

class RedeNeuronal:
    def __init__(self):
        #self.__camadas = [Camada(funcao_ativacao, dim_entrada, dim_saida)]
        self.__camadas = []

    def actualizar(self, pesos, pendores):

        if len(self.__camadas)==1:
            for i, camada in enumerate(self.__camadas):
                camada.actualizar(pesos, pendores)

        else:
            for i, camada in enumerate(self.__camadas):
                camada.actualizar(pesos[i], pendores[i])
                

    def activar(self, entradas):
        saidas = entradas
        for camada in self.__camadas:
            saidas = camada.activar(saidas)
        return saidas

    def juntar(self, camada):
        self.__camadas.append(camada)