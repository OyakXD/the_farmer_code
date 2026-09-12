from __builtins__ import *

def ir_para(x,y):

    while get_pos_x() != x:
        if get_pos_x() < x:
            move(East)
        else:
            move(West)
    while get_pos_y() != y:
        if get_pos_y() != y:
            move(North)
        else:
            move(South)

def preparador():
    if num_items(Items.Fertilizer) >= 500:
        use_item(Items.Fertilizer)
    if get_water() <= 0.5:
        use_item(Items.Water)

def prepare_campo():
    if get_ground_type() != Grounds.Soil:
        preparador()
        till()