# pip install pygame

import pygame
import time
import random

pygame.init()

# Configuração da tela
largura = 1200
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
Preto = (0, 0, 0)
Branco = (255, 255, 255)
Vermelho = (255, 0, 0)
Azul = (0, 0, 255)

# Relógio
clock = pygame.time.Clock()
velocidade = 15

# Tamanho do bloco
tamanho_bloco = 20

# Fontes
fonte = pygame.font.SysFont(None, 35)
fonte_autor = pygame.font.SysFont(None, 20)

def mostrar_pontuacao(pontos):
    texto = fonte.render("Pontuação: " + str(pontos), True, Preto)
    tela.blit(texto, [10, 10])

def jogo():
    x = largura // 2
    y = altura // 2
    x_mudanca = 0
    y_mudanca = 0

    cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20

    fim_de_jogo = False

    while not fim_de_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        x += x_mudanca
        y += y_mudanca

        if x >= largura or x < 0 or y >= altura or y < 0:
            fim_de_jogo = True

        tela.fill(Branco)
        pygame.draw.rect(tela, Preto, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca = [x, y]
        cobra.append(cabeca)

        if len(cobra) > comprimento_cobra:
            del cobra[0]

        for bloco in cobra[:-1]:
            if bloco == cabeca:
                fim_de_jogo = True

        for bloco in cobra:
            pygame.draw.rect(tela, Azul, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

        mostrar_pontuacao(comprimento_cobra - 1)
        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20
            comprimento_cobra += 1

        clock.tick(velocidade)

    # TELA DE FIM DE JOGO 
    tela.fill(Branco)

    texto_fim = fonte.render(
        "Fim de Jogo! Pontuação: " + str(comprimento_cobra - 1),
        True,
        Vermelho
    )

    texto_autor = fonte_autor.render(
        "Projeto por Marcelino Samuel",
        True,
        Preto
    )

    rect_fim = texto_fim.get_rect(center=(largura // 2, altura // 2 - 20))
    rect_autor = texto_autor.get_rect(center=(largura // 2, altura // 2 + 20))

    tela.blit(texto_fim, rect_fim)
    tela.blit(texto_autor, rect_autor)

    pygame.display.update()
    time.sleep(3)

    pygame.quit()

if __name__ == "__main__":
    jogo()