import numpy as np
from abc import ABC, abstractmethod

class FuncaoActivacao(ABC):
    @abstractmethod
    def aplicar(self, x):
        pass


class FuncaoActivacaoDegrau(FuncaoActivacao):
    def aplicar(self, x):
        return np.heaviside(x, 0)

class FuncaoActivacaoSigmoid(FuncaoActivacao):
    def aplicar(self, x):
        return 1 / (1 + np.exp(-x))