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
    def collor(collorName=None,getcollor=True):
        collor={        
                'blue' : (0,50,250),    'red' : (250,0,0),    'yellow' : (250,230,40),
                'anil' : (10,60,120),   'green' : (0,250,50), 'orange' : (250,160,0),
                'violet' : (180,40,250),'gray' : (150,150,150),  'white' : (255,255,255),
                'black' : (0,0,0)}
        if getcollor:
            return collor.get(collorName)
        else:
            return collor

    @staticmethod
    def pallet_generator(cor, numero_de_partes = 36, partes = []):

        for i in range(numero_de_partes+1):
            partes.append(Collors.interpole_collor(i / numero_de_partes, [255, 255, 255], list(cor), [0, 0, 0]))
        
        partes = list(map(lambda item: list(map(lambda x: int(x), item)), partes))
        partes = { key : tuple(value) for key,value in enumerate(partes[::-1],0)}

        return partes
    
    @staticmethod
    def interpole_collor(delta,inicio,fim,*args):
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
            tipo: None
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
    def create_button(cls,nome,position,area):
        """Gera um botão no dicionario da classe.

        Paramêtros:
            nome
                Tipo: String
                Descrição: Valor que representa a chave do botão no dicionario.
            Position
                Tipo: Tupla(int,int)
                Descrição: Tupla que representa a posição botão.
            area
                Tipo: Tupla(int,int)
                Descrição: Tupla que representa a escala dos botões.
        
        Retorno:
            Tipo: None
        """
        cls.__buttons[nome] = pygame.Rect(position,area)
    @classmethod
    def create_buttonList(cls,nome,number,initPosition,spacing,area,orientation='horizontal'):    
        """Gera uma lista de botões no dicionario da classe.

        Paramêtros:
            nome
                Tipo: String
                Descrição: Valor que representa a chave da lista no dicionario.
            number
                Tipo: Inteiro
                Descrição: Valor que representa a quantidade de botões na lista.
            initPosition
                Tipo: Tupla(int,int)
                Descrição: Tupla que representa a posição inicial do primeiro botão na fila.
            spacing
                Tipo: Inteiro
                Descrição: Valor que representa o espaçamento entre os botões na fila.
            area
                Tipo: Tupla(int,int)
                Descrição: Tupla que representa a escala dos botões.
            orientation
                Tipo: String
                Descrição: Valor que representa a orientação da fila, horizontal por padrão, mude para
                vertical para ter uma coluna de botões.
        
        Retorno:
            Tipo: None
        """
        buttonList = []
        if orientation == 'horizontal':
            positX = initPosition[0]
            spacing = spacing + area[0]
            for _ in range(0,number):
                positX = positX + spacing
                buttonList.append(pygame.Rect((positX,initPosition[1]),area))
        elif orientation == 'vertical':
            positY = initPosition[1]
            spacing = spacing + area[1]
            for _ in range(0,number):
                positY = positY + spacing
                buttonList.append(pygame.Rect((initPosition[0],positY),area))
        else:
            raise TypeError("Orientação invalida")
        cls.__buttons[nome] = buttonList
        
    @classmethod
    def button(cls,buttonName):
        """Retorna o Rect do botão especificado.

        Paramêtros:
            buttonName
                Tipo: String
                Descrição: Valor que representa a chave do botão no dicionario.
        
        Retorno:
            Tipo: Rect
        """        
        return cls.__buttons.get(buttonName)
    @classmethod
    def all_buttons(cls):
        """Retorna uma lista com a Chave de todos os botões no dicionario.

        Retorno:
            Tipo: List
        """    
        return cls.__buttons.keys()


if __name__ == '__main__':
    print(Collors.collor(getcollor=False)[0])
    pass
