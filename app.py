from flask import Flask, render_template, request, session, url_for, redirect
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


    #TODO: Create state object and save it into the session. 
    gameState = GameState(player.sum, dealer.sum, player.hasAce, player.hand, True, True)


    # Dicts represetning the object data 
    save_session(deck, dealer, player, gameState) 


    # session["deck"] = deck.serialize()
    # session["dealer"] = dealer.serialize()
    # session["player"] = player.serialize()



@app.route("/", methods=["GET", "POST"])
def index(name=None):
    # Make sure we have all components needed to play a game. 
    # if not all(k in session for k in ("deck", "dealer", "player", "gameState")):
    #     init_game()

    if request.method == "GET":
        init_game()



    deck, dealer, player, gameState = load_session()


    message = f"Ready to play blackjack (Gamestate: {gameState.gameAlive})"
    game_message = ""

    if player.sum <= 21: 

        if player.blackjack == True and dealer.sum != 21:
            game_message = "Natural blackjack! You are rewarded based on 3:2 odds."

            #TODO: Add break functionality 

        elif player.blackjack == True and dealer.sum == 21:
            game_message = "Both dealer and player got natural blackjack, its a push (tie)."
            #TODO: Add break functionality 

      

    if request.method == "POST":
        action = request.form.get("action")

        match action: 

            case "hit":
                player.newCard(deck)
                
                if (player.sum == 21):
                    game_message = "BLACKJACK! Player wins, house loses."
                    gameState.gameAlive = False
                
                elif (player.sum > 21):
                    game_message = f"Player busts: {player.sum}, house wins, player loses."
                    gameState.gameAlive = False
                
            
            case "stand":
                pass

            case "double":
                pass

            case "split pair":
                pass
            case "reset":
                init_game()
                return redirect(url_for("index"))

        # Save the changes from last action 
        # TODO: Clean this stuff up. 
        session["deck"] = deck.serialize()
        session["dealer"] = dealer.serialize()
        session["player"] = player.serialize()
        session["gameState"] = gameState.serialize()  
        session["game_message"] = game_message

        return render_template(
            "index.html",
            player=player,
            dealer=dealer,
            message=message,
            game_message=game_message
        )     
           
            
    return render_template(
        "index.html",
        player=player,
        dealer=dealer,
        message=message,
        game_message=game_message
    )

