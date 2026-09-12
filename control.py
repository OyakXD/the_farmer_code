from __builtins__ import *
import FSM
from MS import *
import sunflower
import utils
import carrot
import grass_tree


def plantacao_pumpkin():
    plant(Entities.Pumpkin)

def varredura_pumpkin():
    if get_entity_type() == Entities.Dead_Pumpkin:
        harvest()
        plant(Entities.Pumpkin)
    else:
        pass

def harvest_pumpkin():
    if can_harvest():
        harvest()
    
def control():

    if FSM.fase == 0:
        utils.prepare_campo()

    elif FSM.fase == 1:
        sunflower.plantacao_sunflower() 

    elif FSM.fase == 2:
        sunflower.captura_petalas()

    elif FSM.fase == 3:
        sunflower.harvest_sunflower()

    elif FSM.fase == 4:
        carrot.plantacao_carrot()

    elif FSM.fase == 5:
        harvest()

    elif FSM.fase == 6:
        grass_tree.plantacao_grass_tree()

    elif FSM.fase == 7:
        grass_tree.harvest_tree_grass()

    elif FSM.fase == 8:
        utils.prepare_campo()

    elif FSM.fase == 9:
        plantacao_pumpkin()

    elif FSM.fase == 10:
        varredura_pumpkin()

    elif FSM.fase == 11:
        harvest_pumpkin()