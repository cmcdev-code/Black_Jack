import player
import card
import random




class Game:
    def __init__(self,number_of_decks,number_before_shuffle,black_jack,insurance_)->None:
        self.deck=[]
        self.decks=number_of_decks
        self.decks_before_shuffle=number_before_shuffle
        self.black_jack_pay=black_jack
        self.insurance=insurance_
        self.dealer = player.Player(9999,9999,9999)
    def shuffle_deck(self)->None:
        random.shuffle(self.deck)
    
    def offer_insurance(self):
        
    
    
        
