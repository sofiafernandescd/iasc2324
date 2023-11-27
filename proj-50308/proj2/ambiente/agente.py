from elemento import Elemento
from ambiente import Ambiente

        
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
        Executar episódios de interação do Agente com o Ambiente. 
        Durante cada episódio, o Agente realiza passos até que o episódio termine.
        """

        num_passos_episodio = []
        for episode in range(num_episodios):
            # reiniciar posição
            self.__s = self.__ambiente.reiniciar()
            # reiniciar passos
            num_passos = 0
            # executar episódio
            while not self.__fim_episodio():
                # executar passo do episódio
                r = self.__passo_episodio()
                #if r==self.__r_max:
                #    print("Encontrou o alvo!")
                #    break
                # incrementar passos
                num_passos += 1
                # mostrar ambiente
                #self.ambiente.mostrar_politica(self.__mec_aprend)
                print("Episódio: ", episode, " Passo: ", num_passos, " Reforço: ", r) #, " Posição: ", self.__s, " Acção: ", self.__a)
                self.__ambiente.mostrar()
                self.__ambiente.mostrar_politica(self.__mec_aprend.obter_politica())
            
            # guardar número de passos
            num_passos_episodio.append(num_passos)
        
        return num_passos_episodio

    def __fim_episodio(self) -> bool:
        """
        Verificar se o episódio terminou com base na presença do alvo
        :return: True se o episódio terminou, False caso contrário
        """
        # obter elemento na posição do agente
        pos, elemento = self.__ambiente.observar()
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
        self.__a = self.__mec_aprend.seleccionar_accao(self.__s)
        # atuar no ambiente
        self.__ambiente.actuar(self.__a)
        # seleccionar acção seguinte
        sn, elem = self.__ambiente.observar()
        # gerar reforço
        r = self.__gerar_reforco(elem, self.__a, sn)
        # verificar se o elemento é um obstáculo
        if elem == Elemento.OBSTACULO:
            print("Bateu num obstáculo!")
            self.__ambiente.voltar(self.__a)
        # verificar se o elemento é um alvo
        elif elem == Elemento.ALVO:
            print("Encontrou o alvo!")
        else:
            self.__ambiente._ambiente[self.__s[1]][self.__s[0]] = " " # limpar posição anterior
            self.__ambiente._ambiente[sn[1]][sn[0]] = "@" # colocar agente na nova posição
        # aprender
        self.__mec_aprend.aprender(self.__s, self.__a, r, sn)
        # actualizar posição
        self.__s = sn
       
        # devolver reforço
        return r
    


    def __gerar_reforco(self, elem, a, sn):
        """
        Gerar reforço com base no elemento em que o Agente se encontra.
        Se o Agente encontrar o alvo, recebe recompensa máxima.
        Se o Agente bater num obstáculo, recebe recompensa máxima negativa.
        :return: reforço
        """
        # verificar se o elemento é um alvo e devolver o reforço máximo
        if elem == Elemento.ALVO:
            return self.__r_max
        # verificar se o elemento é um obstáculo e devolver o reforço máximo negativo
        elif elem == Elemento.OBSTACULO:
            return self.__r_max * -1
        # caso contrário
        else:
            return 0
    
    

