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
    return not (('Cabinas para tripulantes') in val and ('Motores') in val)
    # Verificar que el primero esta conectado al resto, no el segundo con el tercero!

def cabinas_lasers(var, val): # No puede haber baterías conectadas a lasers.
    return not (('Cabinas para tripulantes') in val and ('Lasers') in val)
    # Verificar que el primero esta conectado al resto, no el segundo con el tercero!

def sist_cabinas(var, val): # Los sistemas de vida extraterrestre sí o sí tienen que ubicarse conectados a cabinas.
    print val, (('Cabinas para tripulantes') in val and ('Sistemas de vida extraterrestres') in val)
    return (('Cabinas para tripulantes') in val and ('Sistemas de vida extraterrestres') in val)
    # Verificar que el primero esta conectado al resto, no el segundo con el tercero!

def sist_escudos(var, val): # Los escudos y los sistemas de vida extraterrestre no pueden estar conectados entre si.
    if ('Sistemas de vida extraterrestre') in val and ('Escudos') in val:
        return esta_desconectados(var[0],var[1])
    return True

def bahias_cabinas(var, val): # Las bahías de carga tienen que tener al menos una cabina conectada.
    if ('Bahias de carga') in val and ('Cabinas para tripulantes') in val:
        return not esta_desconectados(var[0], var[1])
    return True

def baterias(var, val): # Las baterías tienen que tener al menos dos sistemas conectados: Lasers, Cabinas de tripulantes, Escudos y Sistemas de vida extraterrestre.
    if ('Baterias') in val:
        return (val.count('Lasers') + val.count('Cabinas de tripulantes') + val.count('Escudos') + val.count('Sistemas de vida extraterrestre')) >= 2
    return True

def usar_todos(var, val): # Usar todos los modulos
    return len(set(val)) == 7

for a in vecinos:
    restricciones.append((a, modulos_diferentes))
    restricciones.append((a, ubicacion_motores))
    restricciones.append((a, cabinas_motores))
    restricciones.append((a, cabinas_lasers))
    restricciones.append((a, sist_cabinas))

#for var1, var2 in itertools.combinations(variables, 2):
    #restricciones.append(((var1,var2),modulos_diferentes))
    #restricciones.append(((var1,var2),ubicacion_motores))
    #restricciones.append(((var1,var2),cabinas_motores))
    #restricciones.append(((var1,var2),cabinas_lasers))
    #restricciones.append(((var1,var2),sist_cabinas))
    #restricciones.append(((var1,var2),sist_escudos))
    #restricciones.append(((var1,var2),bahias_cabinas))
    #restricciones.append(((var1,var2),baterias))

restricciones.append((variables, usar_todos))

def resolver(metodo_busqueda, iteraciones):
    problem = CspProblem(variables, dominios, restricciones)
    if metodo_busqueda == 'backtrack':
        resultado = backtrack(problem = problem)
        print resultado
        #def backtrack(problem, variable_heuristic='', value_heuristic='', inference=True):
    if metodo_busqueda == 'min_conflicts':
        resultado = min_conflicts(problem = problem, iterations_limit = iteraciones)
        print resultado
        #def min_conflicts(problem, initial_assignment=None, iterations_limit=0):

if __name__ == '__main__':
    p = CspProblem(variables, dominios, restricciones)
    resolver('backtrack', iteraciones= None)
