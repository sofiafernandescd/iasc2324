'''
 # @ Author: Sofia Condesso
 # @ Description:
 O objetivo deste script é implementar uma rede neuronal multicamada com
função de ativação do tipo degrau. A rede neuronal deve ser implementada
com base em matrizes e vetores.
– Implementação e teste dos operadores booleanos OR, AND e NOT
– Implementação e teste do operador XOR
 '''

import numpy as np
from funcaoativacao import FuncaoActivacaoDegrau
from camada import Camada
from redeneuronal import RedeNeuronal


# Testes para operadores booleanos OR, AND, NOT e XOR
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

funcao_ativacao_degrau = FuncaoActivacaoDegrau()

# Exemplo OR
print("Exemplo OR")
or_rede = RedeNeuronal()
or_rede.juntar(Camada(funcao_ativacao_degrau, 2, 1))
or_rede.actualizar(np.array([[1], [1]]), np.array([-0.5]))

for entrada in entradas:
    saida = or_rede.activar(entrada)
    print(f"OR({entrada}) = {saida[0]}")
print()

# Exemplo AND
print("Exemplo AND")
and_rede = RedeNeuronal()
and_rede.juntar(Camada(funcao_ativacao_degrau, 2, 1))
and_rede.actualizar(np.array([[1], [1]]), np.array([-1.5]))

for entrada in entradas:
    saida = and_rede.activar(entrada)
    print(f"AND({entrada}) = {saida}")
print()

# Exemplo NOT
print("Exemplo NOT")
not_rede = RedeNeuronal()
not_rede.juntar(Camada(funcao_ativacao_degrau, 1, 1))

pesos1 = [[-1]]
pendores1 = [1]
not_rede.actualizar(pesos1, pendores1)

for entrada in [[0], [1]]:
    saida = not_rede.activar(entrada)
    print(f"NOT({entrada}) = {saida}")
print()


# Exemplo XOR
print("Exemplo XOR")
xor_rede = RedeNeuronal()
xor_rede.juntar(Camada(funcao_ativacao_degrau, 2, 2))
xor_rede.juntar(Camada(funcao_ativacao_degrau, 2, 1))
## Definição dos pesos e pendores da primeira camada (2 neurónios)
pesos1 = [[1, -1], [-1, 1]]
pendores1 = [-0.5, -0.5]

## Definição dos pesos e pendores da camada de saída (1 neurónio)
pesos2 = [1, 1]
pendores2 = [-0.5]

xor_rede.actualizar([pesos1, pesos2], [pendores1, pendores2])

for entrada in entradas:
    saida = xor_rede.activar(entrada)
    print(f"XOR({entrada}) = {saida}")
print()



