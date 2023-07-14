import card


class Player:
    def __init__(self,ones,twos,fives)->None:
        self.cards=[[]]
        one_chips=ones
        two_chips=twos
        five_chips=fives
    cards=[]
    def add_card(self,hand,new_card)->None:
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
            return self.cards[hand][0].is_jack_or_ace()+self.cards[hand][1].is_jack_or_ace()==3