'''
 # @ Author: Sofia Condesso
 # @ Description:
 '''

from abc import ABC, abstractmethod
from typing import Dict, List
import matplotlib.pyplot as plt

#from modelo_mundo import ModeloMundo2D, Estado, Percepcao, Plano
from frente_onda import PlanFrenteOnda, ModeloMundo2D, Estado, Percepcao, Plano
from accao import Accao
from defamb import DEF_AMB

class AgenteDelib(ABC):
    def __init__(self) -> None:
        pass

    def executar(self) -> None:
        """Implementa o processo de tomada de decisão do agente deliberativo"""

        # 1. Observar o mundo
        percepcao = self._percepcionar()

        # 2. Actualizar crenças
        self._actualizar_crencas(percepcao)

        # 3. Deliberar o que fazer
        # a) Gerar opções
        # b) Selecionar opções
        objectivos = self._deliberar()

        # 4. Planear como fazer, gerando um plano de acção
        plano = self._planear(objectivos)

        # 5. Executar plano de acção
        self._executar_plano(plano)


    @abstractmethod
    def _percepcionar(self) -> Percepcao:
        """Método abstrato para a fase de observação"""
        pass



    @abstractmethod
    def _actualizar_crencas(self, percepcao: Percepcao) -> None:
        """Método abstrato para a fase de atualização de crenças"""
        pass

    @abstractmethod
    def _deliberar(self) -> List[Estado]:
        """Método abstrato para a fase de deliberação"""
        pass

    @abstractmethod
    def _planear(self, objectivos: List[Estado]) -> Plano:
        """Método abstrato para a fase de planeamento"""
        pass

    @abstractmethod
    def _executar_plano(plano: Plano) ->  None:
        """Método abstrato para a fase de execução do plano de ação"""
        pass
        

class AgenteFrenteOnda(AgenteDelib):
    def __init__(self, num_ambiente: int) -> None:
        super().__init__()
        self.num_ambiente = num_ambiente
        self.__modelo_mundo = ModeloMundo2D()
        self.__planeador = PlanFrenteOnda(self.__modelo_mundo)
        self.__visualizador = VisValorPol()

    
    def _percepcionar(self) -> Percepcao:

        #return self.__modelo_mundo.percepcionar(self.num_ambiente)
        return DEF_AMB[self.num_ambiente]
        

    def _actualizar_crencas(self, percepcao: Percepcao) -> None:

        self.__modelo_mundo.actualizar(percepcao)
        

    def _deliberar(self) -> List[Estado]:
        """Método para a fase de deliberação. Retorna uma lista de estados que representam objetivos."""
        objetivos = []
        for y, linha in enumerate(self._percepcionar()):
            for x, elemento in enumerate(linha):
                if elemento == ModeloMundo2D.ALVO:
                    objetivos.append((x, y))
        return objetivos
    

    def _planear(self, objectivos: List[Estado]) -> Plano:
        """Com base nos objectivos, planear um plano de acção utilizando um planeador de frente de onda"""
        return self.__planeador.planear(objectivos)
        

    def _executar_plano(self, plano: Plano) ->  None:

        # chamar o visualizador
        self.__visualizador.mostrar(self.__modelo_mundo._x_max, self.__modelo_mundo._y_max, self.__planeador.V, plano)
        # self.__visualizador.mostrar(self.__modelo_mundo.x_max, self.__modelo_mundo.y_max, self.__planeador.V(), plano)
        

class VisValorPol():

    def __init__(self) -> None:
        pass

    def mostrar(sel, x_max: int, y_max: int, V: Dict[Estado, float], politica: Dict[Estado, Accao]) -> None:
        
        fig, grafico = plt.subplots()
        #fig.title('Valor e Política')
        

        # Valores de X, Y e Z (eixo do valor) para gerar o gradiente de cor
        X = range(x_max)
        Y = range(y_max)
        Z = [[V.get((x, y), 0) for x in X] for y in Y]

        # Nos sitios onde não há accao, definir uma acção de omissão
        ACCAO_OMISSAO = (0, 0)

        # Obter politica (acção = (dx, dy)) para cada estado
        DX = [[politica.get((x, y), ACCAO_OMISSAO)[0] for x in X] for y in Y]
        DY = [[-politica.get((x, y), ACCAO_OMISSAO)[1] for x in X] for y in Y] # porque o eixo dos yy é invertido

        grafico.imshow(Z) #, cmap='viridis', interpolation='nearest', origin='lower')
        grafico.quiver(X, Y, DX, DY, scale_units='xy', scale=2) #, color='white', pivot='mid', angles='xy')
        plt.show()
        

