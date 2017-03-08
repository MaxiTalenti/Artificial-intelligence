# coding=utf-8

# Se tienen N jarros enumerados de 1 a N, donde la capacidad en litros del jarro I es I.
# Esto es, el jarro 1 tiene capacidad de 1 litro, el jarro 2, 2 litros y así sucesivamente. 
# Inicialmente el jarro N está lleno de agua y los demás están vacíos.
# El objetivo es que todos los jarros queden con 1 litro de agua, 
# teniendo como operaciones permitidas trasvasar el contenido de un jarro a otro, 
# operación que finaliza al llenarse el jarro de destino o vaciarse el jarro de origen.
#  Todo esto se tiene que lograr con el menor costo posible, siendo I el costo de trasvasar el contenido del jarro I a otro jarro.
# Resolver.
## Teniendo en cuenta el caso donde son 4 jarros:
## Resuelva mediante búsqueda A* considerando la heurística planteada en b.

from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer

# Numero de jarro y listros contenidos
ESTADO = ((1,0), (2,0), (3,0), (4,4))

class Problema(SearchProblem):

    def is_goal(self, state):
        for a in state:
            jarro, litro = a
            if litro != 1:
                return False
        return True

    def actions(self, state):
        acciones = []
        for a in state:
            jarro, litro = a
            if jarro != litro: # Si le falta llenarse
                for b in state:
                    jarro2, litro2 = b
                    if (jarro != jarro2 and litro2 != 0):
                        # Origen, destino
                        acciones.append(('Llenar', ((jarro2,litro2),(jarro,litro))))

        return acciones

    def result(self, state, action):
        origen, destino = action[1]
        statel = list(state)
        statel.remove((origen))
        statel.remove((destino))
        if (destino[0] -destino[1]) >= origen[1]:
            # Vacia el origen.
            statel.append((origen[0], 0))
            statel.append((destino[0], destino[1]+origen[1]))
        else:
            # LLena el destino
            statel.append((destino[0], destino[0]))
            statel.append((origen[0], origen[1]-(destino[0]-destino[1])))

        return tuple(statel)

    def cost(self, state1, action, state2):
        return action[1][0][0]

    def heuristic(self, state):
        cantidad = 0
        for a in state:
            jarro, litro = a
            if jarro != litro:
                cantidad = cantidad+1
        return cantidad

def resolver(metodo_busqueda,posicion_rey,controlar_estados_repetidos):
	problema = Problema(posicion_rey)
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
	print(resultado.state)
	for a in resultado.path():
		print 'parte', a
	return resultado

resolver(metodo_busqueda='breadth_first', posicion_rey=ESTADO, controlar_estados_repetidos=True)