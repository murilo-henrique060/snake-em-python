import random
def gerar_posição():
    while True:
        continuar = True
        posição1 = random.randint(0,60) *10
        posição2 = random.randint(0,60) *10
        posição = (posição1, posição2)
        for posições in cobra:
            if posições == posição:
                continuar = False
                break
        if continuar:
            break
    return posição

cobra = [(280,290), (290,290), (300,290)]

