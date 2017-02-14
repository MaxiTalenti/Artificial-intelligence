# coding=utf-8
# Un grupo de 5 personas quiere cruzar un viejo y estrecho puente. 
# Es una noche cerrada y se necesita llevar una linterna para cruzar. 
# El grupo sólo dispone de una linterna, a la que le quedan 5 minutos de batería. 
# Cada persona tarda en cruzar 10, 30, 60, 80 y 120 segundos, respectivamente. 
# El puente sólo resiste un máximo de 2 personas cruzando a la vez, 
# y cuando cruzan dos personas juntas caminan a la velocidad del más lento. 
# No se puede lanzar la linterna de un extremo a otro del puente, así que cada vez que crucen dos personas, 
# alguien tiene que volver a cruzar hacia atrás con la linterna a buscar a los compañeros que faltan, 
# y así hasta que hayan cruzado todos.

from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer

VALORES = {1: 10, 2: 30, 3: 60, 4: 80, 5: 120}
ESTADO = ('A', #Linterna
		  (1,2,3,4,5), # Personas en A
		  ()) # Personas en B

class Problema(SearchProblem):

    def is_goal(self, state):
    	linterna, a, b = state
    	return len(a) == 0 and len(b) == 5

    def actions(self, state):
    	linterna, a, b = state
    	acciones = []
    	if linterna == 'A':
    		for x in a:
    			for y in a:
    				if x != y:
    					acciones.append(('Mover', (x,y)))
    	else:
    		for x in b:
    			acciones.append(('Volver', x))

    	return acciones

    def result(self, state, action):
    	linterna, a, b = state
    	mov, z = action
    	alist = list(a)
    	blist = list(b)
    	if mov == 'Mover':
    		x, y = z
    		alist.remove((x))
    		alist.remove((y))
    		blist.append((x))
    		blist.append((y))
    		linterna = 'B'
    	else:
    		alist.append((z))
    		blist.remove((z))
    		linterna = 'A'

    	return linterna, tuple(alist), tuple(blist)

	def cost(self, state1, action, state2):
		mov, a = action
        if mov == 'Mover':
        	x,y = a
        	return max(VALORES[x], VALORES[y])
        else:
        	return VALORES[a]

    def heuristic(self, state):
    	linterna, a, b = state
    	sincruzar = len(a)
    	if linterna == 'A':
    		return sincruzar + (sincruzar -1)
    	else:
    		if sincruzar == 0:
    			return 0
    		else:
    			return sincruzar * 2

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
		print 'Step', a
	return resultado

resolver(metodo_busqueda='astar', posicion_rey=ESTADO, controlar_estados_repetidos=True)