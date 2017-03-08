# coding=utf-8
from simpleai.search import SearchProblem, hill_climbing, hill_climbing_random_restarts, beam, hill_climbing_stochastic, simulated_annealing
from simpleai.search.viewers import ConsoleViewer, BaseViewer
from datetime import datetime
import random

INITIAL = [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),
			(1,9),(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(2,9)]

apuntos = []

def sumarValue(value):
    apuntos.append(value)

def grabar(busqueda, valor):
	archi=open('entrega_1_local.txt','a')
	archi.write('{}:{}\n'.format(busqueda, valor))
	archi.close()
	apuntos[:] = []

class HnefataflProblem(SearchProblem):
	def generate_random_state(self):
		Tuplas = []
		while len(Tuplas) < 30:
			TuplaAComprobar = (random.randint(0,9),random.randint(0,9))
			if TuplaAComprobar not in Tuplas:
				Tuplas.append(TuplaAComprobar)
		return Tuplas

	def actions(self, state):	
		Acciones = []
		for i in state:
			fila,col = i
			if fila > 0: 
			#Arriba
				if (fila - 1, col) not in state:
					Acciones.append([(fila,col),(fila - 1, col)]) # Primero posicion luego posible movimiento
			if fila < 9:
			#Abajo
				if (fila + 1 , col) not in state:
					Acciones.append([(fila,col),(fila + 1, col)])
			if col > 0:
				#Derecha
				if (fila , col - 1) not in state:
					Acciones.append([(fila,col),(fila, col  - 1)])
			if col < 9:
				## Izquierda
				if (fila ,col + 1) not in state:
					Acciones.append([(fila,col),(fila, col + 1)])
		return Acciones

	def result(self,state,action): #[(2, 8), (8, 6)]
		[(a,b),(c,d)] = action
		statenuevo = state[:]
		statenuevo.remove((a,b))
		statenuevo.append((c,d))
		return statenuevo
# 		 '''Returns the resulting state of applying `action` to `state`.'''
		
	def value(self, state):
		CamposVacios = []
		PuntosTotal = 0
		for x in range(10): # Obtiene una lista de tuplas con todos los campos vacios.
			for y in range(10):
				if (x,y) not in state:
					CamposVacios.append((x,y))
		for x in CamposVacios: # Verifica por cada campo vacio si tiene peones en arriba, abajo, izq o derecha
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
				if z in (0,9) or y in (0,9):
					PuntosTotal = PuntosTotal + 3
				else:
					PuntosTotal = PuntosTotal + 1
		sumarValue(PuntosTotal)
		return PuntosTotal

def resolver(metodo_busqueda,iteraciones,haz,reinicios):
	print '··· Se van a ejecutar las 10 iteraciones para la busqueda {} ···'.format(metodo_busqueda)
	#print 'Haz:', haz
	#print 'Reinicios:', reinicios
	prob = HnefataflProblem(INITIAL)
	visor = BaseViewer()
	if (metodo_busqueda == 'hill_climbing'): # Ascenso de colina
		for x in range(10):
			print 'Ejecutando Iteracion {} ...'.format(x)
			inicio = datetime.now()
			resultado = hill_climbing(problem = prob, iterations_limit = iteraciones)
			fin = datetime.now()
			print 'Tiempo de iteracion {} : {} segundos.'.format(x, (fin - inicio).total_seconds())
		grabar('1', max(apuntos))
	elif (metodo_busqueda == 'hill_climbing_stochastic'): # Ascenso de colina, variante estocástica
		for x in range(10):
			print 'Ejecutando Iteracion {} ...'.format(x)
			inicio = datetime.now()
			resultado = hill_climbing_stochastic(problem = prob, iterations_limit = iteraciones)
			fin = datetime.now()
			print 'Tiempo de iteracion {} : {} segundos.'.format(x, (fin - inicio).total_seconds())
		grabar('2', max(apuntos))
	elif (metodo_busqueda == 'beam'): # Haz local
		for x in range(10):
			print 'Ejecutando Iteracion {} ...'.format(x)
			inicio = datetime.now()
			resultado = beam(problem = HnefataflProblem(None), iterations_limit = iteraciones, beam_size = haz)
			fin = datetime.now()
			print 'Tiempo de iteracion {} : {} segundos.'.format(x, (fin - inicio).total_seconds())
		grabar('3', max(apuntos))
	elif (metodo_busqueda == 'hill_climbing_random_restarts'): # Ascenso de colina con reinicios aleatorios
		for x in range(10):
			print 'Ejecutando Iteracion {} ...'.format(x)
			inicio = datetime.now()
			resultado = hill_climbing_random_restarts(problem = HnefataflProblem(None), iterations_limit = iteraciones, restarts_limit = reinicios)
			fin = datetime.now()
			print 'Tiempo de iteracion {} : {} segundos.'.format(x, (fin - inicio).total_seconds())
		grabar('4', max(apuntos))
	elif (metodo_busqueda == 'simulated_annealing'): # Temple simulado
		for x in range(10):
			print 'Ejecutando Iteracion {} ...'.format(x)
			inicio = datetime.now()
			resultado = simulated_annealing(problem = prob, iterations_limit = iteraciones)
			fin = datetime.now()
			print 'Tiempo de iteracion {} : {} segundos.'.format(x, (fin - inicio).total_seconds())
		grabar('5', max(apuntos))
	return resultado

if __name__ == '__main__': # Se ejecuta esto si no se llama desde consola
	a = HnefataflProblem(INITIAL)
	print 'ACTIONS'
	print a.actions(INITIAL)
	print '############ RESOLVIENDO ###########'
	resolver('hill_climbing',50,None,None)
	#resolver('hill_climbing_stochastic', 50,None,None)
    #resolver('beam', 50,5,None)
    #resolver('hill_climbing_random_restarts', 50,None,5)
    #resolver('simulated_annealing',50,None,None)

if __name__ != '__main__':
		archi=open('entrega_1_local.txt','w') # Va a generar el archivo de nuevo pisandolo si ya existe.
