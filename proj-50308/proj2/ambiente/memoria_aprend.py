from abc import ABC, abstractmethod


class MemoriaAprend(ABC):
    @abstractmethod
    def actualizar(self, s, a, q):
        raise NotImplementedError

    @abstractmethod
    def q(self, s, a) -> float:
        raise NotImplementedError
    
class MemoriaEsparsa(MemoriaAprend):

    def __init__(self, valor_omissao) -> None:
        self.__valor_omissao = valor_omissao
        self.__memoria = {}
        self.__estados = set()
    

    def actualizar(self, s, a, q) -> None:
        self.__memoria[(s, a)] = q
        self.__estados.add(s)


    def q(self, s, a) -> float:
        return self.__memoria.get((s, a), self.__valor_omissao)
    
    def obter_estados(self):
        return self.__estados
    
