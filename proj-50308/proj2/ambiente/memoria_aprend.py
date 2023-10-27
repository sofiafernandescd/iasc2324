from abc import ABC, abstractmethod

class MemoriaAprend(ABC):
    @abstractmethod
    def actualizar(self, s, a, q):
        raise NotImplementedError

    @abstractmethod
    def q(self, s, a) -> float:
        raise NotImplementedError
    
