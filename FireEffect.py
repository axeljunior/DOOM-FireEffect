import pygame,random
from pygame.locals import *

from Toolkit import *

firePallet = {    
                0 : (7,7,7),
                1 : (31,7,7),
                2 : (47,15,7),
                3 : (71,15,7),
                4 : (87,23,7),
                5 : (103,31,7),
                6 : (119,31,7),
                7 : (143,39,7),
                8 : (159,47,7),
                9 : (175,63,7),
                10 : (191,71,7),
                11 : (199,71,7),
                12 : (223,79,7),
                13 : (223,87,7),
                14 : (207,97,7),
                15 : (215,95,7),
                16 : (215,95,7),
                17 : (215,103,15),
                18 : (207,111,15),
                19 : (207,119,15),
                20 : (207,127,15),
                21 : (207,135,23),
                22 : (199,135,23),
                23 : (199,143,23),
                24 : (199,151,31), 
                25 : (191,159,31),
                26 : (191,159,31),
                27 : (191,167,39),
                28 : (191,167,39),
                29 : (191,175,47),
                30 : (183,175,47),
                31 : (183,183,47),
                32 : (183,183,55),
                33 : (207,207,111),
                34 : (223,223,159),
                35 : (239,239,199),
                36 : (255,255,255) }

class FireEffect(object):
    def __init__(self,initPosition,altura,largura):
        self.scale = Responsivity.rectangle_scale()
        self.area = (self.scale, self.scale)
        self.initPosition = initPosition
        self.canvasSize = altura
        self.wind = 0
        self.aux = 1
        self.canvas = {}

        self.fire_canvas(altura,largura)

    def fire_canvas(self,altura,largura):
        scale = self.scale
        y = self.initPosition

        for indice in list(range(altura)):
            value = { (scale*x, y) : [Block(area=self.area, position=(scale*x, y)), 0] for x in list(range(1,largura)) }
            self.canvas[indice] = value
            y = y-self.scale

    def fire_calculate(self,layer=1):
        for coord in self.canvas[layer].keys():
            y_down = coord[1]+self.scale
            layer_down = layer-1

            if self.canvas[layer_down].get((coord[0],y_down))[1] > 0:
                xNeighbor = self.scale*self.wind + coord[0]
                coordNeighbor = (xNeighbor, coord[1])
                decay = random.randint(0, 1)

                if coordNeighbor in self.canvas[layer].keys() and decay == 1:
                    self.canvas[layer][(coordNeighbor)][1] = self.canvas[layer_down].get((coord[0],y_down))[1] - random.randint(0, 1)
                else:    
                    self.canvas[layer][(coord)][1] = self.canvas[layer_down].get((coord[0],y_down))[1]-random.randint(0, 1)

        if layer < self.canvasSize-1:
            layer+=1
            self.fire_calculate(layer)
            
        print(self.wind)
    
    def fire_intensity(self,val):
        for coord in self.canvas[0].keys():
            self.canvas[0].get(coord)[1] = val
    
    def wind_intensity(self,direction):
        if direction == 'Right':
            self.wind = 1
        elif direction == 'Left':
            self.wind = -1

    def fire_render(self,surface,layer=0):
        for coord in self.canvas[layer].keys():
            cor = self.canvas[layer].get(coord)[1]
            pygame.draw.rect(surface, firePallet.get(cor), self.canvas[layer].get(coord)[0].rect)
            
        if layer < self.canvasSize-2:
            layer+=1
            self.fire_render(surface,layer=layer)

if __name__ == '__main__':
    pass
