# coding=utf-8

# Supongamos que tenemos un tablero rectangular dividido en cuadrados, cuyo tamaño es 3 cuadrados de largo por 4 de ancho.
# Inicialmente, todos los cuadrados están pintados de blanco
# 2 | X |   |   |   | 
# 1 |   |   |   |   | 
# 0 |   |   |   |   |
#	  0   1   2   3
 	 	 	 
# El objetivo es pintar todos los cuadrados de rojo. 
# Para ello, disponemos de un robot que es capaz de pintar cuadrados individuales de rojo, con las siguientes restricciones:
# # - El robot se mueve por el tablero de cuadrado en cuadrado, con movimientos simples iguales a los del caballo en el ajedrez.
# # - El robot nunca se puede situar sobre un cuadrado pintado de rojo.
# # - Una vez que ha realizado el movimiento, el robot se coloca sobre el cuadrado correspondiente (que ha de estar pintado de blanco) 
# # y lo pinta de color rojo. 
# - Inicialmente, el robot se encuentra sobre el cuadrado de la esquina superior izquierda, que ya está pintado de rojo.

from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer

ESTADO = (0,2), ((0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,1),(3,2))

class Problema(SearchProblem):

	def is_goal(self, state):
		posicion, sinpintar = state
		return len(sinpintar) == 0

	def actions(self, state):
		posicion, sinpintar = state
		x, y = posicion
		acciones = []
		if (x+2,y+1) in sinpintar:
			acciones.append(('Mov1', (x+2,y+1)))
		if (x+2,y-1) in sinpintar:
			acciones.append(('Mov2', (x+2,y-1)))
		if (x-2,y+1) in sinpintar:
			acciones.append(('Mov3', (x-2,y+1)))
		if (x-2,y-1) in sinpintar:
			acciones.append(('Mov4', (x-2,y-1)))
		if (x+1,y-2) in sinpintar:
			acciones.append(('Mov5', (x+1, y-2)))
		if (x+1,y+2) in sinpintar:
			acciones.append(('Mov6', (x+1, y+2)))
		if (x-1,y-2) in sinpintar:
			acciones.append(('Mov7', (x-1,y-2)))
		if (x-1,y+2) in sinpintar:
			acciones.append(('Mov8', (x-1,y+2)))

		return acciones

	def result(self, state, action):
		posicion, sinpintar = state
		sin_pintar = list(sinpintar)
		# modificas sin_pintar, ya que ahora es una lista
		sin_pintar.remove((action[1]))
		nuevo_state = posicion, tuple(sin_pintar)
		xnuevo, ynuevo  = action[1]
		return ((xnuevo, ynuevo), tuple(sin_pintar))

	def cost(self, state1, action, state2):
		return 1

	def heuristic(self, state):
		posicion, sinpintar = state
		return len(sinpintar)

problema = Problema(ESTADO)
visor = BaseViewer()
respuesta = astar(problema, graph_search=True, viewer=visor)
for a in respuesta.path():
	print a