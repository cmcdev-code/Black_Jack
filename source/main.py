# import the pygame module, so you can use it
import pygame
import player
import game_black_jack
from card import *
from chips import *
from buttons import *


# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Black Jack")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((680, 680))

    # define a variable to control the main loop
    running = True

    screen.fill((3, 180, 60))

    game, sprit_group_list, round_bets, round_started, player_hand_cards, dealer_hand_cards, hand = init_game_variables()
    while running:

        if len(game.deck) >= game.decks_before_shuffle * 52 * game.decks:
            game.init_card_deck()
        if round_started == 1:
            player_hand_cards = [[]]
            dealer_hand_cards = []
            dealer_card_shown = Card_sprites(game.dealer.cards[0][1].number, (400, 100))

            player_card_1_shown = Card_sprites(game.players.cards[0][0].number, (340, 300))

            player_card_2_shown = Card_sprites(game.players.cards[0][1].number, (340, 350))
            local_sprit_group = pygame.sprite.Group()
            local_sprit_group.add(dealer_card_shown, player_card_1_shown, player_card_2_shown)

            sprit_group_list.append(local_sprit_group)
            dealer_hand_cards.append(dealer_card_shown)

            player_hand_cards[0].append(player_card_1_shown)
            player_hand_cards[0].append(player_card_2_shown)

            round_started = 2

        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Check if the left mouse button was clicked
                mouse_pos = pygame.mouse.get_pos()
                clicked_sprites = [sprite for sprite in sprit_group_list[0] if sprite.rect.collidepoint(mouse_pos)]
                if clicked_sprites:
                    # At least one sprite was clicked
                    if str(clicked_sprites[0]) == "<Chips_sprites Sprite(in 1 groups)>" and round_started == 0:
                        round_bets[0] = round_bets[0] + 1
                        print(clicked_sprites)
                    if (str(clicked_sprites[
                                0]) == "<Start_button_sprite Sprite(in 1 groups)>" and round_started == 0 and
                            round_bets[0] + round_bets[1] + round_bets[2] != 0):
                        if (game.players.check_money(round_bets[0], round_bets[1], round_bets[2])):
                            round_started = 1
                            game.init_round_(round_bets[0], round_bets[1], round_bets[2])
                            print(clicked_sprites)
                        else:
                            round_bets = [0, 0, 0]
                            print("Bets reset")

                    if (str(clicked_sprites[
                                0]) == "<Hit_button_sprite Sprite(in 1 groups)>" and round_started == 2 and game.player_can_hit(
                        hand)):
                        game.player_hit(hand)
                        new_local_card = Card_sprites(game.players.cards[hand][-1].number, (
                            player_hand_cards[hand][-1].rect.center[0], player_hand_cards[0][-1].rect.center[1] + 50))
                        sprit_group_list[1].add(new_local_card)
                        player_hand_cards[0].append(new_local_card)
        if game.players.bust(hand) and hand < (len(game.players.cards) - 1):
            hand += 1

        if not game.player_can_hit(hand) and hand < (len(game.players.cards) - 1):
            hand += 1
            print("Hand is now {}".format(hand))

        screen.fill((3, 180, 60))

        for i in sprit_group_list:
            i.update()

        for i in sprit_group_list:
            i.draw(screen)

        pygame.display.flip()


def init_game_variables():
    game = game_black_jack.Game(8, 0.75, 3 / 2, 1, 10, 10, 10)

    game.init_card_deck()

    chip_1 = Chips_sprites(1, (280, 570), 5)
    chip_2 = Chips_sprites(2, (330, 570), 5)
    chip_3 = Chips_sprites(3, (380, 570), 5)

    hit = Hit_button_sprite((140, 630), 2)
    stand = Stand_button_sprite((220, 630), 2)
    insure = Insure_button_sprite((300, 630), 2)
    double = Double_button_sprite((380, 630), 2)
    split = Split_button_sprite((460, 630), 2)
    start = Start_button_sprite((540, 630), 2)

    sprit_group = pygame.sprite.Group()

    sprit_group.add(chip_1, chip_2, chip_3, hit, stand, insure, double, split, start)
    round_bets = [0, 0, 0]

    player_hands_cards = [[]]
    dealer_hand_cards = []

    sprit_group_list = [sprit_group]
    round_started = 0

    hand = 0
    return game, sprit_group_list, round_bets, round_started, player_hands_cards, dealer_hand_cards, hand


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
