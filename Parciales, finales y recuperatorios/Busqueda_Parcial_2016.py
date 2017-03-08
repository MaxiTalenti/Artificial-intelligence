# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer, WebViewer
import random

class problem(SearchProblem):
    def is_goal(self, state):
        for a in state:
            if a[2] == 0:
                return False
        return True

    def actions(self, state):
        acciones = []
        for a in state:
            if a[2] == 0:
                acciones.append((a[0],a[1]))
                #acciones.append(('Pintar', (a[0],a[1])))
        return acciones

    def result(self, state, actions):
        a,b = actions
        #x,y = b
        statenuevo = list(state)
        statenuevo.remove((a,b,0))
        statenuevo.append((a,b,1))
        if (a-1,b,0) in state:
            statenuevo.remove((a-1,b,0))
            statenuevo.append((a-1,b,1))
        if (a,b-1,0) in state:
            statenuevo.remove((a,b-1,0))
            statenuevo.append((a,b-1,1))
        if (a+1,b,0) in state:
            statenuevo.remove((a+1,b,0))
            statenuevo.append((a+1,b,1))
        if (a,b+1,0) in state:
            statenuevo.remove((a,b+1,0))
            statenuevo.append((a,b+1,1))

        return tuple(statenuevo)

    def heuristic(self, state):
        cantidad = 0
        for a in state:
            x, y , z = a
            if z == 0:
                cantidad = cantidad + 1
        return cantidad/5

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
    return resultado

result = resolver('astar', ((0,0,0),(0,1,0),(0,2,0),(1,0,0),(1,1,0),(1,2,0),(2,0,0),(2,1,0),(2,2,0)), True)
print result
for action, state in result.path():
    print 'action', action
    print 'result', result