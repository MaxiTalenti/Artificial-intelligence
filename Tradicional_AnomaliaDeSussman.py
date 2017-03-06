# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer
import random

# Se tiene un tablero con bloques sobre el mismo.
# Además se cuenta con un brazo robot capaz de tomar un bloque a la vez y moverlo. 
# Se desea encontrar una secuencia de acciones para llegar al estado final, a partir del estado inicial.
# Se tiene como restricción que no se puede mover un bloque que tenga otro encima. 

# |   | C
# | B | A

#  Meta
# | A |
# | B |
# | C |

INITIAL = ((), ('B'), ('C', 'A'))

class HnefataflProblema(SearchProblem):

	def is_goal(self, state):
		pila1, pila2, pila3 = state
		if pila1 == ('C', 'B', 'A'):
			return True
		if pila2 == ('C', 'B', 'A'):
			return True
		if pila3 == ('C', 'B', 'A'):
			return True
		return False

	def actions(self, state):
		pila1, pila2, pila3 = state
		acciones = []
		for a in pila1:
			acciones.append(('Sacar en 1 y poner en 2', (0, 1)))
			acciones.append(('Sacar en 1 y poner en 3', (0, 2)))
		for a in pila2:
			acciones.append(('Sacar en 2 y poner en 1', (1, 0)))
			acciones.append(('Sacar en 2 y poner en 3', (1, 2)))
		for a in pila3:
			acciones.append(('Sacar en 3 y poner en 1', (2, 0)))
			acciones.append(('Sacar en 3 y poner en 2', (2, 1)))
		return acciones

	def result(self, state, actions):
		sacar, poner = actions[1]
		a, b, c = state
		listaasacar = list(state[sacar])
		listaaponer = list(state[poner])
		elemento = listaasacar[-1]
		listaaponer.append(elemento) # Se agrega el último elemento de la lista a sacar.
		listaasacar = listaasacar[:len(listaasacar)-1] # Se quita el último elemento de la lista a sacar.
		statenuevo = list(state)
		statenuevo[sacar] = tuple(listaasacar)
		statenuevo[poner] = tuple(listaaponer)

		return tuple(statenuevo)

	def cost(self, state1, action, state2):
		return 1

	def heuristic(self, state):
		pila1, pila2, pila3 = state
		cantidad = 0
		for x, a in enumerate(pila1):
			if x == 0 and a != 'C':
				cantidad = cantidad + 1
			if x == 1 and a != 'B':
				cantidad = cantidad + 1
			if x == 2 and a != 'A':
				cantidad = cantidad + 1
		for x, a in enumerate(pila2):
			if x == 0 and a != 'C':
				cantidad = cantidad + 1
			if x == 1 and a != 'B':
				cantidad = cantidad + 1
			if x == 2 and a != 'A':
				cantidad = cantidad + 1
		for x, a in enumerate(pila3):
			if x == 0 and a != 'C':
				cantidad = cantidad + 1
			if x == 1 and a != 'B':
				cantidad = cantidad + 1
			if x == 2 and a != 'A':
				cantidad = cantidad + 1
		return cantidad

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