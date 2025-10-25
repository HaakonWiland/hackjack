from flask import Flask, render_template, request, session, url_for, redirect, jsonify 
from blackjackclasses import CardDeck, Player, Card
from basicStrategy import GameState

app = Flask(__name__)
app.secret_key = "1234" #TODO: Change this.


def save_session(deck, dealer, player, gameState):
    session["deck"] = deck.serialize()
    session["dealer"] = dealer.serialize()
    session["player"] = player.serialize()
    session["gameState"] = gameState.serialize()


def load_session():
    deck = CardDeck.deserialize(session["deck"])
    dealer = Player.deserialize(session["dealer"])
    player = Player.deserialize(session["player"])
    gameState = GameState.deserialize(session["gameState"])

    return deck, dealer, player, gameState


def init_game():
    deck = CardDeck()
    dealer = Player()
    player = Player()

    dealer.newCard(deck)
    dealer.newCard(deck)
    player.newCard(deck)
    player.newCard(deck)
    # player.appendCard(Card("2", "diamonds"))
    # player.appendCard(Card("2", "hearts"))

    gameState = GameState(player.sum, dealer.sum, player.hasAce, player.hand, True, True)


    # Dicts represetning the object data 
    save_session(deck, dealer, player, gameState) 


@app.route("/", methods=["GET"])
def index():
    # Always start a new game on reload
    init_game()

    deck, dealer, player, gameState = load_session()
    game_message = f"Ready to play blackjack (Gamestate: {gameState.gameAlive})" 

    #TODO: Handle natural blackjack and natural tie -> Do not work atm.  
    if player.blackjack == True and dealer.sum != 21:
        game_message = "Natural blackjack! You are rewarded based on 3:2 odds."
        gameState.gameAlive = False 

    elif player.blackjack == True and dealer.sum == 21:
        game_message = "Both dealer and player got natural blackjack, its a push (tie)."
        gameState.gameAlive = False 

    return render_template(
        "index.html",
        player=player,
        dealer=dealer,
        message=game_message,
        gameState=gameState,
    )

@app.route("/action", methods=["POST"])
def handle_action():
    data = request.get_json()
    action = data.get("action")

    deck, dealer, player, gameState = load_session()
    # Do not allow to play after game has ended. 
    if gameState.gameAlive == False and action != "reset":

        game_message = "Game has ended, hit the 'Reset Game' button"

        return jsonify({
        "player": player.serialize(),
        "dealer": dealer.serialize(),
        "split": False,
        "game_message": game_message,
        "gameState": gameState.serialize(),
        "gameAlive": gameState.gameAlive
    })

    game_message = ""

    match action:
        case "hit":
            player.newCard(deck)
            if player.sum == 21:
                game_message = "BLACKJACK! Player wins, house loses."
                gameState.gameAlive = False

            elif player.sum > 21:
                game_message = f"Player busts ({player.sum}), house wins."
                gameState.gameAlive = False

        case "stand":
            while dealer.sum <= 16:
                dealer.newCard(deck)

            if dealer.sum > 21:
                game_message = f"Dealer busts ({dealer.sum}), player wins."
                gameState.gameAlive = False

            elif dealer.sum > player.sum:
                game_message = "Dealer wins."
                gameState.gameAlive = False

            elif dealer.sum < player.sum:
                game_message = "Player wins!"
                gameState.gameAlive = False
       
            else:
                game_message = "Push (tie)."
                gameState.gameAlive = False

            gameState.gameAlive = False
        
        case "double":
            player.newCard(deck)
            
            if player.sum > 21:
                game_message = f"Player busts, Dealer wins."
                gameState.gameAlive = False

                # Return so we exit the block
                return jsonify({
                    "player": player.serialize(),
                    "dealer": dealer.serialize(),
                    "split": False,
                    "game_message": game_message,
                    "gameState": gameState.serialize(),
                    "gameAlive": gameState.gameAlive
                })

            while dealer.sum <= 16:
                dealer.newCard(deck)

            if dealer.sum > 21:
                game_message = f"DEALER busts: {dealer.sum}\nPlayer wins, house loses."
                gameState.gameAlive = False

            elif dealer.sum > player.sum:
                game_message = f"The house wins, player loses."
                gameState.gameAlive = False
                
            elif dealer.sum == player.sum:
                game_message = f"Tie, players bet gets returned."
                gameState.gameAlive = False
            
            elif (dealer.sum < player.sum):
                game_message = f"Player wins, house loses."
                gameState.gameAlive = False 
                  

        case "split":
            # Should only be possible if we got pair. 
            if player.hand[0].value != player.hand[1].value:
                game_message = "You do not have equal values, you can not split!"
                return jsonify({
                    "player": player.serialize(),
                    "dealer": dealer.serialize(),
                    "split": False, 
                    "game_message": game_message,
                    "gameState": gameState.serialize(),
                    "gameAlive": gameState.gameAlive
                })

            splitHands = [
                {"cards": [player.hand[0]], "sum": player.hand[0].value, "done": False},
                {"cards": [player.hand[1]], "sum": player.hand[1].value, "done": False},
            ]

            # TODO: prob. not the optimal structure for return data. 
            return jsonify({
                "player": player.serialize(),
                "dealer": dealer.serialize(),
                "split": True,
                "split_cards": [
                    {"filename": player.hand[0].image_filename},
                    {"filename": player.hand[1].image_filename}
                ],
                "game_message": game_message,
                "gameAlive": gameState.gameAlive
            })

            #TODO: Need some animation to visually split up the pairs. 
            #TODO: Then we need to have some functions that play a hand, and play the dealer. 
            pass 

        case "reset":
            init_game()
            deck, dealer, player, gameState = load_session()
            game_message = "New game started."

    save_session(deck, dealer, player, gameState)

    #TODO: Should send in gameState aswell, and do stuff with it. 
    return jsonify({
        "player": player.serialize(),
        "dealer": dealer.serialize(),
        "split": False,
        "game_message": game_message,
        "gameState": gameState.serialize(),
        "gameAlive": gameState.gameAlive
    })


