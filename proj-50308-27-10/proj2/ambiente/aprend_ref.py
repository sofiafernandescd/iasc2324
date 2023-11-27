from abc import ABC, abstractmethod

class AprendRef(ABC):
    def __init__(self, mem_aprend, sel_accao, alfa, gama) -> None:
        """Inicializar mecanismo de aprendizagem por reforço.
        :param mem_aprend: memória de aprendizagem
        :param sel_accao: seleção de ação
        :param alfa: factor de aprendizagem
        :param gama: factor de desconto
        """
        self._mem_aprend = mem_aprend
        self.__sel_accao = sel_accao
        self._alfa = alfa
        self._gama = gama

    @abstractmethod
    def aprender(self, s, a, r, sn, an=None):
        raise NotImplementedError
    

