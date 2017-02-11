# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer, WebViewer
import random

pintados = []

class problem(SearchProblem):
    def is_goal(self, state):
        for a in state:
            if a[2] == 0:
                return False
        return True

    def actions(self, state):
        print 'actions'
        acciones = []
        for a in state:
            acciones.append((a[0],a[1]))
        return acciones

    def results(self, state, actions):
        a,b = actions
        statenuevo = state[:]
        statenuevo.remove(actions)
        statenuevo.append((a,b,1))
        if (a-1,b,0) in state:
            statenuevo.remove(a-1,b,0)
            statenuevo.append(a-1,b,1)
        if (a,b-1,0) in state:
            statenuevo.remove(a,b-1,0)
            statenuevo.remove(a,b-1,1)
        return statenuevo

    def heuristic(self, state):
        return len(state)/5

    def cost(self, state1, action, state2):
        return 1

def resolver(metodo_busqueda,initial,controlar_estados_repetidos):
	problema = problem(initial)
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

resolver('breadth_first', [(0,0,0),(0,1,0),(0,2,0),(1,0,0),(1,1,0),(1,2,0),(2,0,0),(2,1,0),(2,2,0)], True)
