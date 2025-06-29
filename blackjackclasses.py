import random

#TODO: We want to fix this such that we have a carddeck with 52 card, else probabilities are messed up.
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


    # TODO: This has to shuffle good, find optimal way later, currently use Fisher-Yates Shuffle
    def shuffle(self):
        
        for i in range(len(self.cardDeck)-1, 0, -1):
            j: int = random.randint(0, i)
            self.cardDeck[i], self.cardDeck[j] = self.cardDeck[j], self.cardDeck[i]


    def drawCard(self):
        card = self.cardDeck[0]
        self.cardDeck = self.cardDeck[1:] 

        return card


class Player:
    def __init__(self):
        self.hand: list = []
        self.sum = 0

    def newCard(self, deck):
        card = deck.drawCard()
        self.hand.append(card)
        self.sum += card.value

        


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
