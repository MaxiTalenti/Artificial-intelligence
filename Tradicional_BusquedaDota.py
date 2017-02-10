# Esta es una versión muy simplificada del juego Dota. 
# En esta versión, el mapa es un tablero de 3x3, participa un solo jugador, 
# y tiene como objetivos derrotar a un héroe enemigo y destruir su base en la menor cantidad de acciones posibles. 
# El jugador comienza en la esquina inferior izquierda del mapa, 
# y en cada turno puede moverse a los casilleros limítrofes (no en diagonal). 
# Si se encuentra adyacente a un casillero de un enemigo o edificio, también tiene disponible la acción de atacar a dicho objeto, 
# destruyéndolo como resultado. Dos objetos no pueden estar en la misma posición.
# Al inicio del juego, el mapa y la distribución de objetos es la siguiente:

# |   |    | Be |
# |   |	He |    |	 
# | H |    |    |  	 
# H = Héroe (jugador), He = Héroe enemigo, Be = Base enemiga
# Ejemplo de acciones disponibles:
# |   |    | Be |
# | H |	He |    |	 
# |   |    |    |
 	 	 
# En este estado, el héroe está junto al héroe enemigo. 
# En esta situación puede moverse en dos direcciones o atacar a He. 
# Si ataca, en el estado resultante el héroe enemigo estaría muerto.