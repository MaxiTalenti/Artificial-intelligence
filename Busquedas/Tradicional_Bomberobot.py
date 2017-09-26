# coding=utf-8
from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import ConsoleViewer, BaseViewer
import random

#Se planea construir un robot que sea capaz de salvar equipamiento de un depósito en caso de un incendio.
#El mismo deberá llevar todo el equipamiento valioso hacia la salida, antes de que las llamas consuman ninguno de los aparatos,
#y dispondrá de un pequeño extintor para aliviar las llamas mientras realiza la operación de rescate.
#Las llamas poco a poco van subiendo la temperatura de los aparatos, y con el extintor el robot puede temporalmente
#reducir dicha temperatura. Debido a su propósito el robot será construido con materiales resistentes al fuego,
#por lo que puede desplazarse por lugares incendiados sin problemas. Pero el equipamiento es frágil.
#A causa de la frecuencia de los incendios los aparatos fueron diseñados para resistir cierta temperatura,
#pero por encima de ese valor quedan dañados permanentemente y son irrecuperables. 
#El robot debe rescatarlos de las llamas antes de que eso suceda.
#Para probar la lógica del robot se desea simular su comportamiento en un ambiente simplificado. 
#Se divide al depósito en casilleros, uno de los cuales es la salida. 
#Los aparatos se ubican en esos casilleros (sí puede haber más de un aparato en el mismo lugar), y el robot se mueve por los
#casilleros de a uno por vez (el robot también puede estar en el mismo casillero que los aparatos).

# 0 | -	| -	| -	| -	|
# 1 | O	| -	| -	| O	|
# 2 | -	| -	| O	| -	|
# 3 | O	| -	| -	| S	| <- Esta el robot y la salida.
#     0   1   2   3

# El robot simulado dispone de acciones simuladas de usar extintor, moverse, y empujar aparato, con las siguientes limitaciones:
#•	Puede empujar de a un solo aparato por vez. Por más que haya varios aparatos en un casillero, el robot mueve de a uno por acción,
#	dejando el resto atrás.
#•	Solo puede empujar un aparato que se encuentra en su mismo casillero.
#•	Solo puede empujar un aparato hacia un casillero adyacente.
#•	Cuando empuja un aparato, el robot se mueve junto con el aparato (ej: robot y aparato en posición (0, 2), el robot realiza la acción "empujar el aparato a (0, 3)", y por ende quedan ambos, el robot y el aparato, en la posición (0, 3)).
#•	Al usar el extintor, enfría a todos los aparatos en la misma posición del robot.

# En el ejemplo se puede ver que en algunos casilleros hay aparatos, que los mismos poseen distintas temperaturas, y 
# que el robot puede encontrarse en un casillero. 
# En este momento el robot tiene la posibilidad de empujar o enfriar el aparato que se encuentra en su casillero.
# Y se ve un aparato que ya fue rescatado, en la salida del depósito.

# Temperatura:
# En cada turno de la simulación (cada acción realizada por el robot), el fuego hace subir de temperatura a todos los aparatos que
# no estén en la salida (la salida es al aire libre).
# Inicialmente los aparatos se encuentran a 300 grados, pero en cada turno sus temperaturas suben 25 grados.
# Un aparato puede resistir hasta 500 grados (incluidos) en el fuego, luego se rompe y queda inutilizado.
# Y cuando el robot utiliza su extintor, en un solo uso (una única acción) reduce en 150 grados la temperatura de todos los
# aparatos que se encuentran en su propia posición.

# Posiciones iniciales:
# Al inicio de las simulaciones, el robot siempre se encontrará en la salida del depósito, que se encuentra en la posición (3,3)
# (el depósito tiene dimensiones de 4x4 casilleros). Los aparatos en cambio, tendrán posiciones al azar, porque en la realidad
# sus usuarios son gente desordenada. Y la cantidad de aparatos es variable, definida al inicio de cada simulación.

# El robot debe salvar todo el equipamento. Solo se considera un éxito cuando todos los aparatos han llegado a la salida
# antes de ser destruidos. Recordar que los aparatos en la salida, no siguen subiendo de temperatura.

SALIDA = (3,3)
MAX_TEMP = 500
ROBOT = (3,3)
for x in range(4):
	for y in range(4):
		if (x,y)  != (3,3):
			if random.randint(0, 3) == 0:
				print (x,y)

OBJETOS = ((0,0,300), (2,2,300), (3,1,300), (0,1,300)) # Posicion X e Y, temperatura.
LIBRES = tuple((x,y) for x in range(4) for y in range(4) if (x,y) not in OBJETOS)

ESTADO = (ROBOT, OBJETOS, LIBRES)

class Problema(SearchProblem):
    def is_goal(self, state):
        robot, objetos, libres = state
        for x,y in objetos:
        	if (x,y) != SALIDA:
        		return False
        return True

    def actions(self, state):
        robot, objetos, libres = state
        x, y = robot
        acciones = []
        if (x+1,y) in libres:
            acciones.append(('Derecha', (x+1,y)))
        if (x-1,y) in libres:
            acciones.append(('Izquierda', (x-1,y)))
        if (x,y-1) in libres:
            acciones.append(('Arriba', (x,y-1)))
        if (x,y+1) in libres:
            acciones.append(('Abajo', (x,y+1)))
        if (x,y) in objetos:
            acciones.append(('Enfriar', (x,y)))
        if (x+1,y) in libres and robot in objetos and robot != SALIDA:
            acciones.append(('Empujar derecha', (x+1,y)))
        if (x-1,y) in libres and robot in objetos and robot != SALIDA:
            acciones.append(('Empujar izquierda', (x-1,y)))
        if (x,y-1) in libres and robot in objetos and robot != SALIDA:
            acciones.append(('Empujar arriba', (x,y-1)))
        if (x,y+1) in libres and robot in objetos and robot != SALIDA:
            acciones.append(('Empujar abajo', (x,y+1)))

        return acciones

    def result(self, state, action):
        robot, objetos, libres = state
        x, y = robot
        accion, movimiento = action
        obj = list(objetos)
        lib = list(libres)

        if accion in ('Derecha', 'Izquierda', 'Arriba', 'Abajo'):
        	x, y = movimiento

        if accion == 'Enfriar':
        	mayor_temp = 0 # Enfria el más caliente
        	objeto = objetos[0]
        	for obj in objetos:
        		x, y, temp = obj
    			if robot == (x,y):
        			if temp > mayor_temp:
	        			objeto = (x,y,temp)
    		
    		obj.remove((objeto))
    		obj.append((objeto[0],objeto[1],(objeto[2] -150)))

    	if accion in ('Empujar derecha', 'Empujar izquierda', 'Empujar arriba', 'Empujar abajo'):
    		# Empuja el primero de la lista (sino ver de empujar el más caliente).
    		#xobj, yobj = movimiento
    		x,y = movimiento
    		obj.remove(objetos[0])
    		obj.append((objetos[0][0], objetos[0][1], objetos[0][2]))


    	# Verifica temperatura para destruir objeto. (Hacer algo en heurística para las destrucciones)
    	for x,y,temp in obj:
    		if temp >= 500:
    			obj.remove(x,y,temp)

        return ((x,y), tuple(oc), tuple(lib))

    def cost(self, state1, action, state2):
        return 1

    def heuristic(self, state):
        h, ocupados, libres = state
        return len(ocupados)
                

problema = Problema(ESTADO)
visor = BaseViewer()
respuesta = astar(problema, graph_search=True, viewer=visor)
for a in respuesta.path():
    print a

