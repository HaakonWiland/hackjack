import random

possibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
possibleSuits = ["diamonds", "hearts", "spades", "clubs"]

class Card:
    def __init__(self, Value, Suit):
        self.value = Value
        self.suit = Suit


# TODO: We want value and suit to only have "value" and "suit" as possible values


class CardDeck:
    def __init__(self):

        cardDeck: list[tuple] = []

        for v in possibleValues:
            for s in possibleSuits:
                card: tuple = (v, s)
                cardDeck.append(card)

        self.deck = cardDeck
        self.shuffle()

        ## Debug functions ##
        self.length = len(cardDeck)

    # TODO: This has do shuffle good, find optimal way later.
    def shuffle(self):
        randomValue = 0
        # shuffledDeck = []

        for card in range(len(self.deck)):

            ## This is wrong, get decks with 5 11's
            randomValue: int = random.randint(0, 10000)
            index: int = (randomValue) % 43
                
            self.deck[card], self.deck[index] = self.deck[index], self.deck[card]

            # shuffledDeck.append(self.deck[index])
            ##

        # self.deck = shuffledDeck

    def drawCard(self):
        card = self.deck[0]
        self.deck = self.deck[1:]

        return card


class Player:
    def __init__(self, deck):
        self.hand: list = []
        self.hand.append(deck.drawCard())
        # The dealer give cards in between 
        # self.hand.append(deck.drawCard())

        self.sum = 0 
        for card in self.hand:
           self.sum += card[0]

## Testing ##        
# deck = CardDeck()
# p = Player(deck)
#
#
# print(f"Deck: {deck.deck} \n\n Player card: {p.hand} \n\n Player sum: {p.sum}")
#
# for card in deck.deck:
#     if p.hand == card:
#         print(f"Error - duplicate cards")
