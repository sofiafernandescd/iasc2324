from .accao import Accao
from .elemento import Elemento
from .ambiente import Ambiente
from .mec_aprend_ref import MecAprendRef

class Agente:
    """
    Agente que interage com o ambiente 2D
    """

    def __init__(self, ambiente, mec_aprend):
        """
        :param ambiente: ambiente 2D
        :param mec_aprend: mecanismo de aprendizagem
        """
        # inicializar ambiente escolhido
        self._ambiente = ambiente
        # posição inicial do agente
        self.posicao = self._ambiente.reiniciar()
        # acao inicial do agente
        self.accao = None
        # mecanismo de aprendizagem
        self._mec_aprend = mec_aprend
        # mostrar ambiente
        self._ambiente.mostrar()

    def executar(self, accao):
        """
        Actuar no ambiente
        :param accao: acção
        """
        # executar acção
        self._ambiente.actuar(self._posicao, accao)
        # actualizar posição
        self._posicao = self._ambiente.observar(self._posicao)
        # mostrar ambiente
        self._ambiente.mostrar()

  

    def _gerar_reforco(self):
        """
        Gerar reforço
        :return: reforço
        """
        # obter elemento na posição do agente
        elemento = self.observar()
        # verificar se o elemento é um alvo
        if elemento == Elemento.ALVO:
            return 1
        # verificar se o elemento é um obstáculo
        elif elemento == Elemento.OBSTACULO:
            return -1
        # caso contrário
        else:
            return 0
    
    

