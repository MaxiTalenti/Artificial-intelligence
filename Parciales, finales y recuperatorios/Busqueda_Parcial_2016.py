# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer, WebViewer
import random

# Contamos con un tablero de 3x3, y tiene todos los elementos despintads, hay que pintarlos disparando a un casillero, se pinta
# además de este, sus adyacentes, buscar la cantidad mínima de disparos a realizar para pintar el tablero entero.

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

problema = problem(((0,0,0),(0,1,0),(0,2,0),(1,0,0),(1,1,0),(1,2,0),(2,0,0),(2,1,0),(2,2,0)))
visor = BaseViewer()
resultado = astar(problema, graph_search=True, viewer=visor)
print resultado
for action, state in resultado.path():
    print 'action', action
    print 'result', resultado