from ambiente import Ambiente
from agente import AgenteAprendRef
from mec_aprend_ref import MecAprendRef
from accao import Accao

class TesteAprendRef:
    def testar(self, num_ambiente, num_episod):
        """Testar aprendizagem por reforço.
        :param num_ambiente: número de ambiente
        :param num_episod: número de episódios
        """
        # criar ambiente
        ambiente = Ambiente(num_ambiente)
        # acções ao ambiente
        accoes = list(Accao)
        # criar mecanismo de aprendizagem por reforço
        mec_aprend = MecAprendRef(accoes)
        # criar agente
        agente = AgenteAprendRef(ambiente, mec_aprend)
        # executar episódios de interação do agente com o ambiente
        num_passos_episodio = agente.executar(num_episod)

        # imprimir número de passos por episódio
        print(num_passos_episodio)
        # imprimir memória de aprendizagem
        print(agente.mec_aprend.mem_aprend)

        return num_passos_episodio
    
# Executar teste
if __name__ == "__main__":

    NUM_AMBIENTE = 2
    MAX_EPISOD = 100

    teste = TesteAprendRef()
    num_passos_episodio = teste.testar(NUM_AMBIENTE, MAX_EPISOD)

    # Mostrar desempenho do agente
    import matplotlib.pyplot as plt
    plt.plot(num_passos_episodio, label="Q-Learning")
    plt.title(f"Desempenho do agente no ambiente {NUM_AMBIENTE}")
    plt.xlabel("Episódio")
    plt.ylabel("Número de passos")
    plt.legend()
    plt.show()


