from accao import Accao
from elemento import Elemento
from ambiente import Ambiente
from mec_aprend import MecAprend

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
        self._ambiente.mostrar()

    def executar(self):
        """
        Executar um número de iterações
        :param num_iteracoes: número de iterações
        """
        # obter percepção do ambiente
        percepcao = self.observar()
        # escolher acção
        accao = self._mec_aprend.escolher_accao(percepcao)
        # executar acção
        self.actuar(accao)
        # actualizar mecanismo de aprendizagem
        self._mec_aprend.actualizar(percepcao, accao)

    def actuar(self, accao):
        """
        Executa uma acção no ambiente
        :param accao: acção a ser executada
        """
        # executar acção no ambiente
        self._ambiente.actuar(accao)
        # actualizar posição do agente
        self._posicao = self._ambiente._posicao_agente
        # mostrar ambiente
        self._ambiente.mostrar()

    def observar(self):
        """
        Observar o ambiente
        :return: percepção do agente
        """
        # obter a posição do agente
        #posicao = self._ambiente.percepcao(self._posicao)
        # obter o elemento na posição do agente
        #elemento = Elemento(self._ambiente[posicao[0]][posicao[1]])
        return self._ambiente.observar(self._posicao)

    def obter_posicao(self):
        """
        Obter posição do agente
        :return: posição do agente
        """
        return self._posicao
    
    

if __name__ == '__main__':

    # criar ambiente
    ambiente = Ambiente(2)

    # criar mecanismo de aprendizagem
    mec_aprend = MecAprend()

    # criar agente
    agente = Agente(ambiente, mec_aprend)

    # executar acções
    agente.actuar(Accao.NORTE)

    agente.actuar(Accao.ESTE)

    agente.actuar(Accao.SUL)

    agente.actuar(Accao.OESTE)