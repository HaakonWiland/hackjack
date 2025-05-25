import random 

possibleValues = [1,2,3,4,5,6,7,8,9,10,11]
possibleSuits = ["Diamonds", "Hearts", "Spades", "Clubs"]

class card:
    def __init__(self, Value, Suit):
        self.value=Value
        self.suit=Suit

    
#TODO: We want value and suit to only have "value" and "suit" as possible values 

class CardDeck:
    def __init__(self):

        cardDeck: list[tuple] = []

        for v in possibleValues:
            for s in possibleSuits:
                card: tuple = (v, s)
                cardDeck.append(card)
        
        self.deck = cardDeck
        # self.shuffle()
    
        ## Debug functions ## 
        self.length = len(cardDeck)

    #TODO: This has do shuffle good, find optimal way later.
    def shuffle(self):
        randomValue = 0
        shuffledDeck = []
        
        for card in range(len(self.deck)):
            

            ## This is wrong, get decks with 5 11's 
            randomValue: int = random.randint(0,10000)
            index: int = (randomValue) % 43
             
            shuffledDeck.append(self.deck[index])
            ## 

        self.deck = shuffledDeck

    def drawCard(self):
        card = self.deck[0]
        self.deck = self.deck[1:]

        return card 

class Player:
    def __init__(self, deck):
        self.hand = deck.drawCard()
         



    
# c = card(1,"clubs")
deck = CardDeck()
p = Player(deck)





print(f"Deck: {deck.deck} \n\n Player card: {p.hand}")
