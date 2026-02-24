def plantar(tipo):
	if tipo == "carrot":
		# Se não tiver madeira, não planta
		if num_items(Items.Wood) > 0:
			till()
			use_item(Items.Water)
			plant(Entities.Carrot)

	elif tipo == "tree":
		plant(Entities.Tree)

	elif tipo == "bush":
		plant(Entities.Bush)

	elif tipo == "pumpkin":
		# Se não tiver carrot, planta carrot primeiro
		if num_items(Items.Carrot) == 0:
			plantar("carrot")
		else:
			till()
			use_item(Items.Water)
			plant(Entities.Pumpkin)

		
def posicao_plant():
	if can_harvest():
		harvest()
	
	if get_pos_y() <= 5:
		plantar("pumpkin")
	elif get_pos_y() >= 6 and get_pos_y() <= 9:
		plantar("carrot")
	else:
		if (get_pos_x() == 0 and get_pos_y() == 8) or (get_pos_x() == 11 and get_pos_y() == 11):
			plantar("tree")
		else:	
			plantar("bush")
		