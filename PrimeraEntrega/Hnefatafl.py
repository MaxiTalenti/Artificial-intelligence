from simpleai.search import SearchProblem, breadth_first
from simpleai.search.viewers import ConsoleViewer
import random

INITIAL = '1010101000\n0000100000\n1000000000\n0100001101\n1000000110\n000X100001\n1000010001\n1000000100\n0010100001\n0100101100'
INITIALFILA = random.randint(0,9)
INITIALCOLUMNA = random.randint(0,9)

def state_to_board(state):
        return [list(x) for x in state.split('\n')]

def board_to_state(board):
    return '\n'.join([''.join(row) for row in board])

for i,x in enumerate(state_to_board(INITIAL)):
	if (i == INITIALFILA):
		print(x.index(INITIALCOLUMNA))
		for j,a in enumerate(x):
			if (j == INITIALCOLUMNA):
				if (a == '1'):
					print('La ubicacion hay que regenerarla', INITIALFILA,INITIALCOLUMNA)

print(INITIALFILA, INITIALCOLUMNA)

#def RevisarIzq(self, Fila, Columna):
#	if (Fila >= 1):

