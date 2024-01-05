'''
 # @ Author: Sofia Condesso - 50308
 # @ Description:
 '''

from typing import Dict, List
from accao import Accao
from typing import List, Dict
from abc import ABC, abstractmethod, abstractproperty
from accao import Accao

Estado = tuple[int, int]
Posicao = tuple[int, int]
Percepcao = List[List[str]]
Plano = List[Accao]

'''
Modelo do mundo.
 '''

class ModeloMundo(ABC):
    """Modelo do mundo.
    """

    @property 
    @abstractmethod
    def S(self) -> List[Estado]:
        """Obter estados possíveis.
        :return: lista de estados
        """
        pass


    @property 
    @abstractmethod
    def A(self) -> List[Accao]:
        """Obter acções possíveis.
        :return: lista de acções
        """
        pass


    def T(self, s: Estado, a: Accao) -> float:
        """Obter probabilidade de transição.
        :param s: estado
        :param a: acção
        :return: probabilidade de transição
        """
        pass

    def distancia(self, s: Estado, sn: Estado) -> float:
        """Obter distância entre dois estados.
        :param s: estado
        :param sn: estado seguinte
        :return: distância
        """
        pass


class ModeloMundo2D(ModeloMundo):

    ALVO = '+'
    OBSTACULO = '#'

    def __init__(self):
        """Inicializa o modelo do mundo 2D.
        """
        self._x_max = 0
        self._y_max = 0

        
    @property
    def S(self) -> List[Estado]:
        """Obter estados possíveis.
        :return: lista de estados
        """
        return [(x, y) for y in range(self._y_max) for x in range(self._x_max)]
    
    @property
    def A(self) -> List[Accao]:
        """Obter acções possíveis.
        :return: lista de acções
        """
        return [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def T(self, s: Estado, a: Accao) -> float:
        """Obter probabilidade de transição.
        :param s: estado
        :param a: acção
        :return: probabilidade de transição
        """
    
        return self.__simular_accao(s, a)
        

    def distancia(self, s: Estado, sn: Estado) -> float:
        """Obter distância entre dois estados.
        :param s: estado
        :param sn: estado seguinte
        :return: distância
        """
        return abs(s[0] - sn[0]) + abs(s[1] - sn[1])
      

    def actualizar(self, percepcao: Percepcao) -> None:
        """Actualizar modelo do mundo.
        :param percepcao: percepção
        """
        # ir buscar o x_max e y_max
        self._x_max = len(percepcao[0])
        self._y_max = len(percepcao)
        # ir buscar os elementos percepcionados
        self.__elementos = percepcao
        # ir buscar os estados possíveis dentro do ambiente que não são obstáculos
        self.__estados = [(x, y) 
                          for y in range(self._y_max) 
                          for x in range(self._x_max)
                          if percepcao[y][x] != self.OBSTACULO]
        
        self._x_max = len(percepcao[0])
        self._y_max = len(percepcao)

    def obter_posicoes_alvo(self) -> List[Posicao]:
        """Obter posições alvo. Modelo do mundo disponibiliza posições alvo.
        :return: lista de posições alvo
        """
        return [(x, y) for (x, y) in self.__estados
                if self.__elementos[y][x] == self.ALVO]
        

    def __simular_accao(self, estado: Estado, accao: Accao) -> Estado:
        """Simular acção.
        :param s: estado
        :param a: acção
        :return: estado seguinte
        """
        (x, y) = estado
        (dx, dy) = accao
        estado_suc = (x + dx, y + dy)
        if self.__estado_valido(estado_suc):
            return estado_suc
        else:
            return None


    def __estado_valido(self, estado: Estado) -> bool:
        """Verificar se estado é válido.
        :param s: estado
        :return: True se estado é válido, False caso contrário
        """
        (x, y) = estado
        return 0 <= x < self._x_max and 0 <= y < self._y_max and self.__elementos[y][x] != self.OBSTACULO



class FrenteOnda():
    
    def __init__(self, gama: float, valor_max: float) -> None:
        """Inicializa o algoritmo Frente-de-Onda.
        :param gama: factor de desconto
        :param valor_max: valor máximo
        """
        self.gama = gama
        self.valor_max = valor_max
        self.V = {} # # Dicionário para armazenar valores associados a estados
        self.frente_onda = []

    def propagar_valor(self, modelo, objectivos) -> Dict[Estado, float]:
        """Propagação de valor através do algoritmo Frente de Onda.
        :param modelo: modelo
        :param objectivos: objectivos
        """
        for s in objectivos:
            self.V[s] = self.valor_max  # valor máximo para objectivos
            self.frente_onda.append(s)

        while self.frente_onda:
            s = self.frente_onda.pop(0)
            for sn in self.__adjacentes(modelo, s):
                # self.V[s] += self.gama * modelo.T(s, sn) * self.V[sn]
                #v = self.V[sn]*pow(self.gama, modelo.distancia(s, sn))
                # v = self.V.get(sn, '-inf') * pow(self.gama, modelo.distancia(s, sn))
                v = self.V[s] * pow(self.gama, modelo.distancia(s, sn))
                if v > self.V.get(sn, float('-inf')):
                    self.V[sn] = v
                    self.frente_onda.append(sn)
        
        return self.V


    def __adjacentes(self, modelo, estado) -> List[Estado]:
        """Obter estados adjacentes.
        :param modelo: modelo
        :param estado: estado
        :return: estados adjacentes
        """
        estados_adjacentes = []
        for accao in modelo.A:
            estado_suc = modelo.T(estado, accao)
            if estado_suc:
                estados_adjacentes.append(estado_suc)
        return estados_adjacentes
        


class PlanFrenteOnda():

    def __init__(self, modelo: ModeloMundo2D, gama: float = 0.98, valor_max: float = 1) -> None:
        """Inicializa o planeador.
        :param modelo: modelo do mundo
        """
        self.__modelo = modelo
        self.__frente_onda = FrenteOnda(gama, valor_max)


    @property
    def V(self) -> Dict[Estado, float]:
        """Função de valor.
        :return: valores
        """
        return self.__frente_onda.V

    def planear(self, objectivos: List[Estado]) -> Dict[Estado, Accao]:
        """Planear.
        :param objectivos: objectivos
        :return: plano
        """
        self.__V = self.__frente_onda.propagar_valor(self.__modelo, objectivos)
        politica = {
            estado: max(self.__modelo.A, key=lambda accao: self.__valor_accao(estado, accao)) 
            for estado in self.__modelo.S 
            if estado not in objectivos
        }
        return politica

    def __valor_accao(self, estado: Estado, accao: Accao) -> float:
        """Obter valor de uma acção.
        :param estado: estado
        :param accao: acção
        :return: valor
        """
        novo_estado = self.__modelo.T(estado, accao)
        return self.V.get(novo_estado, float('-inf'))
        
