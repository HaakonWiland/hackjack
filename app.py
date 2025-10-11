from flask import Flask, render_template, request, session, url_for, redirect
from blackjackclasses import CardDeck, Player, Card
from basicStrategy import gameState

app = Flask(__name__)
app.secret_key = "1234" #TODO: Change this.


def save_session():
    session["deck"] = deck.serialize()
    session["dealer"] = dealer.serialize()
    session["player"] = player.serialize()


def load_session():
    deck = CardDeck.deserialize(session["deck"])
    dealer = Player.deserialize(session["dealer"])
    player = Player.deserialize(session["player"])

    return deck, dealer, player


def init_game():
    deck = CardDeck()
    dealer = Player()
    player = Player()

    dealer.newCard(deck)
    dealer.newCard(deck)
    player.newCard(deck)
    player.newCard(deck)

    # Dicts represetning the object data 
    session["deck"] = deck.serialize()
    session["dealer"] = dealer.serialize()
    session["player"] = player.serialize()
    save_session() 


@app.route("/", methods=["GET", "POST"])
def index(name=None):
    if "deck" not in session:
        init_game()

    # deck, dealer, player = load_session()

    deck = CardDeck.deserialize(session["deck"])
    dealer = Player.deserialize(session["dealer"])
    player = Player.deserialize(session["player"])

    message = "Ready to play blackjack"
    game_message = ""

    if player.sum <= 21: 

        if player.blackjack == True and dealer.sum != 21:
            game_message = "Natural blackjack! You are rewarded based on 3:2 odds."

      

    if request.method == "POST":
        action = request.form.get("action")

        match action: 

            case "hit":
                # print("hit")
                pass
            
            case "stand":
                pass

            case "double":
                pass

            case "split pair":
                pass

        # Save the changes from last action 
        session["deck"] = deck.serialize()
        session["dealer"] = dealer.serialize()
        session["player"] = player.serialize()  
        return redirect(url_for("index"))        
    

    return render_template(
        "index.html",
        player=player,
        dealer=dealer,
        message=message
    )