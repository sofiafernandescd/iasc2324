from abc import ABC, abstractmethod
from accao import Accao
from random import choice, random, shuffle

class SelAccao(ABC):
    """Classe abstrata para a seleção de ação"""
    def __init__(self, mem_aprend) -> None:
        self._mem_aprend = mem_aprend
    
    @abstractmethod
    def seleccionar_accao(self, s) -> Accao:
        raise NotImplementedError
    


class EGreedy(SelAccao):
    """
    Seleção de ação e-greedy, onde o Agent escolhe uma ação aleatória com 
    probabilidade epsilon e uma ação sôfrega com probabilidade 1-epsilon.
    """
    def __init__(self, mem_aprend, accoes, epsilon) -> None:
        # inicializar memória de aprendizagem
        super().__init__(mem_aprend)
        # inicializar lista de ações
        self.__accoes = accoes
        # inicializar probabilidade até à qual o agente faz exploração
        self._epsilon = epsilon
        

    def seleccionar_accao(self, s) -> Accao:
        """Selecionar entre ação exploratória ou ação sôfrega"""

        # escolher ação aleatória com probabilidade epsilon
        if random() < self._epsilon:
            accao = self.explorar(s)

        # escolher ação sôfrega com probabilidade 1-epsilon
        else:
            accao = self.aproveitar(s)

        return accao
        
    def aproveitar(self, s) -> Accao:
        """Selecionar ação com maior valor Q, a ação sôfrega.
        Apenas para encapsular a chamada ao método accao_sofrega().
        """

        return self.accao_sofrega(s)
    
    def explorar(self) -> Accao:
        """Selecionar uma ação aleatória"""

        return choice(self.__accoes)
    
    def accao_sofrega(self, s) -> Accao:
        """Selecionar ação com maior valor Q, a ação sôfrega"""

        # misturar ações para evitar sempre a mesma ação em caso de empate
        shuffle(self.__accoes) # inplace

        # selecionar ação com maior valor Q, i.e., ação sôfrega 
        return max(self.__accoes, key=lambda a: self._mem_aprend.q(s, a))