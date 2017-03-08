# coding=utf-8

# Luego de que ambientalistas logren prohibir el uso de animales vivos para experimentos, 
# un grupo de científicos se encuentra con la necesidad de programar un robot que simule
# el comportamiento de ratas de laboratorio dentro de laberintos. 
# El robot debe poder encontrar 3 “comidas” escondidas dentro, “ingerirlas”, 
# y salir del laberinto al finalizar su “alimentación”. El laberinto, con la entrada y las comidas, es el que se ve en la figura.


from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer

# 5 ['.', '.', '.', 'P', '.', 'P']
# 4 ['.', 'P', 'C', 'P', '.', '.']
# 3 ['.', '.', 'P', '.', 'P', 'S'] <- Salida.
# 2 ['P', '.', '.', '.', 'C', 'R']
# 1 ['C', 'P', '.', 'P', '.', 'P']
# 0 ['.', '.', '.', 'P', '.', '.']
#     0    1    2    3    4    5

FINAL = (5,3) # Casilla por la cual debe salir

PAREDES = ((0,2), (1,1), (1,4), (2,3), (3,0), (3,1), (3,4), (3,5), (4,3), (5,1), (5,5))

ESTADO = ((5,2), # Robot
         ((0,1), (2,4), (4,2))) # Comidas

class Problema(SearchProblem):

    def is_goal(self, state):
        robot, comidas = state
        return (robot == FINAL and len(comidas) == 0)

    def actions(self, state):
        robot, comidas = state
        x, y = robot
        acciones = []

        if x < 5 and (x+1,y) not in PAREDES:
        	acciones.append(('Derecha', (x+1,y)))
        if x > 0 and (x-1,y) not in PAREDES:
        	acciones.append(('Izquierda', (x-1,y)))
        if y < 5 and (x,y+1) not in PAREDES:
        	acciones.append(('Arriba', (x,y+1)))
        if y > 0 and (x,y-1) not in PAREDES:
        	acciones.append(('Abajo', (x,y-1)))
        
        return acciones

    def result(self, state, action):
        robot, comidas = state
        x, y = action[1]
        com = list(comidas)
        if (x,y) in comidas:
            # Comio
            com.remove((x,y))

        return ((x,y), tuple(com))

    def cost(self, state1, action, state2):
        return 1

    def heuristic(self, state):
        robot, comidas = state
        x, y = robot
        a, b = FINAL
        z = max([abs(x-a), abs(y-b)])

        return len(comidas) + z

problema = Problema(ESTADO)
visor = BaseViewer()
respuesta = astar(problema, graph_search=True, viewer=visor)
for a in respuesta.path():
    print a