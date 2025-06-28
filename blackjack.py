from blackjackclasses import Card, CardDeck, Player

## Main game loop ##
def blackjackGame():
     
    deck = CardDeck() 
    print(deck.getDeck())

    card = deck.drawCard()
    print(f"card : {card}")
    
    # dealer = Player(deck)
    # dealer.newCard 
    # print(f"Dealer hand: {dealer.hand}")



blackjackGame()




