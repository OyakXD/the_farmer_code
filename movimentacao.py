def ir(n, dir):
    for i in range(n):
        move(dir)

def percorrer_campo(preparando=False):
    for linha in range(16):
        for coluna in range(16):
            if preparando:
                till()
            else:
                harvest()
                plant(Entities.Pumpkin)
                use_item(Items.Water)
            if coluna < 15:
                if linha % 2 == 0:
                    ir(1, East)
                else:
                    ir(1, West)
        if linha < 15:
            ir(1, North)   