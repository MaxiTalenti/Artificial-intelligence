# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer
import random

# Se tiene una red de computadoras conectadas, y se desea determinar el mejor camino dentro de la red para enviar un archivo desde la computadora 15,
# hacia la computadora 9. Se posee información respecto al tiempo que demora el archivo en pasar entre las diferentes máquinas conectadas entre sí
# (lineas rojas y azules con sus números), y además se conocen las coordenadas físicas de cada computadora dentro del edificio 
# (tuplas verdes para cada computadora).
# En la mayoría de los casos se ha observado cierta relación entre la velocidad de transferencia entre dos computadoras y la
# distancia a la que se encuentran físicamente entre sí, salvo por algunas conexiones de baja calidad.
# Las computadoras conectadas entre sí, con sus tiempos de transferencia y sus posiciones son las siguientes:

## Compu:(col,fila)
mapa = {1: (37, 26), 2: (25, 12), 3: (41, 16), 4: (55, 28), 6: (68, 31),
    7: (59, 51), 8: (63, 21), 9: (66, 5), 10: (54, 6), 11: (46, 2), 12: (32, 2),
    13: (6, 3), 14: (4, 14), 15: (15, 19), 16: (15, 39), 17: (20, 53),
    18: (25, 43), 19: (13, 10), 20: (25, 43)}

## Compu:[(Destino,Tiempo)]
movs = {1: [(2, 25), (3, 10), (4, 20), (20, 30)],
        2: [(1, 25), (19, 10)],
        3: [(1, 10), (10, 25), (12, 25)],
        4: [(1, 20), (8, 10), (6, 15), (7, 35)],
        6: [(4, 15)],
        7: [(4, 35), (17, 80)],
        8: [(4, 10), (9, 55)],
        9: [(8, 55), (10, 10)],
        10: [(9, 10), (11, 10), (3, 25)],
        11: [(10, 10), (12, 40)],
        12: [(3, 25), (11, 40), (19, 60)],
        13: [(19, 10)],
        14: [(19, 10)],
        15: [(19, 10), (16, 65)],
        16: [(15, 65), (20, 10)],
        17: [(20, 10), (7, 80)],
        18: [(20, 5)],
        19: [(2, 10), (13, 10), (14, 10), (15, 10), (12, 60)],
        20: [(16, 10), (17, 10), (18, 5), (1, 30)]}

INITIAL = 15
GOAL = 9

class HnefataflProblema(SearchProblem):

	def is_goal(self, state):
		return state == GOAL

	def actions(self, state):
		return movs[state]

	def result(self, state, actions):
		return actions[0]

	def cost(self, state1, action, state2):
		return action[1]

	def heuristic(self, state):
		xcompu, ycompu = mapa[state]
		xfinal, yfinal = mapa[GOAL]
		return sum([abs(xcompu-xfinal), abs(ycompu-yfinal)])

problema = HnefataflProblema(INITIAL)
visor = BaseViewer()
resultado = astar(problema, graph_search=True, viewer=visor)
for a in resultado.path():
	print a
print resultado
