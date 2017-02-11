# coding=utf-8
import random
import itertools
from simpleai.search import CspProblem, backtrack, min_conflicts

N = 3 # Tamaño de TABLERO

variables = [(f, c) for f in range(N) for c in range(N)]
dominios = {var: list(range(1, N*N+1)) for var in variables}
restricciones = []

def distinto_valor(var, val):
    return val[0] != val[1]

def suman_lo_mismo(var, val):
    return sum(val[:N]) == sum(val[N:])

for var1, var2 in itertools.combinations(variables, 2):
    restricciones.append(((var1, var2), distinto_valor))

filas = []
for f in range(N):
    fila_actual = []
    for c in range(N):
        fila_actual.append((f, c))
    filas.append(fila_actual)

columnas = []
for c in range(N):
    columnas.append([(f,c) for f in range(N)])

diagonales = [[(i,i) for i in range(N)],[(i,N-(i+1)) for i in range (N)]]
for l in range(N):
    diagonales.append([])

for cosa1, cosa2, in itertools.combinations(filas + columnas + diagonales, 2):
    restricciones.append((cosa1 + cosa2, suman_lo_mismo))


if __name__ !=  '__main__':
    p = CspProblem(variables, dominios, restricciones)
