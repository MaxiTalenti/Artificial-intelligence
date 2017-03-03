# coding=utf-8
import random
import itertools
from simpleai.search import CspProblem, backtrack, min_conflicts

# ¡¡¡ NO TERMINADO !!!

# Se desea realizar un programa que pueda organizar un conjunto de tareas de procesamiento en un conjunto de servidores de alto rendimiento,
# de forma de poder ejecutar todas las tareas en paralelo, aprovechando así el poder de cómputo global.
# Las tareas no pueden encolarse una detrás de otra, sí o sí deben ejecutarse en paralelo y sin compartir recursos,
# por lo que por ejemplo no es posible ejecutar en el mismo servidor tareas que sumen más procesadores que los que el servidor posee
# (lo mismo sucede con todos los demás recursos).
# Los servidores son los siguientes:
# 	Tesla: 8 procesadores, 32 GB de RAM.
# 	Goedel: 4 procesadores, 16GB de RAM, aceleradora gráfica.
# 	Bohr: 4 procesadores, 16GB de RAM.
# Y las tareas a ejecutar son las siguientes:
# 	Limpiador de datos: requiere 2 procesadores y 10 GB de RAM.
# 	Convertidor de entradas: requiere 5 procesadores y 20 GB de RAM.
# 	Entrenador de modelos: requiere 2 procesadores, 14 GB de RAM y una aceleradora gráfica.
# 	Almacenador de estadísticas: requiere 1 procesador y 1GB de RAM.
# 	Graficador de resultados: requiere 2 procesadores y 2 GB de RAM.
# 	Servidor de API: requiere 2 procesadores y 8 GB de RAM.

restricciones = []
variables = ('L', 'C', 'E', 'A', 'G', 'S')
dominios = dict((a, ['T', 'G', 'B']) for a in variables) 
serv_procesadores = {'T' : 8, 'G' : 4, 'B' : 4}
serv_ram = {'T' : 32, 'G' : 16, 'B' : 16}
serv_aceleradora = {'T' : 0, 'G' : 1, 'B' : 0}
tareas_procesadores = {'L' : 2, 'C' : 5, 'E' : 2, 'A' : 1, 'G' : 2, 'S' : 2}
tareas_ram = {'L' : 10, 'C' : 20, 'E' : 14, 'A' : 1, 'G' : 2, 'S' : 8}
tareas_aceleradora = {'L' : 0, 'C' : 0, 'E' : 1, 'A' : 0, 'G' : 0, 'S' : 0}

def procesadores(var, val):
	T = 0
	G = 0
	B = 0
	print var, val
	for a in val:
		if a == 'T':
			T = T + tareas_procesadores[var[val.index(a)]]
		if a == 'G':
			G = G + tareas_procesadores[var[val.index(a)]]
		if a == 'B':
			B = B + tareas_procesadores[var[val.index(a)]]
	print 'PROCESADORES', 'T', T, 'G', G, 'B', B
	if T > serv_procesadores['T']:
		return False
	if G > serv_procesadores['G']:
		return False
	if B > serv_procesadores['B']:
		return False
	return True

def ram(var, val):
	T = 0
	G = 0
	B = 0
	for a in val:
		if a == 'T':
			T = T + tareas_ram[var[val.index(a)]]
		if a == 'G':
			G = G + tareas_ram[var[val.index(a)]]
		if a == 'B':
			B = B + tareas_ram[var[val.index(a)]]
	print 'RAM', 'T', T, 'G', G, 'B', B
	if T > serv_ram['T']:
		return False
	if G > serv_ram['G']:
		return False
	if B > serv_ram['B']:
		return False
	return True	

def aceleradora(var, val):
	T = 0
	G = 0
	B = 0
	for a in val:
		if a == 'T':
			T = T + tareas_aceleradora[var[val.index(a)]]
		if a == 'G':
			G = G + tareas_aceleradora[var[val.index(a)]]
		if a == 'B':
			B = B + tareas_aceleradora[var[val.index(a)]]
	print 'AG', 'T', T, 'G', G, 'B', B
	if T > serv_aceleradora['T']:
		return False
	if G > serv_aceleradora['G']:
		return False
	if B > serv_aceleradora['B']:
		return False
	return True

def todos(var, val):
	return len(set(val)) == 3

restricciones.append(((variables), procesadores))
restricciones.append(((variables), ram))
restricciones.append(((variables), aceleradora))
#restricciones.append(((variables), todos))

problem = CspProblem(variables, dominios, restricciones)
resultado = backtrack(problem = problem)
print resultado

# {'A': 'G', 'C': 'T', 'E': 'T', 'G': 'G', 'L': 'T', 'S': 'G'}
# {'A': 'T', 'C': 'T', 'E': 'T', 'G': 'G', 'L': 'T', 'S': 'G'}

# G -> G, S       --- > 4 proc, 16 RAM, ag --- > 2 + 2 , 2 + 8
# T -> A, C, E, L --- > 8 proc, 32 RAM     --- > 1 + 20 + 14 + 10
# B -> None    --- > 4 proc, 15 RAM

# L: requiere 2 procesadores y 10 GB de RAM.
# C: requiere 5 procesadores y 20 GB de RAM.
# E: requiere 2 procesadores, 14 GB de RAM y una aceleradora gráfica.
# A: requiere 1 procesador y 1GB de RAM.
# G: requiere 2 procesadores y 2 GB de RAM.
# S: requiere 2 procesadores y 8 GB de RAM.