# coding=utf-8
import random
import itertools
from simpleai.search import CspProblem, backtrack, min_conflicts

# Dada la pirámide de números de la imagen, se desea rellenar los casilleros utilizando números del 1 al 50,
# de forma tal que cada casillero tenga el valor resultante de la suma de sus dos casilleros inferiores, 
# y que no haya dos casilleros con el mismo número.

#      | 48 | 
#     | - | - |
#   | - | - | - |
# | 5 | 8 | - | 3 |

# ¡ Esta solución no es válida! Nunca se va a encontrar una solución, si el campo 10 fuera 50 si lo haría.

restricciones = []

variables = tuple(a for a in range(11) if a != 0) # Arranca de la izq inferior contando por casillero.
dominios = dict((a, [str(b) for b in range(51) if b != 0 and b != 5 and b != 8 and b != 3 and b != 48]) for a in variables) 
dominios[1] = ['5']
dominios[2] = ['8']
dominios[4] = ['3']
dominios[10] = ['50']
dominios[5] = ['13']
otro = ((2,3,6), (3,4,7), (5,6,8), (6,7,9), (8,9,10))

def aa(var, val):
	x,y,z = val
	return int(z) == (int(x) + int(y))

def todos(var,val):
	return len(set(val)) == 10

for a in otro:
	restricciones.append((a, aa))
restricciones.append((variables,todos))

problem = CspProblem(variables, dominios, restricciones)
resultado = backtrack(problem = problem)
print resultado