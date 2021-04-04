import pygame, random
from pygame.locals import *

#Inicializando o Pygame
pygame.init()

def jogo():
    global controle, maçã, pontuação, situação, cobra_sprite, VERDE_COBRA

    fonte_pontuação = pygame.font.SysFont('Free Pixel Regular',50)
    pontuação_texto = fonte_pontuação.render(f'{pontuação}',True,BRANCO)

    #Desenhando a Pontuação
    janela.blit(pontuação_texto,(10,10))

    #Desenhando a Maçã
    janela.blit(maçã_sprite, maçã)

    #Desenhando a cobra
    tamanho_cobra = len(cobra)
    intervalo = 205 // tamanho_cobra
    contador = 0

    for pos in cobra:
        cor = intervalo * contador

        verde = VERDE_COBRA[1] - cor
        azul = VERDE_COBRA[2] + cor
        if verde < 50:
            verde = 50
        if azul > 255:
            azul = 255
        VERDE_COBRA = (VERDE_COBRA[0],verde,azul)

        cobra_sprite.fill(VERDE_COBRA)
        janela.blit(cobra_sprite, pos)

        contador = 1

    VERDE_COBRA = VERDE

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
        pontuação += 10
        maçã = gerar_posição()
        cobra.append((cobra[-1][0],cobra[-1][1]))

    #Desenhando as Linhas
    for linhas_horizontais in range(69,599,10):
        pygame.draw.line(janela,CINZA,(0,linhas_horizontais),(599,linhas_horizontais),2)

    for linhas_verticais in range(599,0,-10):
        pygame.draw.line(janela,CINZA,(linhas_verticais,69),(linhas_verticais,599),2)

    #Desenhando a borda
    pygame.draw.line(janela,CINZA2,(0,79),(599,79),20)
    pygame.draw.line(janela,CINZA2,(0,589),(599,589),20)
    pygame.draw.line(janela,CINZA2,(9,79),(9,599),20)
    pygame.draw.line(janela,CINZA2,(589,79),(589,599),20)

    #Verificando a Colisão Com as Bordas
    if cobra[0][0] < 20 or cobra[0][0] > 578 or cobra[0][1] < 90 or cobra[0][1] > 578:
        situação = 3

    #Verificando a Colisão com a cobra
    for pos in range(len(cobra) -1,0,-1):
        if cobra[pos] == cobra[0]:
            situação = 3

def tela_inicial():

    fonte_iniciar = pygame.font.Font(None, 50)
    fonte_titulo = pygame.font.Font(None, 200)
    fonte_texto = pygame.font.Font(None, 16)
    titulo = fonte_titulo.render('Snake',True,VERDE)
    texto = fonte_texto.render('Pressione qualquer tecla para começar ou clique em \"iniciar\"',True,BRANCO)
    iniciar = fonte_iniciar.render('Iniciar',True,PRETO)

    pygame.draw.rect(janela,VERDE2,(132,370,350,150))
    pygame.draw.rect(janela,VERDE3,(142,380,330,130))
    janela.blit(titulo,(90,100))
    janela.blit(iniciar,(255,425))
    janela.blit(texto,(145,350))

def reset():
    global cobra, direção_atual,pontuação, maçã
    cobra = [(280,290), (290,290), (300,290)]
    direção_atual = 4
    pontuação = 0
    maçã = gerar_posição()

