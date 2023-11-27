from accao import Accao
from aprend_ref import QLearning, QME
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

    def __init__(self, 
                 accoes: List[Accao], 
                 memoria_experiencia: bool = False,
                 valor_omissao: float = 0.0,
                 epsilon: float = 0.1
            ) -> None:
        self.__accoes = accoes
        self.__mem_aprend = MemoriaEsparsa(valor_omissao=valor_omissao)
        self.__sel_accao = EGreedy(
            self.__mem_aprend, 
            self.__accoes, 
            epsilon=epsilon
        )
        if memoria_experiencia:
            self.__aprend_ref = QME(
                self.__mem_aprend, 
                self.__sel_accao, 
                alfa = 0.1, # factor de aprendizagem
                gama = 0.9 # factor de desconto
            )
        else:
            self.__aprend_ref = QLearning(
                self.__mem_aprend, 
                self.__sel_accao, 
                alfa = 0.1, # factor de aprendizagem
                gama = 0.9 # factor de desconto
            )

    def aprender(self, s, a, r, sn, an=None):
        """
        Aprender por aprendizagem por reforço. O algoritmo envolve a seleção de uma ação,
        atualização do valor Q(s, a) e atualização da memória de aprendizagem.
        :param s: estado
        :param a: acção
        :param r: reforço
        :param sn: estado seguinte
        :param an: acção seguinte, default=None
        """
        return self.__aprend_ref.aprender(s, a, r, sn, an)
    
    def seleccionar_accao(self, s):
        """
        Seleccionar acção com base no estado. Pode ser uma acção exploratória
        ou uma acção sôfrega.
        :param s: estado
        :return: acção seleccionada
        """
        return self.__sel_accao.seleccionar_accao(s)
    
    def obter_politica(self):
        """
        Obter política. A política é um dicionário de estados e acções, onde
        para cada estado é selecionada a acção com maior valor Q.
        :return: política
        """
        return {s: self.__sel_accao.aproveitar(s) for s in self.__mem_aprend.obter_estados()}
    


    