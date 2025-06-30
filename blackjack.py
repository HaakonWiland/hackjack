from blackjackclasses import Card, CardDeck, Player

def playHand(deck : CardDeck, handDir, dealer: Player): 
    while not handDir["done"] and handDir["sum"] <= 21:
        print(f"DEALER: {dealer.hand[0]}, {dealer.hand[0].value}\n")
        print(f"What do you want to do?\n")
        choice = input("(H) Hit \n(S) Stand\n")

        match choice:
            case "H":
                card = deck.drawCard()
                handDir["cards"].append(card)
                handDir["sum"] += card.value
                print(f"You draw {card}, new hand: {handDir["cards"]}, new sum: {handDir["sum"]}\n")

                if handDir["sum"] == 21:
                    print(f"BLACKJACK! player wins, house loses.")
                    handDir["done"] = True
                elif handDir["sum"] > 21:
                    print(f"Player busts, house wins.")
                    handDir["done"] = True

            case "S":
                print(f"Player chose to stand.")
                handDir["done"] = True

def playDealer(deck: CardDeck, dealer: Player):
    while dealer.sum <= 16:
        dealer.newCard(deck)
        print(f"DEALERS new hand: {dealer.hand}, {dealer.sum}")

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

    # handDir = {"cards": player.hand, "sum": player.sum, "done": False}

    # TODO: Fix gameloop by using the playHand and playDealer function.
    while player.sum <= 21:

        if player.blackjack == True and dealer.sum != 21:
            print(f"Natural blackjack! You are rewarded based on 3:2 odds.")
            break 

        elif player.blackjack == True and dealer.sum == 21:
            print(f"Both dealer and player got natural blackjack, its a push (tie).")
            break

        choice = input(f"(H) Hit \n(S) Stand \n(D) Double Down \n(SP) Split Pairs \n(Q) Quit\n").upper()

        match choice:
            case "H":
                print("You choose to hit!")
                player.newCard(deck)
                print(f"DEALER: {dealer.hand}, {dealer.sum} ({dealerVisible})")
                print(f"PLAYER: {player.hand}, {player.sum}")

                if (player.sum == 21):
                    print(f"BLACKJACK! Player wins, house loses.")
                    break

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
                    print(f"The house wins, player loses.")
                    break

                elif (dealer.sum == player.sum):
                    print(f"Tie, players bet gets returned.")
                    break
                
                elif (dealer.sum < player.sum):
                    print(f"Player wins, house loses.")
                    break


            case "D":
                print("You choose to Double Down!\n")
                print(f"You inital bet has be doubled.")

                player.newCard(deck)
                print(f"PLAYER: {player.hand}, {player.sum}")

                #TODO: After double and newcard, its the same flow as (S). 
                #Fix such that we dont have to repeat code.

                print(f"Dealer reveal hidden card: {dealer.hand}, {dealer.sum}")
                
                while dealer.sum <= 16:
                    dealer.newCard(deck)
                    print(f"DEALER: {dealer.hand}, {dealer.sum}")

                if (dealer.sum > 21):
                    print(f"DEALER busts: {dealer.sum}\nPlayer wins, house loses.")
                    break

                elif (dealer.sum > player.sum):
                    print(f"The house wins, player loses.")
                    break

                elif (dealer.sum == player.sum):
                    print(f"Tie, players bet gets returned.")
                    break
                
                elif (dealer.sum < player.sum):
                    print(f"Player wins, house loses.")
                    break

            case "SP":     
                if (player.hand[0].value != player.hand[1].value):
                    print(f"You do not have equal values, you can not split!")
                    continue

                print("You choose to Split Pairs! Your hand has been split into two different bets.")

                splitHands = [
                    {"cards": [player.hand[0]], "sum": player.hand[0].value, "done": False},
                    {"cards": [player.hand[1]], "sum": player.hand[1].value, "done": False},
                ]

                # Play both hands 
                for i, hand in enumerate(splitHands):
                    print(f"Playing hand {i+1}:\n")
                    playHand(deck, handDir=hand, dealer=dealer)

                # Play the dealer 
                playDealer(deck, dealer)


                for i, hand in enumerate(splitHands):
                    print(f"Result for hand {i+1}")
                    ## TODO: Do we need this first condition, we check it in playHand?
                    if hand["sum"] > 21:
                        print("Player busts, house wins.")
                    
                    elif dealer.sum > 21 or hand["sum"] > dealer.sum:
                        print("Player wins.")
                    
                    elif hand["sum"] == dealer.sum:
                        print("Push (tie - player gets his bet back).")

                    else: 
                        print("Dealer wins.")
            
                break 
                    
                
            case "Q":
                print(f"You choose to quit.")
                break

            case _:
                print(f"Invalid input.")


blackjackGame()




