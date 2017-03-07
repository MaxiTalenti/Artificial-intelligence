# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer
import random

# Hace mucho tiempo un granjero fue al mercado y compró un tigre, una cabra y una lechuga.
# Para volver a su casa tenía que cruzar un río. El granjero dispone de una barca para cruzar a la otra orilla, pero en la barca solo caben él
# y una de sus compras. Si el tigre se queda solo con la cabra, se la come. Si la cabra se queda sola con la lechuga, se la come.
# El objetivo es lograr que el granjero cruce el río y logre tener sus compras con él, dejando cada compra intacta.

INITIAL = ('T','C','L'), ('Mercado')

class HnefataflProblema(SearchProblem):

	def is_goal(self, state):
		return len(state[0]) == 0

	def actions(self, state):
		objetos, lugar = state
		accciones = []
		if lugar == 'Mercado': # Si el tigre se queda solo con la cabra, se la come. Si la cabra se queda sola con la lechuga, se la come.
			if len(objetos) == 3:
				accciones.append(('C'))
			elif len(objetos) == 1:
				accciones.append((objetos[0]))
			else:
				accciones.append(('T'))
				accciones.append(('L'))
		else:
			accciones.append(('Volver'))
		return accciones

	def result(self, state, actions):
		objetos, lugar = state
		if actions == 'Volver':
			return objetos, 'Mercado'
		else:
			obj = list(objetos)
			obj.remove((actions))
			return tuple(obj), 'Casa'

	def cost(self, state1, action, state2):
		return 1

	def heuristic(self, state):
		return len(state[0]) + 1


problema = HnefataflProblema(INITIAL)
visor = BaseViewer()
resultado = astar(problema, graph_search=True, viewer=visor)
for a in resultado.path():
	print a
print resultado
