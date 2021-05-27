import pygame,random
from pygame.locals import *

from simulation.toolkit import *

firePallet = {   0 : (0,0,0),        1 : (7,7,7),      2 : (47,15,7),     3 : (71,15,7),     4 : (87,23,7),     5 : (103,31,7),    6 : (119,31,7), 
                 7 : (143,39,7),     8 : (159,47,7),    9 : (175,63,7),   10 : (191,71,7),   11 : (199,71,7),   12 : (223,79,7),    13 : (223,87,7),
                14 : (207,97,7),    15 : (215,95,7),   16 : (215,95,7),   17 : (215,103,15), 18 : (207,111,15), 19 : (207,119,15),  20 : (207,127,15),
                21 : (207,135,23),  22 : (199,135,23), 23 : (199,143,23), 24 : (199,151,31), 25 : (191,159,31), 26 : (191,159,31),  27 : (191,167,39),
                28 : (191,167,39),  29 : (191,175,47), 30 : (183,175,47), 31 : (183,183,47), 32 : (183,183,55), 33 : (207,207,111), 34 : (223,223,159),
                35 : (239,239,199), 36 : (255,255,255) }

class FireEffect(object):
    def __init__(self,initPosition,height,width):
        self.pixel = Responsivity.rectangle_scale()
        self.area = ( self.pixel, self.pixel )
        self.initPosition = initPosition
        self.canvasSize = height
        self.wind = 0
        self.canvas = {}

        self.fire_canvas( height, width )

    def fire_canvas(self,height,width):
        y = self.initPosition

        for layer in list(range(height)):
            valueLayer = { ( self.pixel * x, y ) : [Block( self.area, ( self.pixel * x, y )), 0] for x in list( range( 1, width )) }
            self.canvas[layer] = valueLayer
            y = y - self.pixel

    def fire_calculate(self,layer=1):
        for coord in self.canvas[layer].keys():
            yDown = coord[1] + self.pixel
            layerDown = layer - 1

            pixelDown = self.canvas[layerDown].get((coord[0],yDown))[1]
            horizontalDecay = random.randint(0, 1)
            verticalDecay = random.randint(0, 1)

            if pixelDown > 0:

                if self.wind == 0:
                    xNeighbor = self.pixel * random.randint(-1, 1) + coord[0]
                else:
                    xNeighbor = self.pixel * self.wind + coord[0]

                coordNeighbor = (xNeighbor, coord[1])

                if coordNeighbor in self.canvas[layer].keys() and horizontalDecay == 1:
                    self.canvas[layer][(coordNeighbor)][1] = pixelDown - verticalDecay
                else:    
                    self.canvas[layer][(coord)][1] = pixelDown - verticalDecay
            # else:
            #     self.canvas[layer][(coord)][1] = 0

        if layer < self.canvasSize - 1:
            layer += 1
            self.fire_calculate(layer=layer)

    def fire_render(self,surface,layer=0):
        for coord in self.canvas[layer].keys():
            intensity = self.canvas[layer].get(coord)[1]
            pygame.draw.rect(surface, firePallet.get(intensity), self.canvas[layer].get(coord)[0].rect)
            # pygame.draw.rect(surface, Collors.change_collor(intensity=intensity,cor=Collors.collor('orange')), self.canvas[layer].get(coord)[0].rect)
            
        if layer < self.canvasSize - 2:
            layer += 1
            self.fire_render(surface,layer=layer)

    def fire_intensity(self,intensity,i=0):
        for coord in self.canvas[i].keys():
            self.canvas[i].get(coord)[1] = intensity

    def wind_intensity(self,direction):
        if direction == 'Right':
            self.wind += 1
        elif direction == 'Left':
            self.wind += -1

if __name__ == '__main__':
    pass
