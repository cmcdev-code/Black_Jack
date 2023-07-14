
class Card:

    def __init__(self,num)->None:
        self.number = num
    def value(self)->int:
        values={0:2, 1:3, 2:4,3:5,4:6, 5:7,6:8,7:9,8:10,9:10,10:10,11:10,12:11}
        return values[self.number % 13]
    def is_jack_or_ace(self)->int:
        # 0 is no 1 is jack 2 is ace
        if self.number % 13==12:
            return 2
        if self.number % 13==11:
            return 1
        else: 
            return 0
        