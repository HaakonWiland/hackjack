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

    def serialize(self):
        return {"value": self.value, "suit": self.suit}
    
    @classmethod
    def deserialize(cls, card_data: dict):
        return cls(card_data["value"], card_data["suit"])

    def image_filename(self):
        return f"{self.valueStr}_of_{self.suit}.png"

# TODO: We want value and suit to only have "value" and "suit" as possible values


class CardDeck:
    def __init__(self, CardDeck=None):
        if CardDeck == None: 
            self.cardDeck: list[tuple] = []

            for v in possibleValues:
                for s in possibleSuits:
                    card: tuple = Card(v, s)
                    self.cardDeck.append(card)
            
            # print(f"Carddeck length: {len(self.cardDeck)}")

            assert len(self.cardDeck) == 52, "Deck needs to have 52 cards."

            self.shuffle()
        
        else:
            self.cardDeck = CardDeck


    def serialize(self):
        return {"deck": [card.serialize() for card in self.cardDeck]}

    @classmethod
    def deserialize(cls, cardDeck_data):
        cardDeck_reconstruct: list[tuple] = []
        
        # A list of dicts, where each dict represents a card 
        cardDeck_list = cardDeck_data["deck"]

        for card_dict in cardDeck_list:
            card = Card(card_dict["value"], card_dict["suit"])
            cardDeck_reconstruct.append(card)

        return cls(cardDeck_reconstruct)

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
    def __init__(self, hand=None, sum_=0, blackjack=False, hasAce=False, softTotalPossible=True):
        self.hand = hand if hand is not None else []
        self.sum = sum_
        self.blackjack = blackjack
        self.hasAce = hasAce
        self.softTotalPossible = softTotalPossible
    
    def serialize(self):
        return {
            "hand": [card.serialize() for card in self.hand],
            "sum": self.sum,
            "blackjack": self.blackjack,
            "hasAce": self.hasAce,
            "softTotalPossible": self.softTotalPossible
        }
    
    @classmethod
    def deserialize(cls, player_data):
        hand = [Card.deserialize(c) for c in player_data["hand"]]
        return cls(
            hand=hand,
            sum_=player_data["sum"],
            blackjack=player_data["blackjack"],
            hasAce=player_data["hasAce"],
            softTotalPossible=player_data["softTotalPossible"]     
        )
    

    def computeSum(self):
        newSum: int = 0

        if self.hasAce == False:
            for card in self.hand:
                newSum += card.value
        
        elif self.hasAce == True:
            for card in self.hand:
                newSum += card.value

            if newSum > 21:
                newSum -= 10 
                self.softTotalPossible = False 

        self.sum = newSum

    def newCard(self, deck):
        card = deck.drawCard()
        self.hand.append(card)

        if card.ace == True:
            self.hasAce = True

        # For the natural blackjack. 
        if card.ace == True and (self.sum + card.value) == 21:
            self.sum += card.value
            self.blackjack = True
        
        else:
            self.computeSum()
    

    # For debugging
    def appendCard(self, card: Card):
        self.hand.append(card)

        if card.ace == True:
            self.hasAce = True

        # For the natural blackjack. 
        if card.ace == True and (self.sum + card.value) == 21:
            self.sum += card.value
            self.blackjack = True
        
        else:
            self.computeSum()

