import pygame
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(script_dir, '..')
class Chips_sprites(pygame.sprite.Sprite):
    def __init__(self,chip_number,pos,scale)->None:
        super(Chips_sprites,self).__init__()
        self.image=pygame.image.load(os.path.join(root_dir, "assets", "chips",str(chip_number)+"chip.png"))
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale),
                                                         int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self)->None:
        pass
