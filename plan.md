Blackjack:

Goal: 
- Simulate a blackjack game with basic stategy 
- Display probabilities for the house/player to win in a given state

Possible functionalities:
- Simulate random playing bot vs a basic stategy bot 
- Given that we know the state of the deck, how can we use this to improve our probabilties of winning 
- Simulator game which trains a person into memorising basic stategy (?) 

What do we need:
- Some object keping track of the basic stategy(just do dict, with function?)
- Functions to compute probabilities in a given state 
- Cool Ascii art for the game 

- Web interface where a user can plot in the state of a game, then get the basic strategy answer back from it 

How to structure the basic strategy? 
- To decide what to do, we need the players hand and the dealers hand. 
- Can do a dict, with "state" and "basic choice"
- Total possible hands (excluding different suits) 13c2= 78 combination 
- Dealer can have 10 different first cards, giving us 78*10=780 different states. 
- Basic strategy displays 280 explisit choices, many states are "the same", ex. 5+3=8 and 2+6=8, the hard total is 8 in both cases. 
- Can sort in 3 categories: Hard totals(no Ace or pair), soft totals (Got an ace), and Pairs. Make nested dict or table for each of them. 
- Then take all cases which are "hard totals", and sum <= 8, as hit? 