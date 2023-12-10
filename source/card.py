import pygame
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(script_dir, '..')
class Card:

    def __init__(self,num)->None:
        self.number = num

    def value(self)->int:
        values={0:2, 1:3, 2:4,3:5,4:6, 5:7,6:8,7:9,8:10,9:10,10:10,11:10,12:11}
        return values[self.number % 13]
    
table = {
    0: "2_clubs_white.png",
    1: "3_clubs_white.png",
    2: "4_clubs_white.png",
    3: "5_clubs_white.png",
    4: "6_clubs_white.png",
    5: "7_clubs_white.png",
    6: "8_clubs_white.png",
    7: "9_clubs_white.png",
    8: "10_clubs_white.png",
    9: "jack_clubs_white.png",
    10: "queen_clubs_white.png",
    11: "king_clubs_white.png",
    12: "ace_clubs_white.png",
    13: "2_diamonds_white.png",
    14: "3_diamonds_white.png",
    15: "4_diamonds_white.png",
    16: "5_diamonds_white.png",
    17: "6_diamonds_white.png",
    18: "7_diamonds_white.png",
    19: "8_diamonds_white.png",
    20: "9_diamonds_white.png",
    21: "10_diamonds_white.png",
    22: "jack_diamonds_white.png",
    23: "queen_diamonds_white.png",
    24: "king_diamonds_white.png",
    25: "ace_diamonds_white.png",
    26: "2_hearts_white.png",
    27: "3_hearts_white.png",
    28: "4_hearts_white.png",
    29: "5_hearts_white.png",
    30: "6_hearts_white.png",
    31: "7_hearts_white.png",
    32: "8_hearts_white.png",
    33: "9_hearts_white.png",
    34: "10_hearts_white.png",
    35: "jack_hearts_white.png",
    36: "queen_hearts_white.png",
    37: "king_hearts_white.png",
    38: "ace_hearts_white.png",
    39: "2_spades_white.png",
    40: "3_spades_white.png",
    41: "4_spades_white.png",
    42: "5_spades_white.png",
    43: "6_spades_white.png",
    44: "7_spades_white.png",
    45: "8_spades_white.png",
    46: "9_spades_white.png",
    47: "10_spades_white.png",
    48: "jack_spades_white.png",
    49: "queen_spades_white.png",
    50: "king_spades_white.png",
    51: "ace_spades_white.png"
}

class Card_sprites(pygame.sprite.Sprite):
    def __init__(self, card_number,pos):
        super(Card_sprites,self).__init__()
        self.image=pygame.image.load(os.path.join(root_dir, "assets", "Pixel Playing Cards Pack", str(table[card_number])))
        self.rect=self.image.get_rect()
        self.rect.center=pos

    def update(self):
        pass

