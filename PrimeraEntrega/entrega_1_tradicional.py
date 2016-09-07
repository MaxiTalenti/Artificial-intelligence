from simpleai.search import SearchProblem, breadth_first
from simpleai.search.viewers import ConsoleViewer
import random

INITIAL = '1010101000\n000100000\n1000000000\n0100001101\n1000000110\n000X100001\n1000010001\n1000000100\n0010100001\n0100101100'
INITIALFILA = random.randint(0,9)
INITIALCOLUMNA = random.randint(0,9)

## Lista las filas
def state_to_board(state):
        return [list(x) for x in state.split('\n')]

def board_to_state(board):
    return '\n'.join([''.join(row) for row in board])

## Obtine la posicion del rey.
def search_king(board):
	for row_index, row in enumerate(state_to_board(board)):
		for col_index, value in enumerate(row):
			if value == 'X':
				return (row_index, col_index)

def search_max_list(board):
	for i, row in enumerate(state_to_board(board)):
		x = len(row) -1
	return [x,i,0]

class problema(SearchProblem):
	def is_goal(self, state):
		for a, b in enumerate(search_king(state)):
			resultado = search_max_list(state)
			## Obtiene si el rey se encuentra en algún borde del cuadro
			if (b == 0 or b == resultado[2:3] or b == resultado[1:2] or b == resultado[0:1]):
				return '- Es meta el estado'
		return '- No es meta el estado'



## for i,x in enumerate(state_to_board(INITIAL)):
##	if (i == INITIALFILA):
##		print(x.index(INITIALCOLUMNA))
##		for j,a in enumerate(x):
##			if (j == INITIALCOLUMNA):
##				if (a == '1'):
##					print('La ubicacion hay que regenerarla', INITIALFILA,INITIALCOLUMNA)

problema = problema()
print(problema.is_goal(INITIAL))

#def RevisarIzq(self, Fila, Columna):
#	if (Fila >= 1):

