# coding=utf-8
import random
import itertools
from simpleai.search import CspProblem, backtrack, min_conflicts

# P = Prohibido
# A = Puesta en defensiva

# 3 | - | - | P | - | A | 
# 2 | - | - | - | P | - | 
# 1 | - | P | - | - | - | 
# 0 | - | - | A | - | - | 
#     0   1   2   3   4

# --> Parte CSP <-- 
# Luego del último ataque, se decidió incrementar el número de robots a 6, y ya no permanecerán almacenados,
# sino que se ubicarán en posiciones defensivas fijas y permanentes. Pero deben respetarse algunas restricciones:

# - No puede haber dos robots en la misma habitación, generarían demasiadas molestias para los científicos.
# - No puede haber dos robots en habitaciones adyacentes, impedirían demasiado la circulación.
# - Las habitaciones restringidas siguen sin poder contener robots.
# - Las dos habitaciones que poseen puertas al exterior deben contener un robot.

restricciones = []

variables = (1,2,3,4,5,6) # Los 6 robots
dominios = dict((a, [(b, c) for b in range(5) for c in range(4)]) for a in variables) 
# Quito las habitaciones prohibidas.
dominios[1].remove((1,1))
dominios[1].remove((2,3))
dominios[1].remove((3,2))
dominios[2].remove((1,1))
dominios[2].remove((2,3))
dominios[2].remove((3,2))
dominios[3].remove((1,1))
dominios[3].remove((2,3))
dominios[3].remove((3,2))
dominios[4].remove((1,1))
dominios[4].remove((2,3))
dominios[4].remove((3,2))
dominios[5].remove((1,1))
dominios[5].remove((2,3))
dominios[5].remove((3,2))
dominios[6].remove((1,1))
dominios[6].remove((2,3))
dominios[6].remove((3,2))

def habitacionesiguales(var, val):
	return len(set(val)) == 6

def habitacionesadyacentes(var, val):
	for a in val:
		x, y = a
		if (x-1, y) in val:
			return False
		if (x+1, y) in val:
			return False
		if (x, y-1) in val:
			return False
		if (x, y+1) in val:
			return False
	return True

def salidasconrobots(var, val):
	return (val.count((2,0)) + val.count((4,3))) == 2

def habitacionesprohibidas(var, val): # Ya se hizo eliminandolos del dominio, sino usar este método.
	return (val.count((2,3)) + val.count((3,2)) + val.count((1,1))) == 0

restricciones.append(((variables),habitacionesiguales))
restricciones.append(((variables), habitacionesadyacentes))
restricciones.append(((variables), salidasconrobots))

problem = CspProblem(variables, dominios, restricciones)
resultado = backtrack(problem = problem)
print resultado

# SOLUCIÓN:
# {1: (0, 0), 2: (0, 2), 3: (1, 3), 4: (2, 0), 5: (2, 2), 6: (4, 3)}

# 3 | - | R | X | - | R | 
# 2 | R | - | R | X | - | 
# 1 | - | X | - | - | - | 
# 0 | R | - | R | - | - | 
#     0   1   2   3   4