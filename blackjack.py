from blackjackclasses import Card, CardDeck, Player

## Main game loop ##
def blackjackGame():
     
    deck = CardDeck() 
    print(deck.getDeck())

    dealer = Player()
    dealer.newCard(deck)
    dealerVisible = dealer.sum
    dealer.newCard(deck)
    print(f"DEALER: {dealer.hand}, {dealer.sum} ({dealerVisible})")

    player = Player()
    player.newCard(deck)
    player.newCard(deck)
    print(f"PLAYER: {player.hand}, {player.sum}")

    while player.sum <= 21:
        choice = input(f"(H) Hit \n(S) Stand \n(D) Double Down \n(SP) Split Pairs \n")
        match choice:
            case "H":
                print("You choose to hit!")
                player.newCard(deck)
                print(f"DEALER: {dealer.hand}, {dealer.sum} ({dealerVisible})")
                print(f"PLAYER: {player.hand}, {player.sum}")

                if (player.sum == 21):
                    print(f"BLACKJACK! Player wins, house loses.")

                elif (player.sum > 21):
                    print(f"PLAYER busts: {player.sum}\n The house wins, player loses.")

            case "S":
                print("You choose to stand!")
                print(f"Dealer reveal hidden card: {dealer.hand}, {dealer.sum}")
                
                while dealer.sum <= 16:
                    dealer.newCard(deck)
                    print(f"DEALER: {dealer.hand}, {dealer.sum}")

                if (dealer.sum > 21):
                    print(f"DEALER busts: {dealer.sum}\nPlayer wins, house loses.")
                    break

                elif (dealer.sum > player.sum):
                    print(f"!The house wins, player loses.")
                    break

                elif (dealer.sum == player.sum):
                    print(f"Tie, players bet gets returned.")
                    break
                
                elif (dealer.sum < player.sum):
                    print(f"Player wins, house loses.")
                    break



            case "D":
                print("You choose to Double Down!")

            case "SP":     
                print("You choose to Split Pairs!")



blackjackGame()




