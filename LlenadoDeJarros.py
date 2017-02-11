# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer
import random

# Se tienen N jarros enumerados de 1 a N, donde la capacidad en litros del jarro I es I.
# es, el jarro 1 tiene capacidad de 1 litro, el jarro 2, 2 litros y así sucesivamente.
# Inicialmente el jarro N está lleno de agua y los demás están vacíos.
# El objetivo es que todos los jarros queden con 1 litro de agua, teniendo como operaciones permitidas
# trasvasar el contenido de un jarro a otro, operación que finaliza al llenarse el jarro de destino
# o vaciarse el jarro de origen. Todo esto se tiene que lograr con el menor costo posible, siendo I el costo de trasvasar
# el contenido del jarro I a otro jarro.

INITIAL = ((1,0),(2,0),(3,0),(4,0),(5,5))
FINAL = ((1,1),(2,1),(3,1),(4,1),(5,1))

class HnefataflProblema(SearchProblem):
    def is_goal(self, state):
        return state == FINAL

    def actions(self, state):
        acciones = []
        for jarro_origen, litros_origen in state:
            for jarro_destino, litros_destino in state:
                if jarro_origen != jarro_destino:
                    if litros_origen > 0: # Verifica si el jarro de origen no esta vacio
                        if jarro_destino > litros_destino:
                            acciones.append((jarro_origen, jarro_destino))
        return acciones

    def result(self, state, actions):
        jarro_origen, jarro_destino = actions
        jarro, litros_origen = state[jarro_origen - 1]
        jarro2, litros_destino = state[jarro_destino -1]

        if litros_origen < (jarro_destino - litros_destino):
            litros_origen = 0
            litros_destino = litros_destino + litros_origen
        else:
            litros_origen = litros_origen - (jarro_destino - litros_destino)
            litros_destino = jarro_destino

        estadoo = list(state[:]) # Lo paso a [(),()] para modificarlo
        estadoo[jarro_origen -1] = (jarro_origen, litros_origen)
        estadoo[jarro_destino -1] = (jarro_destino, litros_destino)
        return (estadoo[0], estadoo[1], estadoo[2], estadoo[3], estadoo[4])

    def cost(self, state1, action, state2):
        return 1

    def heuristic(self, state):
        return len(state) -1

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

print '--- Busqueda estrella ---'
result = astar(HnefataflProblema(INITIAL), graph_search=True, viewer=BaseViewer())
for action, state in result.path():
    if action is not None:
        print 'Volcar del {} al {}'.format(action[0], action[1])
    else:
        print 'Accion: Ninguna'
    print 'Resultado', state
print '--- Busqueda en amplitud ---'
result = breadth_first(HnefataflProblema(INITIAL), graph_search=True, viewer=BaseViewer())
for action, state in result.path():
    if action is not None:
        print 'Volcar del {} al {}'.format(action[0], action[1])
    else:
        print 'Accion: Ninguna'
    print 'Resultado', state
print '--- Busqueda en profundidad ---'
result = depth_first(HnefataflProblema(INITIAL), graph_search=True, viewer=BaseViewer())
for action, state in result.path():
    if action is not None:
        print 'Volcar del {} al {}'.format(action[0], action[1])
    else:
        print 'Accion: Ninguna'
    print 'Resultado', state
print '--- Busqueda Avara ---'
result = greedy(HnefataflProblema(INITIAL), graph_search=True, viewer=BaseViewer())
for action, state in result.path():
    if action is not None:
        print 'Volcar del {} al {}'.format(action[0], action[1])
    else:
        print 'Accion: Ninguna'
    print 'Resultado', state
