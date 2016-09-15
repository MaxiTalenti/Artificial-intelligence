# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer
import random

PEONES = [(0,0),(0,2),(0,4),(0,6),(1,4),(2,0),(3,1),(3,6),(3,7),(3,9),(4,0),(4,7),(4,8),(5,4),
(5,9),(6,0),(6,5),(6,9),(7,0),(7,7),(8,2),(8,4),(8,9),(9,1),(9,4),(9,6),(9,7)]

fila_t,col_t = (9,9) #TAMAÑO TABLERO

def muerte_rey(state):
	fila_r,col_r = state 

	cant_peones = 0 
	if fila_r > 0: # Verificar si existe peon arriba
		if (fila_r - 1, col_r) in PEONES:
			cant_peones=cant_peones + 1
	if fila_r < fila_t: # Verificar si existe peon abajo
		if (fila_r + 1, col_r) in PEONES:
			cant_peones=cant_peones + 1
	if col_r > 0: # Verificar si existe peon a la iqzuierda
		if (fila_r, col_r -1) in PEONES:
			cant_peones=cant_peones + 1
	if col_r < col_t: # Verificar si existe peon a la derecha
		if (fila_r, col_r + 1) in PEONES:
			cant_peones=cant_peones + 1
	return cant_peones < 2

class HnefataflProblema(SearchProblem):
	def is_goal(self, state):
		fila_r,col_r = state
		return (fila_r in [0,9] or col_r in [0,9])

	def actions(self, state):
		fila_r, col_r = state
		actions = []
		if fila_r > 0: # Arriba
			if (fila_r - 1, col_r) not in PEONES and (muerte_rey((fila_r - 1,col_r))):
				actions.append(('Arriba',(-1,0)))
		if fila_r < fila_t: # Abajo
			if (fila_r + 1 , col_r) not in PEONES and (muerte_rey((fila_r + 1,col_r))):
				actions.append(('Abajo',(1,0)))
		if col_r > 0: # Derecha
			if (fila_r , col_r - 1) not in PEONES and (muerte_rey((fila_r, col_r - 1))):
				actions.append(('Izquierda',(0,-1)))
		if col_r < col_t: # Izquierda
			if (fila_r ,col_r + 1) not in PEONES and (muerte_rey((fila_r, col_r + 1))):
				actions.append(('Derecha',(0,1)))
		return actions

	def result(self, state, actions):
		fila_r,col_r = state
		return (fila_r + actions[1][0], col_r + actions[1][1])

	def cost(self, state1, action, state2):
		return 1

	def heuristic(self, state):
		fila_r,col_r = state 
		heuristica =[fila_r, col_r , (fila_t - fila_r) , (col_t - col_r)]
		return min(heuristica)

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
	print(visor.stats)
	return resultado



