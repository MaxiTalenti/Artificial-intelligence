# Supongamos que tenemos un tablero rectangular dividido en cuadrados, cuyo tamaño es 3 cuadrados de largo por 4 de ancho.
#  Inicialmente, todos los cuadrados están pintados de blanco
# | X |   |   |   |	 
# |   |   |   |   |	 
# |   |   |   |   |	 
 	 	 	 
# El objetivo es pintar todos los cuadrados de rojo. 
# Para ello, disponemos de un robot que es capaz de pintar cuadrados individuales de rojo, con las siguientes restricciones:
# # - El robot se mueve por el tablero de cuadrado en cuadrado, con movimientos simples iguales a los del caballo en el ajedrez.
# # - El robot nunca se puede situar sobre un cuadrado pintado de rojo.
# # - Una vez que ha realizado el movimiento, el robot se coloca sobre el cuadrado correspondiente (que ha de estar pintado de blanco) 
# # y lo pinta de color rojo. 
# - Inicialmente, el robot se encuentra sobre el cuadrado de la esquina superior izquierda, que ya está pintado de rojo.

# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer
import random

ESTADO = [(0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (2,3)]

class Problema(SearchProblem):

    def is_goal(self, state):
        return len(state) == 1

    def result(self, state, actions):

    def actions(self, state):

    def cost(self, state1, action, state2):
        return 1

    def heuristic(self, state):
        return len(state)


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
	print(visor.stats)
	return resultado

resolver(metodo_busqueda='astar', posicion_rey=ESTADO, controlar_estados_repetidos=True)