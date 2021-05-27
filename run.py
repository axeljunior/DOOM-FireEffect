import pygame
from pygame.locals import *

from simulation.fireeffect import *
from simulation.toolkit import *

def run_menu(screen):
    button_1 = pygame.draw.rect(screen, (230,230,230), Menu.button('b_start'), border_radius=100)
    Text.draw_text(screen, 'START', (0, 0, 0), (button_1.centerx,button_1.centery), 20, bold=True)

    button_2 = pygame.draw.rect(screen, (230,230,230), Menu.button('b_stop'), border_radius=100)
    Text.draw_text(screen, 'STOP', (0, 0, 0), (button_2.centerx+2,button_2.centery), 20, bold=True)

def run():
    pygame.init()
    timer = pygame.time.Clock()

    TELA = pygame.display.set_mode((Responsivity.width_screen(), Responsivity.height_screen()))
    pygame.display.set_caption("Simulation")

    effect = FireEffect(initPosition=700,height=140,width=80)

    Menu.create_button('b_start',position=(410,600),area=(80,30))
    Menu.create_button('b_stop',position=(510,600),area=(80,30))

    while True:
        TELA.fill((0,0,0))
        timer.tick(24)

        Text.draw_text(TELA,'FIRE',Collors.collor('orange'),(465,100),filefont='verdana',size=50)
        Text.draw_text(TELA,'EFFECT',Collors.collor('orange'),(501,140),filefont='verdana',size=50)

        effect.fire_calculate()
        effect.fire_render(TELA)

        run_menu(TELA)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    effect.wind_intensity(direction='Right')
                if event.key == K_a:
                    effect.wind_intensity(direction='Left')
                if event.key == K_1: #Turn on
                    effect.fire_intensity(intensity=1,i=0)
                if event.key == K_2: #Turn off
                    effect.fire_intensity(intensity=36,i=0)

            if Menu.button('b_start').collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                effect.fire_intensity(intensity=36)
            if Menu.button('b_stop').collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                effect.fire_intensity(intensity=1)

        pygame.display.flip()

run()