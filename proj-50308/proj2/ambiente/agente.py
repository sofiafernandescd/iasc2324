from .accao import Accao
from .elemento import Elemento
from .ambiente import Ambiente
from .mec_aprend import MecAprend

class Agente:
    """
    Agente que interage com o ambiente 2D
    """

    def __init__(self, ambiente, mec_aprend):
        """
        Construtor
        :param ambiente: ambiente 2D
        """
        # inicializar ambiente escolhido
        self._ambiente = ambiente
        # posição inicial do agente
        self._posicao = self._ambiente.reiniciar()
        # mecanismo de aprendizagem
        self._mec_aprend = mec_aprend
        # mostrar ambiente
        # self._ambiente.mostrar()

    def executar(self):
        """
        Executar um número de iterações
        :param num_iteracoes: número de iterações
        """
        pass

    def _gerar_reforco(self):
        """
        Gerar reforço
        :return: reforço
        """
        # obter elemento na posição do agente
        elemento = self._ambiente.observar(self._posicao)
        # verificar se o elemento é um alvo
        if elemento == Elemento.ALVO:
            return 1
        # verificar se o elemento é um obstáculo
        elif elemento == Elemento.OBSTACULO:
            return -1
        # caso contrário
        else:
            return 0
    
    

if __name__ == '__main__':

    # criar ambiente
    ambiente = Ambiente(2)

    # criar mecanismo de aprendizagem
    mec_aprend = MecAprend()

    # criar agente
    agente = Agente(ambiente, mec_aprend)

    