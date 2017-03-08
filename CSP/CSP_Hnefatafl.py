# coding=utf-8
import random
import itertools
from simpleai.search import CspProblem, backtrack, min_conflicts

# Se desea resolver el siguiente problema: dado el mismo tablero de 7x7, llenar el tablero de reyes y soldados,
# pero respetando las siguientes condiciones:
#	un rey nunca puede tener más de 1 (otro) rey en sus casillas adyacentes,
#	y la cantidad total de soldados debe mayor que la cantidad de reyes,
#	pero menor al doble de la cantidad total de reyes (ej: si hay 10 reyes, puede haber 15 soldados , pero no 5 soldados, 20 soldados, ni 30 soldados).

restricciones = []
variables = tuple((a,b) for a in range(7) for b in range(7))
dominios = dict((a, ['R', 'S']) for a in variables) 

def casillasadyacentes(var, val): # Un rey nunca puede tener más de 1 (otro) rey en sus casillas aydacentes.
	return val.count('R') <= 2

def soldadosmayores(var, val): # La cantidad total de soldados debe ser mayor que la cantidad de reyes.
	return val.count('S') > val.count('R')

def otroscalculos(var, val): # La cantidad de soldados tiene que ser menor al doble de reyes.
	soldados = val.count('S')
	reyes = val.count('R')
	return soldados < reyes * 2

for a in variables: # Obtiene adyacentes y casilla a la cuales son adyacentes
	x, y = a
	casillas = []
	if (x-1, y) in variables:
		casillas.append((x-1,y))
	if (x+1, y) in variables:
		casillas.append((x+1, y))
	if (x, y-1) in variables:
		casillas.append((x, y-1))
	if (x, y+1) in variables:
		casillas.append((x, y+1))
	casillas.append((a))
	restricciones.append(((tuple(casillas)), casillasadyacentes))
restricciones.append(((variables), soldadosmayores))
restricciones.append(((variables), otroscalculos))

problem = CspProblem(variables, dominios, restricciones)
resultado = backtrack(problem = problem)
print resultado
for a in resultado: # Para que se vea más entendible.
	if resultado[a] == 'S':
		resultado[a] = '-'
print ''
for a in range(7):
	print '{:<2} | {:<2}| {:<2}| {:<2}| {:<2}| {:<2}| {:<2}| {:<2}|'.format(a, resultado[a, 0], resultado[a, 1], resultado[a, 2],
		resultado[a, 3], resultado[a, 4], resultado[a, 5], resultado[a, 6])
print ''
print 'Reyes', resultado.values().count('R')
print 'Soldados', resultado.values().count('-')
# --- > Solución encontrada < ---

# {(1, 3): 'S', (6, 6): 'S', (3, 0): 'S', (3, 2): 'S', (2, 1): 'R', (0, 0): 'R', (1, 6): 'R', (5, 1): 'S', (2, 5): 'S', (0, 3): 'R',
# (4, 0): 'R', (1, 2): 'S', (3, 3): 'S', (1, 5): 'S', (4, 4): 'S', (6, 3): 'S', (5, 6): 'R', (5, 0): 'S', (2, 2): 'S', (5, 3): 'R',
# (4, 1): 'R', (1, 1): 'S', (6, 4): 'S', (5, 4): 'S', (2, 6): 'S', (3, 6): 'R', (4, 5): 'S', (0, 4): 'R', (5, 5): 'R', (1, 4): 'S',
# (6, 0): 'R', (0, 5): 'S', (4, 2): 'S', (1, 0): 'S', (6, 5): 'S', (3, 5): 'R', (0, 1): 'R', (0, 2): 'S', (4, 6): 'S', (3, 4): 'S',
# (6, 1): 'R', (3, 1): 'S', (0, 6): 'R', (2, 0): 'R', (6, 2): 'S', (4, 3): 'R', (2, 3): 'R', (5, 2): 'S', (2, 4): 'R'}

#  6  | R | R | S | R | S | R | S |
#  5  | S | S | S | R | S | R | S |
#  4  | R | S | R | S | S | S | S |
#  3  | R | S | R | S | R | R | S |
#  2  | S | S | S | S | S | S | S |
#  1  | R | S | R | S | R | S | R |
#  0  | R | S | R | S | R | S | R |
#       0   1   2   3   4   5   6

# Cantidades:
# 	Soldados = 29
# 	Reyes = 20