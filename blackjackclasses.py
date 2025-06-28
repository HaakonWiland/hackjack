import random

possibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
possibleSuits = ["diamonds", "hearts", "spades", "clubs"]

class Card:
    def __init__(self, Value, Suit):
        self.value = Value
        self.suit = Suit
    
    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __repr__(self):
        return self.__str__()

# TODO: We want value and suit to only have "value" and "suit" as possible values


class CardDeck:
    def __init__(self):

        self.cardDeck: list[tuple] = []

        for v in possibleValues:
            for s in possibleSuits:
                card: tuple = Card(v, s)
                self.cardDeck.append(card)

        self.shuffle()

    def getDeck(self):
        return self.cardDeck


    # TODO: This has do shuffle good, find optimal way later.
    def shuffle(self):
        randomValue = 0
        

        for card in range(len(self.cardDeck)):

            randomValue: int = random.randint(0, 10000)
            index: int = (randomValue) % 43
                
            self.cardDeck[card] = self.cardDeck[index]
            self.cardDeck[index] = self.cardDeck[card]


    def drawCard(self):
        card = self.cardDeck[0]
        self.cardDeck = self.cardDeck[1:] 

        return card


class Player:
    def __init__(self, deck):
        self.hand: list = []
        self.sum = 0

    def newCard(self, deck):
        card = deck.getDeck[0]
        self.hand.append(card)
        


        # self.hand.append(deck.drawCard)
        # The dealer give cards in between 
        # self.hand.append(deck.drawCard())

        # self.sum = 0 
        # for card in self.hand:
        #     self.sum += card



## Testing ##        
# deck = CardDeck()
# p = Player(deck)

#
# print(f"Deck: {deck.deck} \n\n Player card: {p.hand} \n\n Player sum: {p.sum}")
#
# for card in deck.deck:
#     if p.hand == card:
#         print(f"Error - duplicate cards")
