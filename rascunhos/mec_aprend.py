from abc import ABC, abstractmethod

class MecAprend:
    """
    Implementação dos mecanismos de memória de aprendizagem e de selecção de acção
    """

    @abstractmethod
    def actualizar(self, s, a, sn, r, an=None):
        raise NotImplementedError




    