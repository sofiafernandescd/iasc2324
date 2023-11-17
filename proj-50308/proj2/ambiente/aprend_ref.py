from abc import ABC, abstractmethod

class AprendRef(ABC):
    def __init__(self, mem_aprend, sel_accao, alfa, gama) -> None:
        """Classe abstrata que serve como uma base para implementações de 
        algoritmos de aprendizagem por reforço.

        :param mem_aprend: memória de aprendizagem
        :param sel_accao: seleção de ação
        :param alfa: factor de aprendizagem
        :param gama: factor de desconto
        """
        self._mem_aprend = mem_aprend
        self._sel_accao = sel_accao
        self._alfa = alfa
        self._gama = gama

    @abstractmethod
    def aprender(self, s, a, r, sn, an=None):
        raise NotImplementedError
    

class QLearning(AprendRef):
    def __init__(self, mem_aprend, sel_accao, alfa, gama) -> None:
        super().__init__(mem_aprend, sel_accao, alfa, gama)

    def aprender(self, s, a, r, sn, an=None):
        """Aprender por Q-Learning. O algoritmo envolve a seleção de uma ação,
        atualização do valor Q(s, a) e atualização da memória de aprendizagem.
        :param s: estado
        :param a: acção
        :param r: reforço
        :param sn: estado seguinte
        """
        # açao sofrega selecionada para o estado seguinte
        an = self._sel_accao.accao_sofrega(sn)
        # valor Q(s, a)
        qsa = self._mem_aprend.q(s, a)
        # valor Q(s', a')
        qsan = self._mem_aprend.q(sn, an)
        # diferença temporal
        delta = r + self._gama * qsan - qsa
        # atualizar valor Q(s, a)
        q = qsa + self._alfa * delta
        # atualizar memória de aprendizagem
        self._mem_aprend.actualizar(s, a, q)
       
        return q
    
