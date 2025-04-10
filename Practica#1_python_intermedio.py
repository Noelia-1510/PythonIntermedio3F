#1 Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A o en B, o en ambos.

conjuntoA = {1,2,3,6}
conjuntoB = {1,2,3,4,5,7} 

print(conjuntoA | conjuntoB)

#2 Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A y en B.

conjuntoA = {1,2,3,6}
conjuntoB = {1,2,3,4,5,7} 

print(conjuntoA & conjuntoB)

#3 Dados dos conjuntos, A y B, escribe un programa en Python que imprima el conjunto de los elementos que se encuentran en A o en B, pero no en ambos.

conjuntoA = {1,2,3,6}
conjuntoB = {1,2,3,4,5,7} 

print(conjuntoA.symmetric_difference(conjuntoB))

#4 Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto de otro conjunto, B.

conjuntoA = {1,2,3,6}
conjuntoB = {1,2,3,4,5,7} 

print(conjuntoA.issubset(conjuntoB))

#5 Dados un conjunto, A, escribe un programa en Python que imprima el número de elementos del conjunto.

conjuntoA = {1,2,3,5,6}
numero_elementos = len(conjuntoA)

print(numero_elementos)
