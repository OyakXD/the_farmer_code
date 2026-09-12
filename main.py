from __builtins__ import *
import FSM
from MS import *
import control

while True:
    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            move(North)

            control.control()

        move(East)

    FSM.FSM()