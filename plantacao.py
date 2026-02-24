def plantar_carrot():
	# VERIFICAR OS CASOS BASES
	# SE A MADEIRA = 0, NÃO PLANTA CARROT
	if num_items(Items.Wood) > 0:
		if can_harvest():
			harvest()
		till()
		use_item(Items.Water)
		plant(Entities.Carrot)

def plantar_tree():
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	
def plantar_arbusto():
	if can_harvest():
		harvest()
	plant(Entities.Bush)
	
def plantar_pumpkin():
	# VERIFICAR OS CASOS BASES
	# SE O CARROT = 0 ELE NÃO PLANTA
	if num_items(Items.Carrot) == 0:
		plantar_carrot()
	else:
		if can_harvest():
			harvest()
		till()
		plant(Entities.Pumpkin)
		
def posicao_plant():
	if get_pos_y() <= 3:
		plantar_carrot()
	elif get_pos_y() >= 4 and get_pos_y() <= 7:
		plantar_pumpkin()
	else:
		if (get_pos_x() == 0 and get_pos_y() == 8) or (get_pos_x() == 11 and get_pos_y() == 11):
			plantar_tree()
		else:	
			plantar_arbusto()
		