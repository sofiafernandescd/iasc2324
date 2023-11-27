from abc import ABC, abstractmethod
from memoria_experiencia import MemoriaExperiencia

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
        self.__sel_accao = sel_accao
        self._alfa = alfa
        self._gama = gama

    @abstractmethod
    def aprender(self, s, a, r, sn, an=None):
        raise NotImplementedError
    

class QLearning(AprendRef):
    def __init__(self, mem_aprend, sel_accao, alfa, gama) -> None:
        super().__init__(mem_aprend, sel_accao, alfa, gama)
        self._mem_aprend = mem_aprend
        self.__sel_accao = sel_accao
        self._alfa = alfa
        self._gama = gama

    def aprender(self, s, a, r, sn, an=None):
        """Aprender por Q-Learning. O algoritmo envolve a seleção de uma ação,
        atualização do valor Q(s, a) e atualização da memória de aprendizagem.
        :param s: estado
        :param a: acção
        :param r: reforço
        :param sn: estado seguinte
        """
        # açao sofrega selecionada para o estado seguinte
        an = self.__sel_accao.accao_sofrega(sn)
        # valor Q(s, a)
        qsa = self._mem_aprend.q(s, a)
        # valor Q(s', a')
        qsan = self._mem_aprend.q(sn, an)
        # diferença temporal
        delta = r + self._gama * qsan - qsa
        #print(r), print(self._gama), print(qsan), print(qsa)
        # atualizar valor Q(s, a)
        q = qsa + self._alfa * delta
        # atualizar memória de aprendizagem
        self._mem_aprend.actualizar(s, a, q)
       
        return q
    

    
class QME(QLearning):
    def __init__(self, mem_aprend, sel_accao, alfa, gama, num_sim=100, dim_max=1000) -> None:
        """Inicializa o agente Q-Learning com Memória de Experiência.

        :param mem_aprend: memória de aprendizagem
        :param sel_accao: estratégia de seleção de ação
        :param alfa: taxa de aprendizado (alfa)
        :param gama: fator de desconto (gama)
        :param num_sim: número de simulações por episódio
        :param dim_max: dimensão máxima da memória de experiência
        """
        super().__init__(mem_aprend, sel_accao, alfa, gama)
        self.__num_sim = num_sim
        self.__memoria_experiencia = MemoriaExperiencia(dim_max)

    def aprender(self, s, a, r, sn, an=None):
        """
        Método de aprendizagem por Q-Learning com Memória de Experiência. O algoritmo envolve a seleção de uma ação,
        atualização do valor Q(s, a) e atualização da memória de aprendizagem (algoritmo Q-Learning). Além disso, o agente aprende a partir
        das experiências armazenadas na memória de experiência.

        :param s: estado atual
        :param a: ação realizada no estado atual
        :param r: reforço obtido após a ação
        :param sn: próximo estado após a ação
        :param an: próxima ação (opcional, pode ser passada como argumento ou será escolhida pela estratégia)
        :return: valor Q atualizado para o estado e ação atuais
        """
        # Ação sofrega selecionada para o estado seguinte
        # an = self.__sel_accao.accao_sofrega(sn)
        # Valor Q(s, a)
        # qsa = self._mem_aprend.q(s, a)
        # Valor Q(s', a')
        # qsan = self._mem_aprend.q(sn, an)
        # Diferença temporal
        # delta = r + self._gama * qsan - qsa
        # Atualizar valor Q(s, a)
        # q = qsa + self._alfa * delta
        # Atualizar memória de aprendizagem
        # self._mem_aprend.actualizar(s, a, q)

        super().aprender(s, a, r, sn, an)

        # Criar experiência
        experiencia = (s, a, r, sn)
        # Atualizar memória de experiência
        self.__memoria_experiencia.actualizar(experiencia)
        # Amostrar experiências da memória de experiência
        experiencias = self.__memoria_experiencia.amostrar(1)

        self.__simular()

    def __simular(self):
        """
        Simula um episódio de aprendizagem.

        Cada episódio consiste em múltiplos passos e o agente aprende a partir da amostragem
        de experiências armazenadas na memória de experiência, utilizando o método de Q-Learning.
        """

        # Amostrar da memória de experiência
        amostras = self.__memoria_experiencia.amostrar(self.__num_sim)

        for (s, a, r, sn) in amostras:
            super().aprender(s, a, r, sn)

            

       
    
