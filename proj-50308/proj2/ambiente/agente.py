from .accao import Accao
from .elemento import Elemento
from .ambiente import Ambiente
from .mec_aprend_ref import MecAprendRef

        
class AgenteAprendRef():
    """
    Agente que interage com o ambiente 2D e possui uma memória de
    aprendizagem e um mecanismo de aprendizagem por reforço.
    """

    def __init__(self, ambiente, mec_aprend, r_max=100):
        """
        :param ambiente: ambiente 2D
        :param mec_aprend: mecanismo de aprendizagem
        :param r_max: reforço máximo
        """
        # inicializar ambiente escolhido
        self.__ambiente = ambiente
        # mecanismo de aprendizagem
        self.__mec_aprend = mec_aprend
        # reforço máximo
        self.__r_max = r_max
        # posição inicial do agente
        self.__s = self.__ambiente.reiniciar()
        # acao inicial do agente
        self.__a = None


    def executar(self, num_episodios) -> list:
        """
        Executar episódios de interação do agente com o ambiente. 
        Durante cada episódio, o agente realiza etapas até que o episódio termine.
        """
        episodio = 0
        num_passos_episodio = []
        while episodio < num_episodios:
            # incrementar episódio
            episodio += 1
            # reiniciar posição
            self.__s = self.__ambiente.reiniciar()
            # reiniciar passos
            num_passos = 0
            # executar episódio
            while not self.__fim_episodio():
                # executar passo do episódio
                r = self.__passo_episodio()
                # incrementar passos
                num_passos += 1
            
            # guardar número de passos
            num_passos_episodio.append(num_passos)
        

        return num_passos_episodio

    def __fim_episodio(self) -> bool:
        """
        Verificar se o episódio terminou com base na presença do alvo
        :return: True se o episódio terminou, False caso contrário
        """
        # obter elemento na posição do agente
        elemento = self.__ambiente.observar()
        # verificar se o elemento é um alvo 
        if elemento == Elemento.ALVO:
            return True
        # caso contrário
        else:
            return False
    
    def __passo_episodio(self):
        """
        Executar um passo dentro de um episódio, onde o agente excuta
        uma acção, observa o ambiente e atualiza a sua posição.
        :return: reforço
        """
        # obter estado seguinte
        sn = self.__ambiente.observar(self.__s)
        # seleccionar acção seguinte
        an = self.__mec_aprend.sel_accao.accao_sofrega(sn)
        # gerar reforço
        r = self._gerar_reforco()
        # aprender
        self.__mec_aprend.aprender(self.__s, self.__a, r, sn, an)
        # actualizar posição
        self.__s = sn
        # actualizar acção
        self.__a = an
       
        # devolver reforço
        return r

    def _gerar_reforco(self):
        """
        Gerar reforço com base no elemento em que o Agente se encontra.
        :return: reforço
        """
        # obter elemento na posição do agente
        elemento = self.__ambiente.observar()
        # verificar se o elemento é um alvo e devolver o reforço máximo
        if elemento == Elemento.ALVO:
            return self.__r_max
        # verificar se o elemento é um obstáculo e devolver o reforço máximo negativo
        elif elemento == Elemento.OBSTACULO:
            return self.__r_max * -1
        # caso contrário
        else:
            return 0
    
    

