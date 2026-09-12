from __builtins__ import *

fase = 0

# till -> plant -> harvest -> till .... -> harvest
def FSM():
    global fase

    if fase == 0: # Till
        fase = 1
    elif fase == 1: # Sunflower
        fase = 2
    elif fase == 2: # Harvest
        fase = 3
    elif fase == 3: # Carrot
        fase = 4
    elif fase == 4: # Harvest
        fase = 5
    elif fase == 5: # Grass and tree
        fase = 6
    elif fase == 6: # Harvest
        fase = 7
    elif fase == 7: # Till
        fase = 8
    elif fase == 8: # Pumpkin
        fase = 9
    elif fase == 9: # Harvest
        fase = 10
    elif fase == 10:
        fase = 11
    elif fase == 11:
        fase = 0