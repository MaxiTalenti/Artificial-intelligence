# coding=utf-8

from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer

# Mover de R a F con el menor costo posible. (El costo es el número del casillero)

# 4 | R  | 4  | 50 | 3  | 5  |
# 3 | 8  | 14 | 23 | 22 | 9  |
# 2 | 5  | 25 | 40 | 12 | 4  |
# 1 | 15 | 18 | 37 | 18 | 12 |
# 0 | 2  | 1  | 7  | 13 | F  |
#      0   1    2    3    4

# Fila, columna
TABLERO = {(0,0) : 2, (1,0) : 15, (2,0) : 5, (3,0) : 8, (0,1) : 1, (1,1) : 18, (2,1) : 25, (3,1) : 14, (4,1) : 50, (0,2) : 7, (1,2) : 37,
(2,2) : 40, (3,2) : 23, (4,2) : 50, (0,3) : 13, (1,3) : 18, (2,3) : 12, (3,3) : 22, (4,3) : 3, (1,4) : 12, (2,4) : 4, (3,4) : 9, (4,4) : 5,
(0,4) : 0}

FINAL = (0,4)
ESTADO = (4,0)

class Problema(SearchProblem):

    def is_goal(self, state):
        return state == FINAL

    def actions(self, state):
        actions = []
        x, y = state
        if (x-1, y) in TABLERO:
            actions.append((x-1,y))
        if (x+1, y) in TABLERO:
            actions.append((x+1, y))
        if (x, y-1) in TABLERO:
            actions.append((x,y-1))
        if (x, y+1) in TABLERO:
            actions.append((x,y+1))
        return actions

    def result(self, state, action):
        return action

    def cost(self, state1, action, state2):
        return TABLERO[action]

    def heuristic(self, state):
        x, y = state
        xx, yy = FINAL
        return min([abs(x-xx), abs(y-yy)])


problema = Problema(ESTADO)
visor = BaseViewer()
resultado = astar(problema, graph_search=True, viewer=visor)
for a in resultado.path():
	print 'Step', a
print resultado