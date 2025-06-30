import random

possibleValues = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
possibleSuits = ["diamonds", "hearts", "spades", "clubs"]

class Card:
    def __init__(self, Value: str, Suit: str):
        self.suit = Suit
        if Value in ("jack", "queen", "king"):
            self.value = 10
            self.valueStr = Value
            self.ace = False

        elif Value == "ace":
            self.value = 11
            self.valueStr = Value
            self.ace = True
        
        else:
            self.value = int(Value)
            self.valueStr = Value
            self.ace = False
    
    def __str__(self):
        return f"{self.valueStr} of {self.suit}"

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
        
        # print(f"Carddeck length: {len(self.cardDeck)}")

        assert len(self.cardDeck) == 52, "Deck needs to have 52 cards."

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
        self.blackjack = False

    def newCard(self, deck):
        card = deck.drawCard()
        self.hand.append(card)

        # For the natural blackjack. 
        if card.ace == True and (self.sum + card.value) == 21:
            self.blackjack = True

        elif card.ace == True and (self.sum + card.value) > 21:
            self.sum += 1 
        else:
            self.sum += card.value

        

