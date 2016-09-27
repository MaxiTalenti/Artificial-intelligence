# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer
import random

INITIAL = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),
			(1,9),(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(4,0)]

class problema(SearchProblem):
	def generate_random_state(self):
		Tuplas = []
		while len(Tuplas) < 30:
			TuplaAComprobar = (random.randint(0,9),random.randint(0,9))
			if TuplaAComprobar not in INITIAL:
				Tuplas.append(TuplaAComprobar)
		return Tuplas

#	def actions(self, state):
# 		#Returns a string representation of an action.
#         #By default it returns str(action).
        
#         #return str(action)

# 	def result(self):
# 		 '''Returns the resulting state of applying `action` to `state`.'''
		
	def value(self, state):
		CamposVacios = []
		for x in xrange(0, 10): # Obtiene una lista de tuplas con todos los campos vacios.
			for y in xrange(0,10):
				if (x,y) not in state:
					CamposVacios.append((x,y))
		PuntosTotal = 0
		for x in CamposVacios:
			Puntos = 0
			z, y = x
			if z > 0: #Arriba
				if (z - 1, y) in state:
					Puntos = 1
			if z < 9: #Abajo
				if (z + 1 , y) in state:
					Puntos = Puntos + 1
			if y > 0: #Izquierda
				if (z , y - 1) in state:
					Puntos = Puntos + 1
			if y < 9: #Derecha
				if (z ,y + 1) in state:
					Puntos = Puntos + 1
			if Puntos > 1:
				if z == 0 or y == 0 or z == 9 or y == 9:
					PuntosTotal = PuntosTotal + 3
				else:
					PuntosTotal = PuntosTotal + 1
		return PuntosTotal


# def resolver(metodo_busqueda, iteraciones, haz, reinicios):
# 	print('A')

a = problema(INITIAL)
print(a.value(INITIAL))