def telaGameOver():

    nomeArq = 'Pontuação_Máxima'

    try:
        a = open(nomeArq,'rt')
        a.close()
    except FileNotFoundError:
        existe = False
    else:
        existe = True

    if not existe:
        a = open(nomeArq,'wt+')
        a.close()
        a = open(nomeArq,'at')
        a.write('0')
        a.close
        pontuação_máxima = 0

    else:
        pontmáx = open(nomeArq,'rt')
        for linha in pontmáx:
            pontuação_máxima = int(linha)
        pontmáx.close()

    if pontuação > pontuação_máxima:
        open(nomeArq,'w').close()
        a = open(nomeArq,'at')
        a.write(f'{pontuação}')
        pontuação_máxima = pontuação

    fonte_game_over = pygame.font.Font(None,100)
    fonte_pontuação = pygame.font.Font(None,40)
    fonte_valor_pontuação = pygame.font.SysFont('Free Pixel Regular',40)
    fonte_mini_texto = pygame.font.Font(None,16)
    fonte_iniciar = pygame.font.Font(None,30)

    game_over = fonte_game_over.render('Game Over',True,VERDE)
    pontuação_atual = fonte_pontuação.render('Sua pontuação: ',True,BRANCO)
    pontuação_máxima_atual = fonte_pontuação.render('Maior Pontuação: ',True,BRANCO)
    valor_pontuação = fonte_valor_pontuação.render(f'{pontuação}',False,BRANCO)
    valor_maior_pontuação = fonte_valor_pontuação.render(f'{pontuação_máxima}',False,BRANCO)
    mini_texto = fonte_mini_texto.render('Pressione \"Enter\" ou no botão \"Recomeçar\" para reiniciar.',True,BRANCO)
    mini_texto2 = fonte_iniciar.render('Recomeçar',True,PRETO)
    mini_texto3 = fonte_iniciar.render('Sair',True,PRETO)

    pygame.draw.rect(janela,VERDE2,(115,408,200,100))
    pygame.draw.rect(janela,VERDE3,(125,418,180,80))
    pygame.draw.rect(janela,VERDE2,(325,408,200,100))
    pygame.draw.rect(janela,VERDE3,(335,418,180,80))
    janela.blit(game_over,(115,150))
    janela.blit(pontuação_atual,(115,250))
    janela.blit(pontuação_máxima_atual,(115,290))
    janela.blit(valor_pontuação,(335,242))
    janela.blit(valor_maior_pontuação,(360,282))
    janela.blit(mini_texto,(115,392))
    janela.blit(mini_texto2,(160,446))
    janela.blit(mini_texto3,(405,446))


def gerar_posição():
    while True:
        continuar = True
        posição1 = random.randint(2,57) *10
        posição2 = random.randint(9,57) *10
        posição = (posição1, posição2)
        for posições in cobra:
            if posições == posição:
                continuar = False
                break
        if continuar:
            break
    return posição

#Cores
PRETO = (0,0,0) #Cor do Fundo e do "Iniciar"
VERDE_COBRA = (50,255,50) #Cor da Cobra
VERDE = (50,255,50) #Cor do Título
VERDE2 = (0,150,0) #Cor da Borda do Botão
VERDE3 = (0,230,0) #Cor do Centro do Botão
BRANCO = (255,255,255) #Cor do Subtítulo
VERMELHO = (255,0,0) #Cor da Maçã
CINZA = (15,15,15) #Cor Das Linhas
CINZA2 = (75,75,75) #Cor das bordas

#Janela
janela = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake Game')

#Cobra
cobra = [(280,290), (290,290), (300,290)]
cobra_sprite = pygame.Surface((10,10))
velocidade = 10

#Maçã
maçã = gerar_posição()
maçã_sprite = pygame.Surface((10,10))
maçã_sprite.fill(VERMELHO)

situação = 1

#Pontuação
pontuação = 0

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

            if situação == 3:
                if evento.key == 13:
                    reset()
                    situação = 2

            elif controle:
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

            if situação == 1:
                if 131 < posição_mouse[0] < 483 and 369 < posição_mouse[1] < 521:
                    situação = 2

            if situação == 3:
                if 324 < posição_mouse[0] < 526 and 407 < posição_mouse[1] < 509:
                    pygame.quit()

                elif 114 < posição_mouse[0] < 316 and 407 < posição_mouse[1] < 509:
                    reset()
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
        telaGameOver()

    #Atualizar a tela
    pygame.display.update()
