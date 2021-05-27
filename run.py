import pygame
from pygame.locals import *

from simulation.fireeffect import *
from simulation.toolkit import *

def run_menu(screen,collors):

    button_1 = pygame.draw.rect(screen, (230,230,230), Menu.button('b_start'), border_radius=100)
    Text.draw_text(screen, 'START', (0, 0, 0), (button_1.centerx,button_1.centery), 20, bold=True)

    button_2 = pygame.draw.rect(screen, (230,230,230), Menu.button('b_stop'), border_radius=100)
    Text.draw_text(screen, 'STOP', (0, 0, 0), (button_2.centerx+2,button_2.centery), 20, bold=True)

    for num in range(1,8):
        pygame.draw.rect(screen, collors[num-1], Menu.button(f'b_collor{num}'), border_radius=100)

def run():
    pygame.init()
    timer = pygame.time.Clock()

    TELA = pygame.display.set_mode((Responsivity.width_screen(), Responsivity.height_screen()))
    pygame.display.set_caption("Simulation")

    effect = FireEffect(initPosition=700,height=140,width=80)

    Menu.create_button('b_start',position=(410,600),area=(80,30))
    Menu.create_button('b_stop',position=(510,600),area=(80,30))

    positX = 390
    collors = [tupla for name,tupla in Collors.collor(getcollor=False).items()]
    for num in range(1,8):
        positX = positX + 25
        Menu.create_button(f'b_collor{num}',position=(positX,550),area=(15,30))

    while True:
        TELA.fill((0,0,0))
        timer.tick(24)

        Text.draw_text(TELA,'FIRE',Collors.collor('orange'),(465,90),filefont='gabriola',size=70)
        Text.draw_text(TELA,'EFFECT',Collors.collor('orange'),(501,140),filefont='gabriola',size=70)

        effect.fire_calculate()
        effect.fire_render(TELA)

        run_menu(TELA,collors)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    effect.wind_intensity(direction='Right')
                if event.key == K_w:
                    effect.change_fire_collor()
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

            for num in range(1,8):
                if Menu.button(f'b_collor{num}').collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    effect.change_fire_collor(collors[num-1])

        pygame.display.flip()

run()