# This works, but is there a better way?

class gameState:
    def __init__(self, PlayerTotal: int, DealerTotal):
        self.playerTotal = PlayerTotal
        self.dealerTotal = DealerTotal
        
    
    def __str__(self):
        return f"Player: {self.playerTotal} \nDealer: {self.dealerTotal} \n"

    def get(self):
        return (self.playerTotal, self.dealerTotal) 

    def bestMove(self):
        # Look up in the best move tables, and retun H,S,SP, or DD?
        pass
    

state = gameState(8,2)

print(state.get() == (8,3))
# TODO: Correct to just use 1 for Ace here? 
hardTotals = {(17,2) : "S", (17,3) : "S", (17,4): "S", (17,5): "S", (17,6): "S", (17,7): "S", (17,8): "S", (17,9): "S", (17,10): "S", (17,1): "S",
              (16,2) : "S", (16,3) : "S", (16,4) : "S", (16,5) : "S", (16,6) : "S", (16,7) : "H", (16,8) : "H", (16,9) : "H", (16,10) : "H", (16,1) : "H",
              (15,2) : "S", (15,3) : "S", (15,4) : "S", (15,5) : "S", (15,6) : "S", (15,7) : "H", (15,8) : "H", (15,9) : "H", (15,10) : "H", (15,1) : "H",                     
               
   # Just keep typing... 
    }

print(f"{hardTotals[(8,2)]}")