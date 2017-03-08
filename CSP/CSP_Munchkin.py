# coding=utf-8
import random
import itertools
from simpleai.search import CspProblem, backtrack, min_conflicts

# En el juego Munchkin, cada jugador tiene un personaje al que puede mejorar aplicando diferentes cartas.
# Estas cartas incluyen cosas como armas, armaduras, pociones, maldiciones, y otros modificadores que incrementan el nivel del personaje,
# haciéndolo más capaz de ganar el juego. Pero existen algunas restricciones respecto a qué cartas pueden utilizarse en un mismo personaje,
# de forma de evitar jugadores “superpoderosos” que degradan la jugabilidad.

# Un jugador tiene que elegir 3 cartas para intentar armar su personaje, y las opciones disponibles son:
# Armadura de madera +1 (800 oro)
# Armadura de hierro +3 (1000 oro)
# Armadura de acero +5 (1300 oro)
# Espada de madera +1 (500 oro)
# Espada de hierro +2 (700 oro)
# Espada de acero +4 (1000 oro)
# Garrote gigante de madera +6 (1300 oro)
# Poción de fuego +5 (1500 oro)
# Poción de hielo +2 (800 oro)
# Poción de ácido +3 (1200 oro)

# Y a la vez, deben cumplirse las siguientes restricciones:
# 	Solo se puede tener 1 armadura
# 	Solo se puede tener 1 arma de mano (espada o garrote)
# 	Solo se dispone de 3000 de oro para gastar (es decir, el valor de las cartas sumadas no puede superar ese monto)
# 	No se pueden mezclar cartas de objetos de fuego con cartas de objetos de madera
# 	Se tiene que lograr un bonificador total (sumando las cartas) mayor a +15
# 	¿Qué 3 cartas puede elegir el jugador para equipar a su personaje?

# ¡ No se encuentra solución porque para obtener una bonificación mayor a +15 solo hay una combinación posible y no cumple ciertas restricciones !

restricciones = []
variables = (1,2,3)
dominios = dict((a, ['AM', 'AH', 'AA', 'EM', 'EH', 'EA', 'G', 'PF', 'PH', 'PA']) for a in variables) 
costos = {'AM' : 800, 'AH' : 1000, 'AA' : 1300, 'EM' : 500, 'EH' : 700, 'EA' : 1000, 'G' : 1300, 'PF' : 1500, 'PH' : 800, 'PA' : 1200}
bonificacion = {'AM' : 1, 'AH' : 3, 'AA' : 5, 'EM' : 1, 'EH' : 2, 'EA' : 4, 'G' : 6, 'PF' : 5, 'PH' : 2, 'PA' : 3}

def unaarmadura(var, val): # Una sola armadura
	return (val.count('AM') + val.count('AH') + val.count('AA')) <= 1

def unaarma(var, val): # Solo se puede tener 1 arma de mano (espada o garrote)
	return (val.count('EM') + val.count('EH') + val.count('EA') + val.count('G')) <= 1

def costomaximo(var, val): # Solo se dispone de 3000 de oro gastar (es decir, el valro de las cartas sumadas no puede superar ese monto)
	return (costos[val[0]] + costos[val[1]] + costos[val[2]]) <= 3000

def nomezclar(var, val): # No se pueden mezclar cartas de objetos de fuego con cartas de objetos de madera
	return not ('PF' in val and ('AM' in val or 'EM' in val or 'G' in val))

def bonificacionmayor(var, val): # Se tiene que lograr un bonificador total (sumando las cartas) mayor a +15
	return (bonificacion[val[0]] + bonificacion[val[1]] + bonificacion[val[2]]) > 15

restricciones.append(((variables), unaarmadura))
restricciones.append(((variables), unaarma))
restricciones.append(((variables), costomaximo))
restricciones.append(((variables), nomezclar))
restricciones.append(((variables), bonificacionmayor))

problem = CspProblem(variables, dominios, restricciones)
resultado = backtrack(problem = problem)
print resultado