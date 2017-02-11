# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer
import random

INITIAL = [(10,0), (30,0), (60,0), (80,0), (120,0)]
META = [(10,1), (30,1), (60,1), (80,1), (120,1)]

class HnefataflProblema(SearchProblem):
    def is_goal(self, state):
        return state == META

    def actions(self, state):
        if state


    def result(self, state, actions):

    def cost(self, state1, action, state2):

    def heuristic(self, state):

def resolver(metodo_busqueda,jarros,controlar_estados_repetidos):
	problema = HnefataflProblema(jarros)
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
	return resultado

result = astar(HnefataflProblema(INITIAL), graph_search=True, viewer=BaseViewer())
