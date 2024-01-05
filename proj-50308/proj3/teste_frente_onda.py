'''
 # @ Author: Your name
 # @ Description:
    Estudo de métodos de raciocínio automático e de arquitectura de agentes deliberativos
    Implementação de um agente deliberativo com planeamento com base no algoritmo Frente-de-Onda
 '''

from agente_delib import AgenteFrenteOnda


AMBIENTE = 2

agente = AgenteFrenteOnda(AMBIENTE)
agente.executar()

