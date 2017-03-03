# coding=utf-8
import random
import itertools
from simpleai.search import CspProblem, backtrack, min_conflicts

restricciones = []

variables = (1,2,3,4,5,6,7,8)
dominios = dict((a, ['S','I','M','R','G','D','C','E']) for a in variables)
otro = ((1,),(1,2),(1,2,3),(1,2,3,4),(1,2,3,4,5),(1,2,3,4,5,6),(1,2,3,4,5,6,7),(1,2,3,4,5,6,7,8))

# S en cualquier momento
# I debe ejecutarse luego de al menos otros 3 procesos. - OK
# M primero - OK
# R antes del Sopaperizador - OK
# G luego de Sopaperizador - OK
# D antes de G pero despues de S
# C luego de D y G
# E antes que R y I

# En la primera posición solo tiene que estar M.
dominios[1].remove('S')
dominios[1].remove('I')
dominios[1].remove('R')
dominios[1].remove('G')
dominios[1].remove('D')
dominios[1].remove('C')
dominios[1].remove('E')

def ic(var,val): # I luego de al menos otros 3 procesos.
    if 'I' in val:
        return val.index('I') > 2
    return True

def re(var, val): # R tiene que estar antes que S.
    if 'R' in val:
        if 'S' in val:
            return val.index('R') < val.index('S')
    return True

def ga(var, val): # G tiene que estar después de S.
    if 'G' in val:
        if 'S' in val:
            return val.index('G') > val.index('S')
        else:
            return False
    return True

def di(var,val): # D antes de G pero después de S . - > | S | D | G |.
    if 'D' in val:
        if 'S' in val:
            if 'G' in val:
                return (val.index('S') < val.index('D')) and (val.index('D') < val.index('G'))
            else:
                return (val.index('S') < val.index('D'))
        else:
            return False
    return True

def cr(var,val): # C luego de D y G
    if 'C' in val:
        if 'D' in val and 'G' in val:
            return (val.index('C') > val.index('D')) and (val.index('C') > val.index('G'))
        else:
            return False
    return True

def ec(var, val): #E antes a R e I
    if 'E' in val:
        if 'R' in val:
            if 'I' in val:
                return (val.index('E') < val.index('R')) and (val.index('E') < val.index('I'))
            else:
                return val.index('E') < val.index('R')
        else:
            if 'I' in val:
                return val.index('E') < val.index('I')
    return True

def todos(var,val):
    return len(set(val)) == 8


for a in otro:
    restricciones.append((a,ic))
    restricciones.append((a,re))
    restricciones.append((a,ga))
    restricciones.append((a,di))
    restricciones.append((a,cr))

restricciones.append((variables,todos))


problem = CspProblem(variables, dominios, restricciones)
resultado = backtrack(problem = problem)
print resultado
