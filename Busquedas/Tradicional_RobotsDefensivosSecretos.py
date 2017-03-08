# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer
import random

# Se poseen dos robots para custodiar un centro de investigación secreto. 
# Los robots permanecen almacenados en espera, y frente a alguna emergencia deben reaccionar ubicándose en posiciones defensivas.
# El centro de investigación posee habitaciones en forma de grilla, pero algunas de ellas no son accesibles para los robots, 
# por riesgo de contaminación. Los robots sólo pueden moverse entre habitaciones adyacentes.
# Se debe resolver la “puesta en defensiva” como un problema de búsqueda, con el objetivo de encontrar el camino más óptimo.

# E = Espera
# P = Prohibido
# A = Puesta en defensiva

# 3 | - | E | P | - | A | 
# 2 | - | - | - | P | - | 
# 1 | - | P | - | - | - | 
# 0 | - | - | A | - | - | 
#     0   1   2   3   4

INITIAL = ((1,3), (1,3))
HABITACIONES = ((0,0), (0,1), (0,2), (0,3), (1,0), (1,2), (1,3), (2,0), (2,1), (2,2), (3,0), (3,1), (3,3), (4,0), (4,1), (4,2), (4,3))
POS_DEFENSIVAS = ((2,0), (4,3))

class HnefataflProblema(SearchProblem):

	def is_goal(self, state):
		rob_1, rob_2 = state
		if rob_1 not in POS_DEFENSIVAS:
			return False
		if rob_2 not in POS_DEFENSIVAS:
			return False
		return True

	def actions(self, state):
		rob_1, rob_2 = state
		x_1, y_1 = rob_1
		x_2, y_2 = rob_2
		acciones = []
		# Los AND en los If fueron agregados para que no puedan estar en la misma habitacion los robots, sino sacar.
		if (x_1+1, y_1) in HABITACIONES and (x_1+1, y_1) != (x_2, y_2):
			acciones.append(('Mover R1', (x_1+1,y_1)))
		if (x_1-1, y_1) in HABITACIONES and (x_1-1, y_1) != (x_2, y_2):
			acciones.append(('Mover R1', (x_1-1,y_1)))
		if (x_1, y_1+1) in HABITACIONES and (x_1, y_1+1) != (x_2, y_2):
			acciones.append(('Mover R1', (x_1,y_1+1)))
		if (x_1, y_1-1) in HABITACIONES and (x_1, y_1-1) != (x_2, y_2):
			acciones.append(('Mover R1', (x_1,y_1-1)))

		if (x_2+1, y_2) in HABITACIONES and (x_2+1, y_2) != (x_1, y_1):
			acciones.append(('Mover R2', (x_2+1,y_2)))
		if (x_2-1, y_2) in HABITACIONES and (x_2-1, y_2) != (x_1, y_1):
			acciones.append(('Mover R2', (x_2-1,y_2)))
		if (x_2, y_2+1) in HABITACIONES and (x_2, y_2+1) != (x_1, y_1):
			acciones.append(('Mover R2', (x_2,y_2+1)))
		if (x_2, y_2-1) in HABITACIONES and (x_2, y_2-1) != (x_1, y_1):
			acciones.append(('Mover R2', (x_2,y_2-1)))

		return acciones

	def result(self, state, actions):
		rob_1, rob_2 = state
		x_1, y_1 = rob_1
		x_2, y_2 = rob_2
		accion, posicion = actions
		x_new, y_new = posicion

		if accion == 'Mover R1':
			x_1 = x_new
			y_1 = y_new
		else:
			x_2 = x_new
			y_2 = y_new
		return ((x_1, y_1), (x_2, y_2))

	def cost(self, state1, action, state2):
		return 1

	def heuristic(self, state):
		rob_1, rob_2 = state
		x_1, y_1 = rob_1
		x_2, y_2 = rob_2
		pos_1, pos_2 = POS_DEFENSIVAS
		x_p1, y_p1 = pos_1
		x_p2, y_p2 = pos_2

		return min([abs(x_1 - x_p1), abs(x_1 - x_p2), abs(y_1 - y_p1), abs(y_1 - y_p2)]) + min([abs(x_2 - x_p1), abs(x_2 - x_p2), abs(y_2 - y_p1), abs(y_2 - y_p2)])
		

def resolver(metodo_busqueda,posicion_rey,controlar_estados_repetidos):
	problema = HnefataflProblema(posicion_rey)
	visor = BaseViewer()
	#Busquedas, Grafo -> graph_search=True
	if (metodo_busqueda == 'breadth_first'): # En amplitud
		resultado = breadth_first(problema, graph_search=controlar_estados_repetidos, viewer=visor)
	elif (metodo_busqueda == 'depth_first'): # Profundidad
		resultado = depth_first(problema, graph_search=controlar_estados_repetidos, viewer=visor)
	elif (metodo_busqueda == 'greedy'): # Avara
		resultado = greedy(problema, graph_search=controlar_estados_repetidos, viewer=visor)
	elif (metodo_busqueda == 'astar'): # Estrella
		resultado = astar(problema, graph_search=controlar_estados_repetidos, viewer=visor)
	for a in resultado.path():
		print a
	return resultado

resolver('astar', INITIAL, True)