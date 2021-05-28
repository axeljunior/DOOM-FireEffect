import pygame,random
from simulation.toolkit import *

def run_menu(screen,collors):
    Text.draw_text(screen,'FIRE',Collors.collor('orange'),(465,90),filefont='gabriola',size=70)
    Text.draw_text(screen,'EFFECT',Collors.collor('orange'),(501,140),filefont='gabriola',size=70)
    
    button_1 = pygame.draw.rect(screen, (230,230,230), Menu.button('b_start'), border_radius=100)
    Text.draw_text(screen, 'START', (0, 0, 0), (button_1.centerx,button_1.centery), 20, bold=True)

    button_2 = pygame.draw.rect(screen, (230,230,230), Menu.button('b_stop'), border_radius=100)
    Text.draw_text(screen, 'STOP', (0, 0, 0), (button_2.centerx+2,button_2.centery), 20, bold=True)

    collorButtonList = Menu.button('collor_buttons')
    for index in range(len(collorButtonList)):
        pygame.draw.rect(screen, collors[index], collorButtonList[index], border_radius=100)

    centerMenuButtonList = Menu.button('RandomDefault')
    for index in range(len(centerMenuButtonList)):
        pygame.draw.rect(screen, Collors.collor('gray'), centerMenuButtonList[index], border_radius=100)
        if index == 0:
            text = 'Random'
        elif index == 1:
            text = 'Default'
        Text.draw_text(screen, text, (0, 0, 0), (centerMenuButtonList[index].centerx+2,centerMenuButtonList[index].centery), 30, bold=True)

def mouse_event_listener(effect, collors):
    if pygame.mouse.get_pressed()[0]:
        if Menu.button('b_start').collidepoint(pygame.mouse.get_pos()):
            effect.fire_intensity(intensity=36)
        if Menu.button('b_stop').collidepoint(pygame.mouse.get_pos()):
            effect.fire_intensity(intensity=1)

        collorButtonList = Menu.button('collor_buttons')
        for index in range(len(collorButtonList)):
            if collorButtonList[index].collidepoint(pygame.mouse.get_pos()):
                effect.change_fire_collor(collors[index])

        centerMenuButtonList = Menu.button('RandomDefault')
        for index in range(len(centerMenuButtonList)):
            if centerMenuButtonList[index].collidepoint(pygame.mouse.get_pos()):
                if index == 0:
                    r = random.randint(0, 255)
                    g = random.randint(0, 255)
                    b = random.randint(0, 255)
                    Collor = (r,g,b)
                    effect.change_fire_collor(collor=Collor)
                elif index == 1:
                    effect.change_fire_collor(collor=None,default=True)

                