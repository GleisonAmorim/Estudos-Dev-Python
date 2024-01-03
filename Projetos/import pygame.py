import pygame
import time
import random

pygame.init()

largura_tela = 800
altura_tela = 600

# Cores
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

tamanho_cobra = 20
velocidade = 15

fonte = pygame.font.SysFont(None, 35)

def cobra(tamanho, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho, tamanho])

def mensagem(msg, cor):
    tela_texto = fonte.render(msg, True, cor)
    tela.blit(tela_texto, [largura_tela / 6, altura_tela / 3])

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')

def jogoLoop():
    jogo = True

    while jogo:
        x1 = largura_tela / 2
        y1 = altura_tela / 2

        x1_change = 0
        y1_change = 0

        lista_cobra = []
        comprimento_cobra = 1

        comida_x = round(random.randrange(0, largura_tela - tamanho_cobra) / 10.0) * 10.0
        comida_y = round(random.randrange(0, altura_tela - tamanho_cobra) / 10.0) * 10.0

        game_over = False

        while not game_over:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    jogo = False
                    game_over = True
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        x1_change = -tamanho_cobra
                        y1_change = 0
                    elif evento.key == pygame.K_RIGHT:
                        x1_change = tamanho_cobra
                        y1_change = 0
                    elif evento.key == pygame.K_UP:
                        y1_change = -tamanho_cobra
                        x1_change = 0
                    elif evento.key == pygame.K_DOWN:
                        y1_change = tamanho_cobra
                        x1_change = 0

            x1 += x1_change
            y1 += y1_change
            tela.fill(branco)

            pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_cobra, tamanho_cobra])
            cobra(tamanho_cobra, lista_cobra)

            lista_cabeca = []
            lista_cabeca.append(x1)
            lista_cabeca.append(y1)
            lista_cobra.append(lista_cabeca)
            if len(lista_cobra) > comprimento_cobra:
                del lista_cobra[0]

            for segmento in lista_cobra[:-1]:
                if segmento == lista_cabeca:
                    game_over = True

            if x1 == comida_x and y1 == comida_y:
                comida_x = round(random.randrange(0, largura_tela - tamanho_cobra) / 10.0) * 10.0
                comida_y = round(random.randrange(0, altura_tela - tamanho_cobra) / 10.0) * 10.0
                comprimento_cobra += 1

            pygame.display.update()

            # Controle de velocidade
            pygame.time.Clock().tick(velocidade)

        tela.fill(branco)
        mensagem("Você perdeu! Pressione C para jogar novamente ou Q para sair.", vermelho)
        pygame.display.update()

        while game_over:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        jogo = False
                        game_over = False
                    if evento.key == pygame.K_c:
                        jogoLoop()

    pygame.quit()
    quit()

jogoLoop()
