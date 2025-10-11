from flask import Flask, render_template, request, session, url_for
from blackjackclasses import CardDeck, Player, Card
from basicStrategy import gameState

app = Flask(__name__)
app.secret_key = "1234" #TODO: Change this.

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


@app.route("/", methods=["GET", "POST"])
def index(name=None):
    if "deck" not in session:
        init_game()

    deck = CardDeck.deserialize(session["deck"])
    # dealer = Player.deserialize(session["dealer"])
    # player = Player.deserialize(session["player"])





    return render_template("index.html", person="haakon")