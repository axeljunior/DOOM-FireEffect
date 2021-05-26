import pygame, os

class Responsivity(object):
    __widthScreen = 600 #Largura
    __heightScreen = 720 #Altura
    __rectangle_scale = 5
    @classmethod
    def height_screen(cls):
        return cls.__heightScreen
    @classmethod
    def width_screen(cls):
        return cls.__widthScreen
    @classmethod
    def rectangle_scale(cls):
        return cls.__rectangle_scale

class Block(pygame.sprite.Sprite):
    def __init__(self, area, position=None):
        super().__init__()
        self.image=pygame.Surface(area)
        self.rect=self.image.get_rect()
        if not isinstance(position,type(None)):
            self.update((position))
    
    def set_texture(self, texture, deform=None):
        self.image = pygame.image.load(texture)
        if not isinstance(deform,type(None)):
            self.image = pygame.transform.scale(self.image,(deform[0],deform[1]))
        self.rect=self.image.get_rect()

    def update(self, cordenates):
        self.rect.x, self.rect.y = cordenates

class Text(object):
    @staticmethod
    def draw_text(screen, text, color, surface, size=20, bold=False, italic=False, filefont='arial', loadfile=False):

        if loadfile == True:
            fontobj = pygame.font.Font(os.path.join('assets/fonts',filefont), size) 
        else:
            fontobj = pygame.font.SysFont(filefont, size, bold=bold, italic=italic)

        textobj = fontobj.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.center = surface
        screen.blit(textobj, textrect)

class Collors(object):
    @staticmethod
    def collor(collorName):
        collor={        
                'white' : (255,255,255),
                'black' : (0,0,0),
                'gray' : (50,50,50),
                'red' : (250,0,0),
                'orange' : (250,160,0),
                'yellow' : (250,230,40),
                'green' : (0,250,50),
                'blue' : (0,50,250),
                'anil' : (10,60,120),
                'violet' : (180,40,250)}
        return collor.get(collorName)
    
    @staticmethod
    def change_collor(intensity,cor):
        r,g,b = cor
        
        if r <= 255:
            r += intensity*2
        if g <= 255:
            g += intensity*2
        if b <= 255:
            b += intensity*2

        # print((r,g,b))
        return (r,g,b)
        # /**
        # * Interpola valores baseados em um delta.
        # * @example interpolar(0.75, 0, [100, -100], 0) -> [-50, 50]
        # * @param {number} delta Valor no intervalo [0, 1] que representa o percentual da interpolação.
        # * @param {number|number[]} inicio Valor(es) que representa(m) o inicio da interpolação.
        # * @param {number|number[]} fim Valor(es) que representa(m) o final ou o próximo ponto da interpolação.
        # * @param  {...number} args Valor(es) que representa(m) os pontos da interpolação.
        # */
    
    @staticmethod
    def interpole_collor(
        delta,
        inicio,
        fim,
        *args
    ):
        """Interpola valores baseados em um delta.

        Paramêtros:
            delta
                Tipo: númerico
                descrição: Valor no intervalo [0, 1] que representa o percentual da interpolação.
            inicio
                tipo: númerico ou lista númerica
                descrição: Valor(es) que representa(m) o inicio da interpolação.
            fim
                tipo: númerico ou lista númerica
                descrição: Valor(es) que representa(m) o final ou o próximo ponto da interpolação.
            args
                tipo: lista de (númerico ou lista númerica)
                descrição: Valor(es) que representa(m) os pontos da interpolação.
        
        Retorno:
            tipo: número ou lista númerica

        Exemplos:
            interpolar(0.5, 0, 200) -> [100]
            interpolar(0.75, 0, 200) -> [150]
            interpolar(0.5, 0, 200, 100, 0) -> [50]
            interpolar(0.75, 0, [100, -100], 0) -> [50, -50]
            interpolar(0.5, [255, 255, 255], [0, 0, 0]) -> [127.5, 127.5, 127.5]
            interpolar(0.5, [255, 255, 255], [0, 0, 0], [-100, 0, 100], [50, 0, 0]) -> [-50, 0, 50]

        """
        parts = [inicio, fim, *args]
        if (delta <= 0): 
            return parts[0]
        value = int((len(parts) - 1) * delta)
        inc = len(parts) / (len(parts) - 1)
        modDelta = ((delta * len(parts)) % inc) / inc
        if (value >= len(parts) - 1):
            return parts[len(parts) - 1]
        try:
            l = list(map(lambda part: isinstance(part, list), parts))
            index = l.index(True)
        except:
            return (
            ((parts[value + 1]) - (parts[value])) * modDelta +
            (parts[value])
            )
        length = len(parts[index])
        for i in range(len(parts)):
            if isinstance(parts[i], list) and len(parts[i]) != length:
                raise Exception('Argumentos com tamanhos diferentes!')
            
        
        resultado = []
        # for (i = 0 i < (parts[index]).length i++):
        for i in range(len(parts[index])):
            if (isinstance(parts[value], list)): 
                x = (parts[value])[i]
            else:
                x = (parts[value])
            if isinstance(parts[value + 1], list):
                y = (parts[value + 1])[i]
            else:
                y = (parts[value + 1])
            resultado.append((y - x) * modDelta + x)
        
        return resultado

    # @staticmethod
    # def change_collor(tam,cor,num=0):
    #     if tam <= 3:
    #         return Collors.collor(cor)
    #     else:
    #         r,g,b = Collors.collor(cor)

    #         num = 5*tam

    #         if num >= 250:
    #             num = 250

    #         if num > r and num <= 250:
    #             r = num
    #         if num > g and num <= 250:
    #             g = num
    #         if num > b and num <= 250:
    #             b = num

    #         return (r,g,b)

class ArtResource(object):
    __sfxLibrary={}
    @staticmethod
    def image_load(filename):
        return os.path.join('assets/images',filename)

    @classmethod
    def sound_add_sfx(cls,filename,extension,volume=None):
        cls.__sfxLibrary[filename] = pygame.mixer.Sound(os.path.join('assets/sounds',f'{filename}.{extension}'))
        if not isinstance(volume,type(None)):
            cls.__sfxLibrary[filename].set_volume(float(volume))
    @classmethod
    def sound_play_sfx(cls,filename):
        cls.__sfxLibrary.get(filename).play()

    @staticmethod
    def sound_add_bgm(filename,extension,volume):
        pygame.mixer.music.load(os.path.join('assets/sounds',f'{filename}.{extension}'))
        pygame.mixer.music.set_volume(float(volume))
    @staticmethod
    def sound_play_bgm():
        pygame.mixer.music.play(-1)

class Menu(object):
    __buttons = {}
    
    @classmethod
    def create_button(cls,nome=str,position=tuple,area=tuple):
        cls.__buttons[nome] = pygame.Rect(position,area)
    @classmethod
    def button(cls,buttonName):
        return cls.__buttons.get(buttonName)
    @classmethod
    def all_buttons(cls):
        return cls.__buttons.keys()

if __name__ == '__main__':
    def change_collor(intensity,cor):
        r,g,b = cor
        
        if r <= 255 and intensity < 9:
            r += intensity*2
        if g <= 255 and intensity < 9:
            g += intensity*2
        if b <= 255 and intensity < 9:
            b += intensity*2
        # print((r,g,b))
        return (r,g,b)
    
    for n in list(range(36)):
        print(change_collor(n,(250,160,0)))
    pass
