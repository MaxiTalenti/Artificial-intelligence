# coding=utf-8

from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer

# Se desea desarrollar una aplicación que controle un brazo robótico encargado de mover piezas entre 2 máquinas,
# de una fábrica. Cada vez que la máquina forjadora termina un lote de piezas, el robot debe mover todas las
# piezas forjadas hacia la maquina templadora. El robot posee un sensor que le permite conocer la posicion de 
# todas las piezas en un espacio de grilla, como el mostrado en la figura con la salvedad de que puede haber
# distinta cantidad de filas, y puede ejecutar movimientos directos desde cualquier posición a cualquier otra
# posición de la grilla. Agarrar y soltar objetos son también acciones disponibles, diferentes de los movimientos
# entre posiciones, y solo es posible tener una pieza agarrada al mismo tiempo. Lo que se desea lograr, es pasar 
# todas las piezas de una máquina a otra en la menor cantidad posible de movimientos, teniendo como consideración
# especial que los movimientos entre casillas se cuentan como la cantidad de casilleros que se atraviesan.
# Por ejemplo, si bien se puede en una acción moverse desde la casilla superior izquierda a la casilla inferior
# derecha, esa acción se considera como 4 movimientos.

# 2 |   | X |   |
# 1 |   | X |   |
# 0 |   | R |   |
#     0   1   2
#     For    Temp

#           Elem en Forjadora, si esta o no       |  Elem en Templadora, si esta o no      | Elemento en mano    | Ubicacion de la mano
ESTADO = (((0,0, True), (0,1, True), (0,2, True)), ((2,0,False), (2,1,False), (2,2,False)),         (),                    (1,0))

class Problema(SearchProblem):

    def is_goal(self, state):
        forj, templ, enmano, ubic = state
        for a in forj:
            x,y,esta = a
            if esta == True:
                return False
        return len(enmano) == 0

    def actions(self, state):
        forj, templ, enmano, ubic = state
        acciones = []
        for a in forj:
            x, y, z = a
            if len(enmano) == 0:
                if (x,y) != ubic and z == True:
                   acciones.append(('Mover', (x,y)))
                elif (x,y) == ubic and z == True:
                    acciones.append(('Agarrar', (x,y)))
        if len(enmano) != 0:
            for b in templ:
                r, t, y = b
                if (r,t) == ubic and y == False:
                    acciones.append(('Soltar', (r,t)))
                elif (r,t) != ubic and y == False:
                    acciones.append(('Mover', (r,t)))

        return acciones

    def result(self, state, action):
        forj, templ, enmano, ubic = state
        act, mov = action
        x, y = ubic
        lforj = list(forj)
        ltempl = list(templ)
        if act == 'Mover':
            x, y = mov
        if act == 'Agarrar':
            enmano = (ubic)
            lforj.remove((x, y, True))
            lforj.append((x,y, False))
        if act == 'Soltar':
            enmano = ()
            ltempl.remove((x,y, False))
            ltempl.append((x,y, True))
        
        return tuple(lforj), tuple(ltempl), enmano, (x,y) 

    def cost(self, state1, action, state2):
        forj, templ, enmano, ubic = state1
        act, mov = action
        x, y = ubic
        xx, yy = mov
        if act == 'Mover':
            return sum([abs(x-xx), abs(y-yy)])
        else:
            return 1

    def heuristic(self, state):
        forj, templ, enmano, ubic = state
        cantidad = 0
        estaenforj = False
        for a in forj:
            xforj, yforj, esta = a
            if esta == True:
                cantidad = cantidad + 4
            if ubic == a:
                estaenforj = True
        if len(enmano) == 0 and estaenforj == True:
            return cantidad - 1
        elif len(enmano) == 0 and estaenforj == False:
            return cantidad
        elif len(enmano) != 0 and estaenforj == True:
            return cantidad + 2
        elif len(enmano) != 0 and estaenforj == False:
            return cantidad + 1
                
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