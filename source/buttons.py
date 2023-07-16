import os 
import pygame 


class Hit_button_sprite(pygame.sprite.Sprite):
    def __init__(self,pos,scale)->None:
        super(Hit_button_sprite,self).__init__()
        self.image=pygame.image.load(os.path.join("assets\\buttons","hit.png"))
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale),
                                                         int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self)->None:
        pass

class Double_button_sprite(pygame.sprite.Sprite):
    def __init__(self,pos,scale)->None:
        super(Double_button_sprite,self).__init__()
        self.image=pygame.image.load(os.path.join("assets\\buttons","double.png"))
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale),
                                                         int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self)->None:
        pass


class Insure_button_sprite(pygame.sprite.Sprite):
    def __init__(self,pos,scale)->None:
        super(Insure_button_sprite,self).__init__()
        self.image=pygame.image.load(os.path.join("assets\\buttons","insure.png"))
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale),
                                                         int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self)->None:
        pass
class Split_button_sprite(pygame.sprite.Sprite):
    def __init__(self,pos,scale)->None:
        super(Split_button_sprite,self).__init__()
        self.image=pygame.image.load(os.path.join("assets\\buttons","split.png"))
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale),
                                                         int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self)->None:
        pass

class Stand_button_sprite(pygame.sprite.Sprite):
    def __init__(self,pos,scale)->None:
        super(Stand_button_sprite,self).__init__()
        self.image=pygame.image.load(os.path.join("assets\\buttons","stand.png"))
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale),
                                                         int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self)->None:
        pass
class Start_button_sprite(pygame.sprite.Sprite):
    def __init__(self,pos,scale)->None:
        super(Start_button_sprite,self).__init__()
        self.image=pygame.image.load(os.path.join("assets\\buttons","start.png"))
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale),
                                                         int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self)->None:
        pass
