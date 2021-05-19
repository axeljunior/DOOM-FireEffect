
import pygame
from pygame.locals import *

from FireEffect import *
from Toolkit import *

def run():
    pygame.init()
    timer = pygame.time.Clock()

    TELA = pygame.display.set_mode((Responsivity.width_screen(), Responsivity.height_screen()))
    pygame.display.set_caption("Simulation")

    effect = FireEffect(initPosition=700,altura=140,largura=79)
    effect.fire_intensity(36)

    while True:
        TELA.fill((0,0,0))
        timer.tick(10)

        effect.fire_calculate()
        effect.fire_render(TELA)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    effect.wind_intensity(direction='Right')
                if event.key == K_a:
                    effect.wind_intensity(direction='Left')

        pygame.display.flip()

run()