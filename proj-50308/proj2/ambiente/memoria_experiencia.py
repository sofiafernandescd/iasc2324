import random

class MemoriaExperiencia():
    """
    Classe que representa a memória de experiência, para realizar amostragem.
    """

    def __init__(self, dim_max) -> None:
        self.__dim_max = dim_max
        self.__memoria = []
    

    def actualizar(self, e: tuple) -> None:
        """
        Adiciona uma nova experiência à memória.
        Lida com a limitação da lista para não ultrapassar a dimensão máxima.

        Args:
            e (tuple): Tuplo com a experiência (s, a, r, sn)
        """
        # Lógica para adicionar a experiência à memória, considerando a limitação da dimensão máxima
        self.__memoria.append(e)
        if len(self.__memoria) > self.__dim_max:
            del self.__memoria[0]


    def amostrar(self, n: int) -> float:
        """
        Amostra uma experiência com base nos estados (s) e ações (a) fornecidos.
        Retorna um valor relevante da experiência ou o valor padrão especificado na ausência da experiência.

        Args:
            n (int): Número de amostras a obter da memória
        """
        n_amostras = min(n, len(self.__memoria))
        # Lógica para amostrar uma experiência com base nos estados (s) e ações (a) fornecidos
        return random.sample(self.__memoria, n_amostras)
    