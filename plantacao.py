def plantar_carrot():
	# VERIFICAR OS CASOS BASES
	# SE A MADEIRA = 0, NÃO PLANTA CARROT
	if num_items(Items.Wood) > 0:
		if can_harvest():
			harvest()
		till()
		use_item(Items.Water)
		plant(Entities.Carrot)
		
	else:
		if can_harvest():
			harvest()
		plant(Entities.Bush)

def plantar_tree():
	if can_harvest():
		harvest()
	plant(Entities.Tree)
	
def plantar_arbusto():
	if can_harvest():
		harvest()
	plant(Entities.Bush)
		