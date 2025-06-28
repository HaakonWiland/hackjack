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
        choice = input(f"(H) Hit \n(S) Stand \n(D) Double Down \n(SP) Split Pairs \n(Q) Quit\n")
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
                if (player.hand[0] != player.hand[1]):
                    print(f"You do not have equal values, you can not split!")

                print("You choose to Split Pairs! Your hand has been split into two different bets.")
                hand1, hand2 = player.hand[0], player.hand[1]
                hand1Sum, hand2Sum = player.hand[0].value , player.hand[1].value 



                #TODO: Setup here is very hard, might want to rewrite and structure it differently.
                ####
                while hand1Sum <= 21:
                    print("1. hand, what do you want to do?")
                    choice = input(f"(H) Hit \n(S) Stand \n")

                    match choice:

                        case "H":
                           newCard = deck.drawCard()
                           hand1.append(newCard)
                           hand1Sum += newCard.value

                           print(f"You drew {newCard}, new 1.hand: {hand1}, {hand1Sum}")

                           if (hand1Sum == 21):
                               print(f"BLACKJACK! PLAYER hand1 wins, house loses.")
                               hand1Done = True
                               break

                           elif (hand1Sum > 21):
                               print(f"PLAYER hand1 busts, the house wins, player loses.")
                               hand1Done = True 
                               break

                        case "S":
                            print(f"You chose to stand with 1.hand, now decide for the 2.hand.")

                while hand2Sum <= 21:
                    print(f"2.hand, what do you want to do?")
                    choice = input(f"(H) Hit \n(S) Stand \n")

                    match choice:

                        case "H":
                           newCard = deck.drawCard()
                           hand2.append(newCard)
                           hand2Sum += newCard.value

                           print(f"You drew {newCard}, new 2.hand: {hand2}, {hand2Sum}")  
                           
                           if (hand2Sum == 21):
                               print(f"BLACKJACK! PLAYER 2.hand wins, house loses.")
                               hand2Done = True
                               break

                           elif (hand2Sum > 21):
                               print(f"PLAYER 2.hand busts, the house wins, player loses.")
                               hand2Done = True
                               break  

                        case "S":
                            print(f"You chose to stand with 2.hand.")

                while dealer.sum <= 16 and (not hand1Done or not hand2Done):
                    print(f"PLAYER: hand1: {hand1Sum}, hand2: {hand2Sum}")
                    dealer.newCard(deck)
                    print(f"DEALER: {dealer.hand}, {dealer.sum}")

                if (dealer.sum == 21):
                    print(f"The house wins, player lose both hands.")

                elif (dealer.sum > 21):
                    print(f"DEALER busts, player wins both hands.")

                ### 

            case "Q":
                print(f"You choose to quit.")
                break




blackjackGame()




