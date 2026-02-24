from plantacao import *

def move_n_dir(n, dir):
	for i in range(n):
		if get_pos_y() <= 2:
			plantar_carrot()
		else:
			plantar_arbusto()
		move(dir)
		

def move_direita(n):
	
	move_n_dir(n, East)
	

def move_cima(n):
	move_n_dir(n, North)
	
def move_baixo(n):
	move_n_dir(n, South)

def move_esquerda(n):
	move_n_dir(n, West)
	

