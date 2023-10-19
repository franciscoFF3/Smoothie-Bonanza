import pygame
import random
# Inicialização do Pygame
pygame.init()

# Definições de tela
largura_tela, altura_tela = 600, 400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Smoothie Bonanza')

# Cores
BRANCO = (255, 255, 255)

# Imagens das frutas e scatter
pygame.image.load('cereja.png')


'cereja' == open ('cereja.png')
'maca' == open ('maçã.png')
'uva' == open ('uva.png')
'framboesa' == open ('framboesa.png')
'scatter' == open ('scatter.png')

frutas = ['cereja', 'maca', 'uva', 'framboesa']
scatter = 'scatter'

# Carregando imagens
imagens = {}
for fruta in frutas:
    imagens[fruta] = pygame.image.load(fruta)
imagens[scatter] = pygame.image.load(scatter)

# Função para mostrar a matriz de símbolos na tela
def mostrar_matriz(matriz):
    for i in range(3):
        for j in range(4):
            tela.blit(imagens[matriz[i][j]], (i * 150, j * 100))

# Função para girar os símbolos
def girar():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(4):
            linha.append(random.choice(frutas))
        matriz.append(linha)
    return matriz

# Função principal do jogo
def jogo():
    global rodadas_gratis
    tela.fill(BRANCO)  # Preenche a tela com a cor branca
    mostrar_matriz(matriz)

    # Verifica se o jogador ganhou rodadas grátis
    scatters = sum([linha.count(scatter) for linha in matriz])
    if scatters >= 4:
        rodadas_gratis += 10

    # Atualiza o contador de rodadas grátis
    fonte = pygame.font.Font(None, 36)
    texto_rodadas_gratis = fonte.render(f'Rodadas Grátis: {rodadas_gratis}', True, (0, 0, 0))
    tela.blit(texto_rodadas_gratis, (150, 320))

# Variáveis do jogo
matriz = girar()
rodadas_gratis = 0

# Loop principal do jogo
rodando = True
while rodando:
    # Tratamento de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # Gira os símbolos quando a barra de espaço é pressionada
                matriz = girar()

    # Atualiza a tela
    jogo()  # Chama a função do jogo para atualizar a lógica do jogo
    pygame.display.flip()  # Atualiza a tela

# Finaliza o Pygame
pygame.quit()
