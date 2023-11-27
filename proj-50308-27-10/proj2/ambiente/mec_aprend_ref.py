from accao import Accao
from aprend_ref import AprendRef
from sel_accao import SelAccao
from memoria_aprend import MemoriaAprend
from typing import List


class MecAprendRef():
    """Mecanismo de aprendizagem por reforço.
    O mecanismo de aprendizagem por reforço é composto por:
    - memória de aprendizagem (MemoriaAprend)
    - seleção de ação (SelAccao)
    - aprendizagem por reforço (AprendRef)
    """

    def __init__(self, accoes: List[Accao]) -> None:
        self.accoes = accoes
        self._mem_aprend = MemoriaAprend()
        self.__sel_accao = SelAccao(self._mem_aprend)
        self._aprend_ref = AprendRef(
            self._mem_aprend, 
            self.__sel_accao, 
            alfa = 0.1, # factor de aprendizagem
            beta = 0.9 # factor de desconto
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
        return self._aprend_ref.aprender(s, a, r, sn, an)

    