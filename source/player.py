import card


class Player:
    def __init__(self,ones,twos,fives)->None:
        self.cards=[[]]
        self.one_chips=ones
        self.two_chips=twos
        self.five_chips=fives
        self.insurance_taken=False
    
    def add_card(self,hand,new_card: card.Card)->None:
        if hand >= len(self.cards) and hand == len(self.cards):
            local=[]
            local.append(new_card)
            self.cards.append(local)
        elif hand >= len(self.cards)+2:
            print("Not possible")
        else:
            self.cards[hand].append(new_card)
    def remove_cards(self)->None:
        if len(self.cards) >=2:
            del self.cards[1:len(self.cards)]
        del self.cards[0][:]
    def check_money(self,one,two,five)->bool:
        return self.one_chips-one >=0 and self.two_chips-two>=0 and self.five_chips-five>=0
    def update_balance(self,one,two,five)->None:
        self.one_chips+=one
        self.two_chips+=two
        self.five_chips+=five

    def get_hand_value(self,hand)-> int:
        value =0
        for i in range(len(self.cards[hand])):
            value+=self.cards[hand][i].value()
        if value<= 21:
            return value
        else:
            number_of_aces=0
            for i in range(len(self.cards[hand])):
                if self.cards[hand][i].value()==11:
                    number_of_aces+=1
            if number_of_aces==0:
                return value
            for i in range(number_of_aces):
                value-=10
                if(value<=21 and value>=2):
                    return value
            else:
                value+= number_of_aces*11
                return value
    def bust(self,hand)-> bool:
        return self.get_hand_value(hand)>21
    def black_jack(self,hand)->bool:
        if len(self.cards[hand])>2 or self.get_hand_value(hand)!= 21:
            return False 
        else:
            return True
    def split(self,hand,one,two,five)->None:
        self.add_card(len(self.cards),self.cards[hand].pop())

            
    def can_split(self,hand,one,two,five)->bool:
        if(len(self.cards[hand]==2 and self.check_money(one,two,five)) and (self.cards[hand][0] == self.cards[hand][1] or (self.cards[hand][0]+1)% (self.cards[hand][1]+1)==0 if self.cards[hand][0]< self.cards[hand][1] else (self.cards[hand][1]+1)% (self.cards[hand][0]+1)==0)):
            return True
        else:
            return False
        
    def can_double(self,one,two,five)->bool:
        return self.check_money(one,two,five)
    def double_hand(self,hand,card):
        self.add_card(hand,card)
