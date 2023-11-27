from ambiente import Ambiente
from agente import AgenteAprendRef
from mec_aprend_ref import MecAprendRef
from accao import Accao
import matplotlib.pyplot as plt

class TesteAprendRef:
    def testar(self, num_ambiente, num_episod, memoria_experiencia=False, valor_omissao=0.0, epsilon=0.1):
        """Testar aprendizagem por reforço.
        :param num_ambiente: número de ambiente
        :param num_episod: número de episódios
        """
        # criar ambiente
        ambiente = Ambiente(num_ambiente)
        # acções ao ambiente
        accoes = list(Accao)
        # criar mecanismo de aprendizagem por reforço
        mec_aprend = MecAprendRef(accoes, memoria_experiencia, valor_omissao, epsilon)
        # criar agente
        agente = AgenteAprendRef(ambiente, mec_aprend)
        # executar episódios de interação do agente com o ambiente
        num_passos_episodio = agente.executar(num_episod)

        # imprimir número de passos por episódio
        print(num_passos_episodio)
        # imprimir memória de aprendizagem
        #print(agente.__mec_aprend.__mem_aprend.__memoria)

        return num_passos_episodio
    
# Executar teste
if __name__ == "__main__":

    NUM_AMBIENTE = 2
    MAX_EPISOD = 100

    teste = TesteAprendRef()
    num_passos_episodio_qlearning = teste.testar(NUM_AMBIENTE, MAX_EPISOD)
    num_passos_episodio_qme = teste.testar(NUM_AMBIENTE, MAX_EPISOD, memoria_experiencia=True)
    num_passos_episodio_qvo = teste.testar(NUM_AMBIENTE, MAX_EPISOD, valor_omissao=100.0, epsilon=0.0)

    
    # subplot dos 3 graficos
    plt.subplot(3, 1, 1)
    # desempenho Q-Learning
    plt.plot(num_passos_episodio_qlearning, label="Q-Learning")
    plt.title(f"Desempenho do agente no ambiente {NUM_AMBIENTE}")
    plt.xlabel("Episódio")
    plt.ylabel("Número de passos")
    plt.legend()
    # desempenho QME
    plt.subplot(3, 1, 2)
    plt.plot(num_passos_episodio_qme, label="QME")
    plt.xlabel("Episódio")
    plt.ylabel("Número de passos")
    plt.legend()
    # desempenho Q-Learning valores iniciais optimistas
    plt.subplot(3, 1, 3)
    plt.plot(num_passos_episodio_qvo, label="Q-Learning valores iniciais optimistas")
    plt.xlabel("Episódio")
    plt.ylabel("Número de passos")
    plt.legend()
    plt.show()

