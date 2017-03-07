# coding=utf-8
import random
import itertools
from simpleai.search import CspProblem, backtrack, min_conflicts

# ¡ No terminado !

# Un “cuadrado mágico” en matemáticas es una grilla cuadrada de NxN, que es rellenada con los números del 1 al (NxN),
# de forma tal que cada fila y cada columna de la grilla suman lo mismo.
# Por ejemplo, a la derecha se muestra un posible cuadrado mágico de 3x3, donde todas las filas y columnas suman 15
# (y como la definición lo dice, fue rellenado con los números del 1 al 9).
# Se desea generar un cuadrado mágico de 5x5, es posible?

restricciones = []

N = 3
variables = tuple((a,b) for a in range(N) for b in range(N)) # Arranca de la izq inferior contando por casillero.
dominios = dict((a, [b for b in range(N*N+1)]) for a in variables)

def comprobarsuma(var, val):
	return sum(val[N:]) == sum(val[:N])

def todos(var, val):
	return val[0] != val[1]

for a in itertools.combinations(variables, 2): # Para restricciones binarias.
	restricciones.append((a, todos))

filas = [tuple([(f, c) for c in range(N)]) for f in range(N)]
filasycolumnas = filas + filas

for a, b in itertools.combinations(filasycolumnas, 2):
	if len(set(a+b)) > 1:
		restricciones.append(((a+b), comprobarsuma))

problem = CspProblem(variables, dominios, restricciones)
resultado = backtrack(problem = problem)
print resultado
print ''
for a in range(N):
	print '{:<2} | {:<3} | {:<3} | {:<3} |'.format(a, resultado[a, 0], resultado[a, 1], resultado[a, 2])