from __builtins__ import *
from MS import *
import utils

petalas = []

def plantacao_sunflower():
    utils.preparador()
    plant(Entities.Sunflower)

def captura_petalas():
    tamanho = get_world_size()
    
    valor = measure() * tamanho * tamanho
    valor += get_pos_x() * tamanho
    valor += get_pos_y()
    petalas.append(valor)

def harvest_sunflower():
    global petalas
    petalas_ordenadas = mergeSort(petalas)

    for valor in petalas_ordenadas:

        tamanho = get_world_size()

        x = (valor // tamanho) % tamanho
        y = valor % tamanho

        utils.ir_para(x,y)

        if can_harvest():
            harvest()
        else:
            while not can_harvest():
                do_a_flip()
            harvest()

    while len(petalas) > 0:
        utils.ir_para(0,0)
        do_a_flip()
        petalas.pop()
