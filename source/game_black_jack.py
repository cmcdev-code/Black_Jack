import player
import card
import random




class Game:
    def __init__(self,number_of_decks,number_before_shuffle,black_jack,insurance_,one,two,five)->None:
        self.deck=[]
        self.decks=number_of_decks
        self.decks_before_shuffle=number_before_shuffle
        self.black_jack_pay=black_jack
        self.insurance=insurance_
        self.dealer = player.Player(9999,9999,9999)
        self.players = player.Player(one,two,five)
        self.bets=[]
        self.insurance_amount=(0,0,0)
        self.insurance_taken=False
    
    def shuffle_deck(self)->None:
        random.shuffle(self.deck)
    
    def offer_insurance(self)->bool:
        if self.dealer[0][1].is_jack_or_queen()==2:
            return True
        else:
            return False

    def init_card_deck(self)->None:
        del self.deck[:]
        for i in range(self.decks* 52):
            self.deck.append(card.Card(i % 52))
        self.shuffle_deck()

    def player_hit(self,hand)-> None:
        self.players.add_card(hand,self.deck.pop(0))

    def player_can_hit(self,hand)->bool:
        return not self.players.bust(hand) and self.players.get_hand_value(hand) != 21
    
    def player_place_bets(self, one,two ,five)->bool:
        if(self.players.check_money(one,two,five)):
            self.players.update_balance(-one,-two,-five)        
            return True
        else:
            return False
    def player_split(self,hand,one,two,five)->None:
        self.player_split(hand,one,two,five)
    
    def add_bet(self,one,two,five)->None:
        self.players.update_balance(-one,-two,-five)
        self.bets.append((one,two,five))

    def hands_won(self)->None:
        if not self.dealer.black_jack(0):

            for i in range(len(self.players.cards)):

                if self.players.black_jack(i):

                    self.players.update_balance(self.black_jack_pay * self.bets[i][0]*2,self.black_jack_pay * self.bets[i][1]*2,self.black_jack_pay * self.bets[i][2]*2)

                elif (self.players.get_hand_value(i) > self.dealer.get_hand_value(0)  or self.dealer.bust(0) )and  not self.players.bust(i):

                    self.players.update_balance(self.bets[i][0]*2,self.bets[i][1]*2,self.bets[i][2]*2)

                elif self.players.get_hand_value(i)== self.dealer.get_hand_value(0) or (self.players.bust(i) and self.dealer.bust(0)):
                    
                    self.players.update_balance(self.bets[i][0],self.bets[i][1],self.bets[i][2])
        elif self.dealer.black_jack(0) and self.players.insurance_taken:
            self.players.update_balance(2* self.insurance_amount[0],2* self.insurance_amount[1],2* self.insurance_amount[2])

        

    def reset_balance(self)->None:
        del self.bets[:]

    def init_round_(self,one,two,five)->None:
        self.insurance=(0,0,0)
        self.insurance_taken=False
        self.add_bet(one,two,five)


        self.dealer.add_card(0,self.deck.pop(0))
        
        self.players.add_card(0,self.deck.pop(0))

        self.dealer.add_card(0,self.deck.pop(0))

        self.players.add_card(0,self.deck.pop(0))

    def insurance_can_be_offered(self)->bool:
        return self.insurance and self.dealer.cards[0][1].value()==11

    def player_insurance_check(self,one,two,five)->bool:
        return self.players.check_money(one,two,five)
    
    def update_player_balance_insurance(self,one,two,five)->None:
        self.insurance_amount=(one,two,five)
        self.players.update_balance(-one,-two,-five)
    def check_player_can_double(self,hand)->bool:
        return self.players.can_double(self.bets[hand][0],self.bets[hand][1],self.bets[hand][2])

    def player_doubled(self,hand)->None:
        
        self.players.update_balance(-self.bets[hand][0],-self.bets[hand][1],-self.bets[hand][2])
        
        self.players.add_card(hand,self.deck.pop(0))

        self.bets[hand][0]*=2
        self.bets[hand][1]*=2
        self.bets[hand][2]*=2

