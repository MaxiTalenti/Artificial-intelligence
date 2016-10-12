# coding=utf-8
import random
import itertools
from simpleai.search import CspProblem, backtrack, min_conflicts

variables = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']
dominios = dict((a, ['Lasers', 'Motores', 'Cabinas para tripulantes', 'Bahias de carga', 'Sistemas de vida extraterrestres', 'Escudos', 'Baterias']) for a in variables)
#vecinos = {'A' : ['B, C'], 'B' : ['A','D'], 'C' : ['A','D','E'], 'D' : ['B','C','F'], 'E' : ['C','G'],
 #'F' : ['D','H'], 'G' : ['E','I'], 'H' : ['F', 'I'], 'I' : ['J','G','H'], 'J' : ['I', 'K'], 'K' : ['L','J'],
# 'L' : ['K','M','N','P'], 'M' : ['L'], 'N' : ['L'], 'O' : ['P'], 'P' : ['L','O','Q'], 'Q' : ['P']}
vecinos = (('A','B','C'), ('B','A','D'), ('C','A','D','E'), ('D','B','C','F'), ('E','C','G'),
 ('F','D','H'), ('G','E','I'), ('H','F','I'), ('I','J','G','H'), ('J','I','K'), ('K','L','J'),
 ('L','K','M','N','P'), ('M','L'), ('N','L'), ('O','P'), ('P','L','O','Q'), ('Q','P'))
restricciones = []

def modulos_diferentes(var, val): # No es posible instalar dos módulos iguales conectados entre sí
    return len(set(val)) == len(val)

def ubicacion_motores(var, val): # Los motores solo pueden ubicarse en los slots traseros o en los 4 slots laterales.
    if ('Motores') in val:
        return var[val.index('Motores')] in ('O','P','Q','M','N','E','F')
    return True

def cabinas_motores(var, val): # Las cabinas no pueden estar conectadas a los motores
    if ('Cabinas para tripulantes') in val[0]:
        return not (('Motores') in val)
    if ('Motores') in val[0]:
        return not (('Cabinas para tripulantes') in val)
    return True

def baterias_lasers(var, val): # No puede haber baterías conectadas a lasers.
    if ('Baterias') in val[0]:
        return not (('Lasers') in val)
    if ('Lasers') in val[0]:
        return not (('Baterias') in val)
    return True

def sist_cabinas(var, val): # Los sistemas de vida extraterrestre sí o sí tienen que ubicarse conectados a cabinas.
    if (('Cabinas para tripulantes') in val[0]):
        return ('Sistemas de vida extraterrestres') in val
    if (('Sistemas de vida extraterrestres') in val[0]):
        return ('Cabinas para tripulantes') in val
    return True

def sist_escudos(var, val): # Los escudos y los sistemas de vida extraterrestre no pueden estar conectados entre si.
    if ('Sistemas de vida extraterrestres') in val[0]:
        return not (('Escudos') in val)
    if ('Escudos') in val[0]:
        return not (('Sistemas de vida extraterrestres') in val)
    return True

def bahias_cabinas(var, val): # Las bahías de carga tienen que tener al menos una cabina conectada.
    if ('Bahias de carga') in val[0]:
        return ('Cabinas para tripulantes') in val
    if ('Cabinas para tripulantes') in val[0]:
        return ('Bahias de carga') in val
    return True

def baterias(var, val): # Las baterías tienen que tener al menos dos sistemas conectados: Lasers, Cabinas de tripulantes, Escudos y Sistemas de vida extraterrestre.
    if ('Baterias') in val[0]:
        return (val.count('Lasers') + val.count('Cabinas de tripulantes') + val.count('Escudos') + val.count('Sistemas de vida extraterrestres')) >= 2
    return True

def usar_todos(var, val): # Usar todos los modulos
    return len(set(val)) == 7

for a in vecinos:
    restricciones.append((a, modulos_diferentes))
    restricciones.append((a, ubicacion_motores))
    restricciones.append((a, cabinas_motores))
    restricciones.append((a, baterias_lasers))
    restricciones.append((a, sist_cabinas))
    restricciones.append((a, sist_escudos))
    restricciones.append((a, bahias_cabinas))
    restricciones.append((a, baterias))

restricciones.append((variables, usar_todos))

def resolver(metodo_busqueda, iteraciones):
    problem = CspProblem(variables, dominios, restricciones)
    if metodo_busqueda == 'backtrack':
        resultado = backtrack(problem = problem)
        grabar('1', resultado, iteraciones = iteraciones)
        #def backtrack(problem, variable_heuristic='', value_heuristic='', inference=True):
    if metodo_busqueda == 'min_conflicts':
        resultado = min_conflicts(problem = problem, iterations_limit = iteraciones)
        print iteraciones, resultado
        grabar('2', resultado, iteraciones = iteraciones)
        #def min_conflicts(problem, initial_assignment=None, iterations_limit=0):

def grabar(busqueda, valor, iteraciones):
	archi=open('entrega_2.txt','a')
	archi.write('{}:{} Iteraciones: {}\n'.format(busqueda, valor, iteraciones))
	archi.close()

if __name__ == '__main__':
    p = CspProblem(variables, dominios, restricciones)
    resolver('backtrack', iteraciones = None)
    for a in range(1,5):
        resolver('min_conflicts', iteraciones= 3000*(a+1))
