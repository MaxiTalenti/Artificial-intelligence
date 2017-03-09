# coding=utf-8

from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer

# Se pretende encontrar la manera de distribuir objetos en bolsas, donde cada 
# objeto tiene un peso asociado y las bolas un limite de peso soportado.
# Los objetos a distribuir tienen los siguientes pesos asociados (5,2,8,4)
# El peso soportado por las bolsas es de 10, las cuales cuestan $5.
# Se pretende encontrar la distribucion de objetos en bolsas de manera de minimizar el costo.

PESOS = {1: 5, 2: 2, 3: 8, 4: 4}
#             Obj    | Bolsas.
ESTADO = ((1,2,3,4), ())

class Problema(SearchProblem):

    def is_goal(self, state):
        objetos, bolsas = state
        return len(objetos) == 0

    def actions(self, state):
        objetos, bolsas = state
        acciones = []
        for a in objetos:
            peso = PESOS[a]
            for b in bolsas:
                bolsa, pesobolsa = b
                if pesobolsa + peso <= 10:
                    acciones.append(('Sumar', (a, bolsa, pesobolsa + peso)))
                else:
                    acciones.append(('Comprar', None))
        if acciones == []:
            acciones.append(('Comprar', None))

        return acciones

    def result(self, state, action):
        objetos, bolsas = state
        act, oth = action
        lbolsas = list(bolsas)
        lobj = list(objetos)
        if act == 'Comprar':
            lbolsas.append((len(lbolsas)+1, 0))
        else:
            objeto, bolsa, pesonuevo = oth
            lobj.remove(objeto)
            for z in bolsas:
                bolsan, pesob = z
                if bolsa == bolsa:
                    lbolsas.remove((z))
                    lbolsas.append((bolsan, pesonuevo))
        return tuple(lobj), tuple(lbolsas)

    def cost(self, state1, action, state2):
        act, oth = action
        if act == 'Comprar':
            return 5
        else:
            return 0

    def heuristic(self, state):
        objetos, bolsas = state
        return len(objetos)

problema = Problema(ESTADO)
visor = BaseViewer()
resultado = astar(problema, graph_search=True, viewer=visor)
for a in resultado.path():
    print a
print resultado