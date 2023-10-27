from ambiente import Ambiente
from mec_aprend import MecAprend
from agente import Agente

if __name__ == '__main__':

    # criar ambiente
    ambiente = Ambiente(2)

    # criar mecanismo de aprendizagem
    mec_aprend = MecAprend()

    # criar agente
    agente = Agente(ambiente, mec_aprend)

    