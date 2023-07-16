# import the pygame module, so you can use it
import pygame
import player
import game_black_jack
from card import *
from chips import *




# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((680,680))
    
    # define a variable to control the main loop
    running = True
     
    screen.fill((3,180,60))
    
    game=game_black_jack.Game(8,0.75,3/2,1,10,10,10)

    game.init_card_deck()

    chip_1=Chips_sprites(1,(280,570),5)
    chip_2=Chips_sprites(2,(330,570),5)
    chip_3=Chips_sprites(3,(380,570),5)
    
    sprit_group=pygame.sprite.Group()

    sprit_group.add(chip_1,chip_2,chip_3)
    
    while running:

        if len(game.deck) >= game.decks_before_shuffle * 52 *game.decks:
            game.shuffle_deck()
        
        
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        sprit_group.draw(screen)
        pygame.display.flip()
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()