import pygame
from pygame.locals import *

from simulation.fireeffect import *
from simulation.menu import *
from simulation.toolkit import *

def run():
    pygame.init()
    timer = pygame.time.Clock()

    TELA = pygame.display.set_mode((Responsivity.width_screen(), Responsivity.height_screen()))
    pygame.display.set_caption("Simulation")

    effect = FireEffect(initPosition=700,height=140,width=80)

    Menu.create_button('b_start',position=(410,600),area=(80,30))
    Menu.create_button('b_stop',position=(510,600),area=(80,30))
    Menu.create_buttonList(nome='collor_buttons',number=7,initPosition=(393,550),spacing=15,area=(10,30))

    Menu.create_buttonList(nome='RandomDefault',number=2,initPosition=(412,250),spacing=30,area=(175,50),orientation='vertical') 

    collors = [tupla for name,tupla in Collors.collor(getcollor=False).items()]

    while True:
        TELA.fill((0,0,0))
        timer.tick(24)

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
                if event.key == K_a:
                    effect.wind_intensity(direction='Left')
        
        mouse_event_listener(effect, collors)

        pygame.display.flip()

run()