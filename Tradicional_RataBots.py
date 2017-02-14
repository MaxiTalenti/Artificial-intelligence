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

ESTADO = ((5,2), # Robot
         ((0,2), (1,1), (1,4), (2,3), (3,0), (3,1), (3,4), (3,5), (4,3), (5,1), (5,5)), # Paredes
         ((0,1), (2,4), (4,2)), # Comidas
         ((0,0), (0,3), (0,4), (0,5), (1,0), (1,2), (1,3), (1,5), (2,0), (2,1), (2,2), (2,5), (3,2), (3,3),
         (4,0), (4,1), (4,4), (4,5), (5,0), (5,3), (5,4))) # Espacios libres

class Problema(SearchProblem):

    def is_goal(self, state):
        robot, paredes, comidas, esplibres = state
        if len(comidas) == 0:
            print 'comidas vacias', robot, comidas
        return (robot == FINAL and len(comidas) == 0)

    def actions(self, state):
        robot, paredes, comidas, esplibres = state
        x, y = robot
        acciones = []
        if ((x+1,y) in esplibres) or ((x+1,y) in comidas):
            acciones.append(('Derecha', (x+1,y)))
        if ((x-1,y) in esplibres) or ((x-1,y) in comidas):
            acciones.append(('Izquierda', (x-1,y)))
        if ((x,y-1) in esplibres) or ((x,y-1) in comidas):
            acciones.append(('Abajo', (x,y-1)))
        if ((x,y+1) in esplibres) or ((x,y+1) in comidas):
            acciones.append(('Arriba', (x,y+1)))
        
        return acciones

    def result(self, state, action):
        robot, paredes, comidas, espacioslibres = state
        x, y = action[1]
        com = list(comidas)
        espl = list(espacioslibres)
        if (x,y) in comidas:
            # Comio
            com.remove((x,y))
        else:
            # Movio
            espl.remove((x,y))
        espl.append((x,y))

        return ((x,y), paredes, tuple(com), tuple(espl))

    def cost(self, state1, action, state2):
        return 1

    def heuristic(self, state):
        robot, paredes, comidas, espacioslibres = state
        return len(comidas) +1

def resolver(metodo_busqueda,posicion_rey,controlar_estados_repetidos):
	problema = Problema(posicion_rey)
	visor = ConsoleViewer()
	#Busquedas, Grafo -> graph_search=True
	if (metodo_busqueda == 'breadth_first'): # En amplitud
		resultado = breadth_first(problema, graph_search=controlar_estados_repetidos, viewer=visor)
	elif (metodo_busqueda == 'depth_first'): # Profundidad
		resultado = depth_first(problema, graph_search=controlar_estados_repetidos, viewer=visor)
	elif (metodo_busqueda == 'greedy'): # Avara
		resultado = greedy(problema, graph_search=controlar_estados_repetidos, viewer=visor)
	elif (metodo_busqueda == 'astar'): # Estrella
		resultado = astar(problema, graph_search=controlar_estados_repetidos, viewer=visor)
	print(resultado.state)
	for a in resultado.path():
		print 'Step', a
	return resultado

resolver(metodo_busqueda='astar', posicion_rey=ESTADO, controlar_estados_repetidos=True)