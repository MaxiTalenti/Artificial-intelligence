# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer
import random

# La pantalla posee 3 casillas alineadas una al lado de la otra, cada una con un número dentro.
# Inicialmente todas poseen el número cero. Los botones que pueden presionarse son los siguientes:
# Botón rojo: Suma 3 al casillero inicial.
# Botón verde: Resta 2 al casillero inicial.
# Botón amarillo: Intercambia los valores de las dos primeras casillas.
# Botón celeste: Intercambia los valores de las dos últimas primeras casillas.
# La secuencia de números que se debe lograr para abrir la escotilla es la siguiente:  5, 1, 8

INITIAL = (0,0,0)

class HnefataflProblema(SearchProblem):

	def is_goal(self, state):
		return state == (5,1,8)

	def actions(self, state):
		a, b, c = state
		actions = []
		actions.append(('Rojo', (a+3,b,c)))
		actions.append(('Verde', (a-2,b,c)))
		actions.append(('Amarillo', (b,a,c)))
		actions.append(('Celeste', (a,c,b)))
		return actions

	def result(self, state, actions):
		return actions[1]

	def cost(self, state1, action, state2):
		return 1

	def heuristic(self, state):
		a,b,c = state
		contador = 0
		if a != 5:
			contador = contador + 1
		if b != 1:
			contador = contador + 1
		if c != 8:
			contador = contador + 1
		return contador

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