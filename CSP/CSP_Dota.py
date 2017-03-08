# coding=utf-8
import random
import itertools
from simpleai.search import CspProblem, backtrack, min_conflicts

# En el dota 0.02, el héroe tiene la posibilidad de comprar ítems que mejoran sus habilidades de combate.
# Pero algunos de esos items son demasiado costosos, o tienen consecuencias negativas si se combinan con otros.
# Se desea elegir 3 ítems para el héroe, de la siguiente lista de posibles ítems:

# Assault cuirass: armadura que acelera los ataques (costo: 5000).
# Battlefury: hacha que hace mucho daño, daña a enemigos cercanos, y regenera vida (costo: 4000).
# Cloak: capa con resistencia a conjuros (costo: 500).
# Hyperstone: piedra que acelera muchísimo los ataques (costo: 2000).
# Quelling blade: hacha que mejora levemente el daño (costo: 200).
# Shadow blade: espada que acelera los ataques y mejora el daño (costo: 3000).
# Veil of discord: capa que regenera vida y mejora a nivel general al personaje (costo: 2000).

# Pero en la elección se deben respetar las siguientes condiciones:
# 	Se dispone de 6000 monedas de oro para gastar en total, los ítems comprados no pueden superar esa suma.
# 	Hyperstone no se puede utilizar junto con Shadow blade, porque sus efectos no se suman.
# 	Quelling blade y Shadow blade no pueden utilizarse juntas, porque sus efectos no se suman.
# 	Cloak y Veil of discord no pueden utilizarse juntas, porque una es componente de la otra.
# 	Como mínimo se debe tener 1 ítem que regenere vida.
# 	Los ítems son únicos, no se puede tener dos veces el mismo ítem.

restricciones = []
variables = (1,2,3)
dominios = dict((a, ['AC', 'B', 'C', 'H', 'Q', 'SB', 'VD']) for a in variables) 
costos = {'AC' : 5000, 'B' : 4000, 'C' : 500, 'H' : 2000, 'Q' : 200, 'SB' : 3000, 'VD' : 2000}

def costototal(var, val): # Se dispone de 6000 monedas de oro para gastar en total, los items comprados no pueden superar esa suma.
	return (costos[val[0]] + costos[val[1]] + costos[val[2]]) <= 6000

def efectosnosuman(var, val): #	Hyperstone no se puede utilizar junto con Shadow blade, porque sus efectos no se suman.
	return not ('H' in val and 'SB' in val)

def efectosnosuman2(var, val): # Quelling blade y Shadow blade no pueden utilizarse juntas, porque sus efectos no se suman.
	return not ('Q' in val and 'SB' in val)

def componentesdeotro(var, val): # Cloak y Veil of discord no pueden utilizarse juntas, porque una es componente de la otra.
	return not ('C' in val and 'VD' in val)

def regenerarvida(var, val): # Como mínimo se debe tener 1 ítem que regenere vida.
	return (val.count('VD') + val.count('B')) >= 1

def itemsunicos(var, val):
	return len(set(val)) == 3

restricciones.append(((variables), costototal))
restricciones.append(((variables), efectosnosuman))
restricciones.append(((variables), efectosnosuman2))
restricciones.append(((variables), componentesdeotro))
restricciones.append(((variables), regenerarvida))
restricciones.append(((variables), itemsunicos))

problem = CspProblem(variables, dominios, restricciones)
resultado = backtrack(problem = problem)
print resultado