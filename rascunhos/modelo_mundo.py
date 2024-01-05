'''
 # @ Author: Your name
 # @ Description:
 '''
from typing import List, Dict
from abc import ABC, abstractmethod, abstractproperty
from accao import Accao
from defamb import DEF_AMB

Estado = tuple[int, int]
Posicao = tuple[int, int]
Percepcao = List[List[str]]
Plano = List[Accao]


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




    

