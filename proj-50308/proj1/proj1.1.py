'''
 # @ Autor: Sofia Condesso (50308) - MEIM
 # @ Hora de Criação: 2023-09-22 17:33:57
 # @ Descrição: 
 # Este script tem como objetivo implementar a função XOR com uma rede neuronal do tipo perceptrão. 
 # A rede terá uma camada escondida e será representada por matrizes e vetores. 
 # A função de ativação será a função degrau.
 '''

import numpy as np

## Definição do conjunto de entrada (quatro entradas do tipo [x1, x2])
# Combinações para as quais queremos avaliar a função XOR 
conjunto_entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]
# Se estivessemos a fazer aprendizagem também poderiamos experimentar com nuvens de pontos vizinhos, o que nos permitia ter mais dados de treino e teste
# E, por isso, um modelo mais ajustado e bem avaliado, do ponto de vista da forma geométrica tomada pelo problema XOR. Exemplo:
# conjunto_entrada = [[0, 0], [0, 1], [1, 0], [1, 1], [0.1, 0.1], [0.1, 1.1], [1.1, 0.1], [1.1, 1.1], ...]
print(f"Conjunto de entrada: \n{conjunto_entrada}\n")

## Definição dos pesos e pendores da primeira camada (2 neurónios)
pesos1 = [[1, -1], [-1, 1]]
pendores1 = [-0.5, -0.5]

## Definição dos pesos e pendores da camada de saída (1 neurónio)
pesos2 = [1, 1]
pendores2 = [-0.5]

## Exemplo da utilização da função heaviside do numpy
y = np.heaviside(conjunto_entrada, 0) # função degrau
print(f"Função heaviside: \n{y}\n")


def funcao_ativacao_degrau(
    x: float
    ) -> float:
    """Função de ativação degrau
    Esta função retorna 0 se x for menor ou igual a 0 e 1 caso contrário.

    Args:
        x (float): Valor de entrada no neurónio

    Returns:
        float: Valor de saída do neurónio
    """
    return np.heaviside(x, 0)

def activar(
    entrada: float, 
    pesos: float, 
    pendores: float
    ) -> float:
    """
    Aplicar a função de ativação ao produto interno dos pesos e 
    entradas somado com os pendores

    Args:
        entrada (float): Valores de entrada
        pesos (float): Pesos que ligam uma camada à camada anterior
        pendores (float): Pendores da camada

    Returns:
        float: Valores de saida do neurónio
    """
    y = np.dot(entrada, pesos) + pendores
    saida = funcao_ativacao_degrau(y)
    return saida


def main1():
    """
    Versão com dois ciclos for.
    Os valores de saída do primeiro ciclo (camada escondida) são guardados 
    para serem usados como entrada do segundo ciclo (camada de saída).
    """

    print("Versão com dois ciclos for:")

    # Inicializar conjunto para guardar os valores de saída da camada escondida
    conjunto_entrada2 = []
    # Para cada entrada do conjunto de entrada
    for entrada in conjunto_entrada:
        # Calcular a ativação dos neurónios da camada escondida
        saida = activar(entrada, pesos1, pendores1)
        # Guardar os valores de saída
        conjunto_entrada2.append(saida)
        print(entrada, saida)

    print()
    # Para cada entrada da camada escondida
    for entrada in conjunto_entrada2:
        # Calcular a ativação do neurónio de saída
        saida = activar(entrada, pesos2, pendores2)
        print(entrada, saida)

    print()

main1()

def main2():
    """
    Versão com um ciclo for.
    Os valores de saída da camada escondida são usados como entrada da 
    camada de saída, utilizando apenas um ciclo.
    """
    print("Versão com um ciclo for:")
    # Para cada entrada do conjunto de entrada
    for entrada in conjunto_entrada:
        # Calcular a ativação dos neurónios da camada escondida
        saida = activar(entrada, pesos1, pendores1)
        # Calcular a ativação do neurónio de saída
        saida = activar(saida, pesos2, pendores2)
        print(entrada, saida)

    print()


main2()

def main3():
    """
    Versão sem utilização de ciclo for.
    Dado que trabalhamos com matrizes e vetores, a função heaviside
    do numpy pode ser utilizada diretamente com os conjuntos de entrada e
    respetivos conjuntos de saída
    """
    print("Versão sem utilização de ciclo for:")
    # Calcular a ativação dos neurónios da camada escondida
    saida = activar(conjunto_entrada, pesos1, pendores1)
    # Calcular a ativação do neurónio de saída 
    saida = activar(saida, pesos2, pendores2)
    print(conjunto_entrada, saida)
    print()


main3()

"""
Conclusão: Em todos os casos, a saída é igual, pois os pesos e pendores são os mesmos.
Se alterarmos os valores dos pesos e pendores de forma proporcional (ex: multiplicar por 10) 
os resultados de saída seriam os mesmos.
"""

print("Exemplo de alteração dos pesos e pendores:")
## Definição dos pesos e pendores da primeira camada (2 neurónios)
pesos1 = [[10, -10], [-10, 10]]
pendores1 = [-5, -5]

## Definição dos pesos e pendores da camada de saída (1 neurónio)
pesos2 = [10, 10]
pendores2 = [-5]

# Calcular a ativação dos neurónios da camada escondida
saida = activar(conjunto_entrada, pesos1, pendores1)
# Calcular a ativação do neurónio de saída 
saida = activar(saida, pesos2, pendores2)
print(conjunto_entrada, saida)
