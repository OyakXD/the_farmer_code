from __builtins__ import *
import utils

def plantacao_grass_tree():
    utils.preparador()
    if ((get_pos_x() % 2) == (get_pos_y() % 2)):
        plant(Entities.Tree)
    else:
        till()

def harvest_tree_grass():
    if can_harvest():
        harvest()
    else:
        while not can_harvest():
            do_a_flip()
        harvest()