# coding=utf-8
import random
import itertools
from simpleai.search import CspProblem, backtrack, min_conflicts

# En la misma fábrica, también se desea desarrollar otra aplicacion que permita optimizar el almacenamiento de diferentes productos
# en proceso de fabricacion. Pero existen algunos problemas entre los productos que restrigen la manera en la cual pueden ser almacenados.
# El almacen puede dividirse en areas formando una grilla 5x5, donde cada area contendra un
# unico tipo de producto, y se busca llenar el almacen entero. 

# Los productos a almacenar, con sus requerimientos especiales, son los siguientes:
# - Lingotes de hierro: No se posee ninguna restriccion especial.
# - Lingotes de accero: no pueden ubicarse adyacentes a los lingotes de hierro, por el peligro de oxidación.
# - Espadas forjadas: deben encontrarse adyacentes entre si, para minimizar la necesidad de soportes especiales para las espadas.
# - Espadas templadas en proceso de enfriamento: no deben colocarse adyacentes entre si,
#   porque el calor en conjunto retrasaria el proceso de enfriamiento.
# - Espadas templadas terminadas: no pueden estar adyacentes a las espadas en enfriamiento,
#   porque el calor de las segundas podrian arruinar el templado terminado de las primeras.


restricciones = []

variables = tuple((a,b) for a in range(6) for b in range(6)) # Arranca de la izq inferior contando por casillero.
dominios = dict((a, ['LH', 'LA', 'EF', 'ETP', 'ETT']) for a in variables) 

def lingotesa(var, val): # No pueden ubicarse adyacentes a los lingotes de hierro, por el peligro de oxidación. RESTRICCIÓN BINARIA.
	return not 'LH' in val and 'LA' in val

def espadasforjadas(var, val): # Deben encontrarse adyacentes entre si, para minimizar la necesidad de soportes especiales para las espadas.
	if val.count('EF') != 0:
		return val.count('EF') != 1
	return True

def espadastempladasenproceso(var, val): # Espadas templadas en proceso de enfriamento: no deben colocarse adyacentes entre si. RESTRICCIÓN BINARIA.
	return val.count('ETP') != 2

def espadastempladasterminadas(var, val):
	return not 'ETP' in val and 'EF' in val

def todos(var, val):
	return len(set(val)) == 5

#for a in itertools.combinations(variables, 2):
	#restricciones.append((a, lingotesa))
	#restricciones.append((a, espadastempladasenproceso))

for a in variables: # Obtiene adyacentes y casilla a la cuales son adyacentes
	x, y = a
	casillas = []
	if (x-1, y) in variables:
		casillas.append((x-1,y))
	if (x+1, y) in variables:
		casillas.append((x+1, y))
	if (x, y-1) in variables:
		casillas.append((x, y-1))
	if (x, y+1) in variables:
		casillas.append((x, y+1))
	casillas.append((a))
	
	restricciones.append(((tuple(casillas)), lingotesa))
	restricciones.append(((tuple(casillas)), espadasforjadas))
	restricciones.append(((tuple(casillas)), espadastempladasenproceso))
	restricciones.append(((tuple(casillas)), espadastempladasterminadas))

#restricciones.append(((variables), todos))

problem = CspProblem(variables, dominios, restricciones)
resultado = backtrack(problem = problem)
print resultado

#  --- > Solución < ---
# 4 | - | - | - | - | - |
# 3 | - | - | - | - | - |
# 2 | - | - | - | - | - |
# 1 | - | - | - | - | - |
# 0 | - | - | - | - | - |
#     0   1   2   3   4