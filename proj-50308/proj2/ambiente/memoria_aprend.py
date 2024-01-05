from abc import ABC, abstractmethod


class MemoriaAprend(ABC):
    @abstractmethod
    def actualizar(self, s, a, q):
        raise NotImplementedError

    @abstractmethod
    def q(self, s, a) -> float:
        raise NotImplementedError
    
class MemoriaEsparsa(MemoriaAprend):
    """ Memória de aprendizagem esparsa.
    A memória de aprendizagem esparsa é um dicionário que associa um par (s, a) a um valor Q(s, a).
    """

    def __init__(self, valor_omissao) -> None:
        """Inicializa a memória de aprendizagem esparsa.
        :param valor_omissao: valor a considerar para o Q-Learning valores iniciais optimistas
        """
        self.__valor_omissao = valor_omissao
        self.__memoria = {}
        self.__estados = set()
    

    def actualizar(self, s, a, q) -> None:
        """Atualizar valor Q(s, a).
        :param s: estado
        :param a: acção
        :param q: valor Q(s, a)
        """
        self.__memoria[(s, a)] = q
        self.__estados.add(s)


    def q(self, s, a) -> float:
        """Obter valor Q(s, a).
        :param s: estado
        :param a: acção
        :return: valor Q(s, a)
        """
        return self.__memoria.get((s, a), self.__valor_omissao)
    
    def obter_estados(self):
        """Obter estados
        :return: estados
        """
        return self.__estados
    
