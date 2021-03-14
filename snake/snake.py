import pygame, random
from pygame.locals import *

#Inicializando o Pygame
pygame.init()

def jogo():
    global controle, maçã
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
        reset()

def tela_inicial():
    
    fonte_iniciar = pygame.font.Font(None, 50)
    fonte_titulo = pygame.font.Font(None, 200)
    fonte_texto = pygame.font.Font(None, 16)
    titulo = fonte_titulo.render('Snake',True,(50,255,50),(0,0,0))
    texto = fonte_texto.render('Pressione qualquer tecla para começar ou clique em \"iniciar\"',True,(255,255,255))
    iniciar = fonte_iniciar.render('Iniciar',True, (0,0,0), (0,230,0))

    pygame.draw.rect(janela,(0,150,0),(132,370,350,150))
    pygame.draw.rect(janela,(0,230,0),(142,380,330,130))
    janela.blit(titulo,(90,100))
    janela.blit(iniciar,(255,425))
    janela.blit(texto,(145,350))

def reset():
    global cobra, direção_atual
    cobra = [(280,290), (290,290), (300,290)]
    direção_atual = 4

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
cobra_sprite.fill((50,255,50))
velocidade = 10

#Maçã
maçã = gerar_posição()
maçã_sprite = pygame.Surface((10,10))
maçã_sprite.fill((255,0,0))

situação = 1

#Direção
direção_atual = 4

controle = True

relogio = pygame.time.Clock()

while True:

    for evento in pygame.event.get():
        
        if evento.type == QUIT:
            pygame.quit()
            quit()

        if evento.type == KEYDOWN:
            
            if situação == 1:
                situação = 2
            
            if controle:
                if evento.key == K_UP and direção_atual != 3:
                    direção_atual = 1

                if evento.key == K_RIGHT and direção_atual != 4:
                    direção_atual = 2
                
                if evento.key == K_DOWN and direção_atual != 1:
                    direção_atual = 3

                if evento.key == K_LEFT and direção_atual != 2:
                    direção_atual = 4
                
                controle = False
            
        elif evento.type == MOUSEBUTTONDOWN:

            posição_mouse = pygame.mouse.get_pos()
            print(posição_mouse[0],posição_mouse[1])

            if situação == 1:
                if 131 < posição_mouse[0] < 483 and 369 < posição_mouse[1] < 521:
                    situação = 2
                
    #Limitando o FPS
    relogio.tick(10)

    #Limpando a tela
    janela.fill((0,0,0))

    if situação == 1:
        tela_inicial()
    
    elif situação == 2:
        jogo()
    
    else:
        print('game_over()')

    #Atualizar a tela
    pygame.display.update()