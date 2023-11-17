from accao import Accao
from aprend_ref import QLearning
from sel_accao import EGreedy
from memoria_aprend import MemoriaEsparsa
from typing import List


class MecAprendRef():
    """Mecanismo de aprendizagem por reforço.
    O mecanismo de aprendizagem por reforço é composto por:
    - memória de aprendizagem (MemoriaEsparsa)
    - seleção de ação (EGreedy)
    - aprendizagem por reforço (QLearning)
    """

    def __init__(self, accoes: List[Accao], alfa=0.5, gama=0.9, epsilon=0.1) -> None:
        self.__accoes = accoes
        self.__mem_aprend = MemoriaEsparsa(valor_omissao="Não existe")
        self._sel_accao = EGreedy(
            self.__mem_aprend, 
            self.__accoes, 
            epsilon=0.1
        )
        self.__aprend_ref = QLearning(
            self.__mem_aprend, 
            self._sel_accao, 
            alfa = 0.1, # factor de aprendizagem
            gama = 0.9 # factor de desconto
        )

    def aprender(self, s, a, r, sn, an=None):
        """
        Aprender por aprendizagem por reforço.
        :param s: estado
        :param a: acção
        :param r: reforço
        :param sn: estado seguinte
        :param an: acção seguinte, default=None
        """
        return self.__aprend_ref.aprender(s, a, r, sn, an)
    


    