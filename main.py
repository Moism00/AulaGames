import pygame

print('inicio')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('fin')

print('loop inicio')
while True:
    # chech for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # fecha a janela pygame
            quit()  # encerrar pygame
