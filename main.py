import pygame
from pygame import Surface, Rect

WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324
# Inicializar o módulo do PyGame

pygame.init()
print("starting setup")
# Criando janela no PyGame
window: Surface = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

# Carregando imagem e gerando uma superfície
bg_surf: Surface = pygame.image.load("asset/background/orig.png").convert_alpha()
player_surf: Surface = pygame.image.load("./asset/ship/Ship1.png").convert_alpha()

# Obtendo retangulo da superficie
bg_rect: Rect = bg_surf.get_rect(left=0, top=0)
player_rect: Rect = player_surf.get_rect(left=100, top=100)

# Desenhando a imagem na janela (Window)
window.blit(source=bg_surf, dest=bg_rect)
window.blit(source=player_surf, dest=player_rect)

# Atualizando a janela
pygame.display.flip()

# Acrescentando um relógio no jogo
clock = pygame.time.Clock()

# Carregando musica ambiente no jogo
pygame.mixer_music.load("./asset/soundsambience/475620__tyops__game-intro-space-futuristic.wav")
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.3)

print("ending setup")
print("Loop starting")
while True:
    clock.tick(140)  # Este loop acontece 60 vezes por segundo ou 60 FPS
    print(f"{clock.get_fps() :.0f}")  # executando e printando o valor do FPS em tempo real no console

    window.blit(source=bg_surf, dest=bg_rect)
    window.blit(source=player_surf, dest=player_rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Loop ending")
            pygame.quit()
            quit()

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        player_rect.centery -= 1
    if pressed_key[pygame.K_s]:
        player_rect.centery += 1
    if pressed_key[pygame.K_a]:
        player_rect.centerx -= 1
    if pressed_key[pygame.K_d]:
        player_rect.centerx += 1

        pass
#
