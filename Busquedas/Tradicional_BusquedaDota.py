# coding=utf-8

# Esta es una versión muy simplificada del juego Dota. 
# En esta versión, el mapa es un tablero de 3x3, participa un solo jugador, 
# y tiene como objetivos derrotar a un héroe enemigo y destruir su base en la menor cantidad de acciones posibles. 
# El jugador comienza en la esquina inferior izquierda del mapa, 
# y en cada turno puede moverse a los casilleros limítrofes (no en diagonal). 
# Si se encuentra adyacente a un casillero de un enemigo o edificio, también tiene disponible la acción de atacar a dicho objeto, 
# destruyéndolo como resultado. Dos objetos no pueden estar en la misma posición.
# Al inicio del juego, el mapa y la distribución de objetos es la siguiente:

# 2  |   |    | Be |
# 1  |   | He |    |	 
# 0  | H |    |    |  	 
#      0    1    2
# H = Héroe (jugador), He = Héroe enemigo, Be = Base enemiga
	 	 
# En este estado, el héroe está junto al héroe enemigo. 
# En esta situación puede moverse en dos direcciones o atacar a He. 
# Si ataca, en el estado resultante el héroe enemigo estaría muerto.


from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer

# Posicion columna, posicion fila
# Lugar H, lugares ocupados, lugares libres.
ESTADO = (0,0), ((1,1), (2,2)), ((0,1), (0,2), (1,0), (1,2), (2,0), (2,1))

class Problema(SearchProblem):
    def is_goal(self, state):
        h, ocupados, libres = state
        return len(ocupados) == 0

    def actions(self, state):
        h, ocupados, libres = state
        x, y = h
        acciones = []
        if (x+1,y) in libres:
            acciones.append(('MoverLibre1', (x+1,y)))
        if (x-1,y) in libres:
            acciones.append(('MoverLibre2', (x-1,y)))
        if (x,y-1) in libres:
            acciones.append(('MoverLibre3', (x,y-1)))
        if (x,y+1) in libres:
            acciones.append(('MoverLibre2', (x,y+1)))
        if (x+1,y+1) in ocupados:
            acciones.append(('Matar1', (x+1,y+1)))
        if (x-1,y-1) in ocupados:
            acciones.append(('Matar2', (x-1,y-1)))
        if (x+1,y-1) in ocupados:
            acciones.append(('Matar3', (x+1,y-1)))
        if (x-1,y+1) in ocupados:
            acciones.append(('Matar4', (x-1,y+1)))

        return acciones

    def result(self, state, action):
        h, ocupados, libres = state
        x, y = h
        act = action[1]
        oc = list(ocupados)
        lib = list(libres)

        if act in ocupados:
            oc.remove((act))
            lib.append((act))
        if act in libres:
            lib.remove((act))
            lib.append((h))
            x, y = act

        return ((x,y), tuple(oc), tuple(lib))

    def cost(self, state1, action, state2):
        return 1

    def heuristic(self, state):
        h, ocupados, libres = state
        return len(ocupados)
                

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
    print resultado.state
    for a in resultado.path():
        print 'parte', a
    return resultado

resolver(metodo_busqueda='astar', posicion_rey=ESTADO, controlar_estados_repetidos=True)