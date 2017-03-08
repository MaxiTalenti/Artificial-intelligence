# coding=utf-8

# Se necesita programar la lógica para un autoelevador (“zamping”) robótico, 
# cuya tarea consiste en recolectar y llevar hacia un punto de entrega único, 
# una determinada cantidad de pallets que le son pedidos.
# El robot conoce la ubicación de los pallets dentro del almacén, 
# que se encuentran siempre en el suelo (no hay estanterías ni pallets apilados), 
# conoce su propia ubicación, la ubicación del punto de entrega (fijo), 
# y recibe como orden una lista de números de pallets a recolectar.
# Podemos pensar al almacén como una grilla para modelar los movimientos del robot como discretos. 
# Y de la misma manera, podemos considerar el “agarrar” un pallet, y “dejar” un pallet, 
# como movimientos atómicos, sin necesidad de conocer el detalle de cómo se efectúan dichas tareas. 
# Para agarrar un pallet, el robot debe estar en la posición del pallet, y para dejarlo, debe encontrarse en el punto de entrega.
# El aspecto que se desea optimizar es la cantidad de movimientos que el robot realiza para llevar todos los pallets pedidos,
# al punto de entrega. 
# Y para realizar el ejemplo de árbol de búsqueda utilizaremos el almacén de ejemplo diagramado a la derecha.
## Resolver:
## Teniendo en cuenta el diagrama de almacén, y como orden “entregar los pallets 8, 3 y 9”, 
## resuelva mediante búsqueda A* considerando la heurística planteada en b (solo las primeras 5 iteraciones).

# 4 |   | 1  | 5 |  | 9 |
# 3 | 2 | 10 |   |  | R | <-- Robot
# 2 | 4 |    | 8 |  | E | <-- Entrega
# 1 | 3 |    |   |  |   |
# 0 | 6 | 7  |   |  |   |
#     0    1   2   3  4

from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer

ENTREGA = (4,2)
PALLETS = {1: (1,4), 2: (0,3), 3: (0,1), 4: (0,2), 5: (2,4), 6: (0,0), 7: (1,0), 8: (2,2), 9: (4,4), 10: (1,3)}
LIBRES = ((0,4), (1,1), (1,2), (2,0), (2,1), (2,3), (3,0), (3,1), (3,2), (3,3), (3,4), (4,0), (4,1), (4,2))
ESTADO = ((4,3), # Robot
         (8,3,9), # A entregar
         ()) # Palet en mano

class Problema(SearchProblem):

    def is_goal(self, state):
        robot, aentregar, enmano = state
        return sum([len(aentregar), len(enmano)]) == 0

    def actions(self, state):
        robot, aentregar, enmano = state
        x, y = robot
        acciones = []
        if x > 0:
            acciones.append(('Izquierda', (x-1, y)))
        if x < 4:
            acciones.append(('Derecha', (x+1, y)))
        if y > 0:
            acciones.append(('Abajo', (x, y-1)))
        if y < 4:
            acciones.append(('Arriba', (x,y+1)))

        if len(enmano) == 0:
            # Tiene que buscar para recojer.
            for a in aentregar:
                xpal, ypal = PALLETS[a]
                if (xpal,ypal) == (x,y):
                    acciones.append(('Agarrar', a))
        else:
            if (x,y) == ENTREGA:
                acciones.append(('Dejar', None))

        return acciones

    def result(self, state, action):
        robot, aentregar, enmano = state
        x, y = robot
        laentregar = list(aentregar)
        lenmano = list(enmano)

        if action[0] == 'Agarrar':
            laentregar.remove((action[1]))
            lenmano.append((action[1]))
        elif action[0] == 'Dejar':
            lenmano = []
        else:
            x, y = action[1]
        
        return (x,y), tuple(laentregar), tuple(lenmano)

    def cost(self, state1, action, state2):
        return 1

    def heuristic(self, state):
        robot, aentregar, enmano = state
        x, y = robot
        xx, yy = ENTREGA
        dif = (abs(x-xx), abs(y-yy))
        return sum([len(aentregar), len(enmano), max(dif)])

problema = Problema(ESTADO)
visor = BaseViewer()
respuesta = astar(problema, graph_search=True, viewer=visor)
for a in respuesta.path():
    print a