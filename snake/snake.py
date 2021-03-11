import pygame, random
from pygame.locals import *

#Inicializando o Pygame
pygame.init()

def gerar_posição():
    while True:
        continuar = True
        posição1 = random.randint(0,59) *10
        posição2 = random.randint(0,59) *10
        posição = (posição1, posição2)
        for posições in cobra:
            if posições == posição:
                continuar = False
                break
        if continuar:
            break
    return posição

#Janela
janela = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake Game')

#Cobra
cobra = [(280,290), (290,290), (300,290)]
cobra_sprite = pygame.Surface((10,10))
cobra_sprite.fill((255,255,255))
velocidade = 10

#Maçã
maçã = gerar_posição()
maçã_sprite = pygame.Surface((10,10))
maçã_sprite.fill((255,0,0))

#Direção
direção_atual = 4

controle = True

relogio = pygame.time.Clock()

while True:

    for evento in pygame.event.get():
        
        if evento.type == QUIT:
            pygame.quit()
            quit()
        if evento.type == KEYDOWN and controle:
            if evento.key == K_UP and direção_atual != 3:
                direção_atual = 1

            if evento.key == K_RIGHT and direção_atual != 4:
                direção_atual = 2
            
            if evento.key == K_DOWN and direção_atual != 1:
                direção_atual = 3

            if evento.key == K_LEFT and direção_atual != 2:
                direção_atual = 4
            
            controle = False
            
    #Limitando o FPS
    relogio.tick(10)

    #Limpando a tela
    janela.fill((0,0,0))

    #Desenhando a Maçã
    janela.blit(maçã_sprite, maçã)

    #Desenhando a cobra
    for pos in cobra:
        janela.blit(cobra_sprite, pos)
    
    controle = True

    #Movendo a cobra
    for pos in range(len(cobra) -1,0,-1):
        cobra[pos] = (cobra[pos -1][0], cobra[pos -1][1])
    
    if direção_atual == 1: #Cima
        cobra[0] = (cobra[0][0], cobra[0][1] - velocidade)
    
    if direção_atual == 2: #Direita
        cobra[0] = (cobra[0][0] + velocidade, cobra[0][1])
    
    if direção_atual == 3: #Baixo
        cobra[0] = (cobra[0][0], cobra[0][1] + velocidade)
    
    if direção_atual == 4: #Esquerda
        cobra[0] = (cobra[0][0] - velocidade, cobra[0][1])

    #Verificando a colisão com a maçã
    if maçã == cobra[0]:
        maçã = gerar_posição()
        cobra.append((cobra[0][0],cobra[0][1]))

    #Verificando a Colisão Com as Bordas
    if cobra[0][0] < 0 or cobra[0][0] > 599 or cobra[0][1] < 0 or cobra[0][1] > 599:
        cobra = [(280,290), (290,290), (300,290)]
        direção_atual = 4

    #Atualizar a tela
    pygame.display.update()