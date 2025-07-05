# This works, but is there a better way?

class gameState:
    def __init__(self, PlayerTotal: int, DealerTotal: int, PlayerAce: int):
        self.playerTotal = PlayerTotal
        self.dealerTotal = DealerTotal
        self.state = (self.playerTotal, self.dealerTotal)
        self.playerAce = PlayerAce
        
    
    def __str__(self):
        return f"Player: {self.playerTotal} \nDealer: {self.dealerTotal} \n"

    def get(self):
        return self.state

    def getPlayer(self):
        return self.state[0] 

    def bestMove(self):
        choice = ""

        #TODO: If player got pairs, use pair splittig 
        #TODO: If player got ace, use soft totals
        if self.playerAce == True:
            choice = softTotals[self.state]

        elif self.state[0] < 8:
            choice = "H"
        elif self.state[0] > 17:
            choice = "S"
        else: 
            choice = hardTotals[self.state]
        
        return choice
    

state = gameState(8,2, False)

# print(state.get() == (8,3))
# TODO: Correct to just use 1 for Ace here? 

hardTotals = {(17,2) : "S", (17,3) : "S", (17,4): "S", (17,5): "S", (17,6): "S", (17,7): "S", (17,8): "S", (17,9): "S", (17,10): "S", (17,1): "S",
              (16,2) : "S", (16,3) : "S", (16,4) : "S", (16,5) : "S", (16,6) : "S", (16,7) : "H", (16,8) : "H", (16,9) : "H", (16,10) : "H", (16,1) : "H",
              (15,2) : "S", (15,3) : "S", (15,4) : "S", (15,5) : "S", (15,6) : "S", (15,7) : "H", (15,8) : "H", (15,9) : "H", (15,10) : "H", (15,1) : "H",
              (14,2) : "S", (14,3) : "S", (14,4) : "S", (14,5) : "S", (14,6) : "S", (14,7) : "H", (14,8) : "H", (14,9) : "H", (14,10) : "H", (14,1) : "H",
              (13,2) : "S", (13,3) : "S", (13,4) : "S", (13,5) : "S", (13,6) : "S", (13,7) : "H", (13,8) : "H", (13,9) : "H", (13,10) : "H", (13,1) : "H",
              (12,2) : "H", (12,3) : "H", (12,4) : "S", (12,5) : "S", (12,6) : "S", (12,7) : "H", (12,8) : "H", (12,9) : "H", (12,10) : "H", (12,1) : "H",
              (11,2) : "D", (11,3) : "D", (11,4) : "D", (11,5) : "D", (11,6) : "D", (11,7) : "D", (11,8) : "D", (11,9) : "D", (11,10) : "D", (11,1) : "D",
              (10,2) : "D", (10,3) : "D", (10,4) : "D", (10,5) : "D", (10,6) : "D", (10,7) : "D", (10,8) : "D", (10,9) : "D", (10,10) : "H", (10,1) : "H",
              (9,2) : "H", (9,3) : "D", (9,4) : "D", (9,5) : "D", (9,6) : "D", (9,7) : "H", (9,8) : "H", (9,9) : "H", (9,10) : "H", (9,1) : "H",
              (8,2) : "H", (8,3) : "H", (8,4) : "H", (8,5) : "H", (8,6) : "H", (8,7) : "H", (8,8) : "H", (8,9) : "H", (8,10) : "H", (8,1) : "H"                    
}

#TODO: How to handle these, have to read the hand of the player - how should it be represented? 
# Can do .hasAce() == True, then just represent with the (Ace + other_card, dealers_sum)
# Example: (10,2) means the player has Ace and a 9.  
softTotals = {(10,2) : "S", (10,3) : "S", (10,4) : "S", (10,5) : "S", (10,6) : "S", (10,7) : "S", (10,8) : "S", (10,9) : "S", (10,10) : "S", (10,1) : "S",
               (9,2) : "S", (9,3) : "S", (9,4) : "S", (9,5) : "S", (9,6) : "D", (9,7) : "S", (9,8) : "S", (9,9) : "S", (9,10) : "S", (9,1) : "S",
               (8,2) : "D", (8,3) : "D", (8,4) : "D", (8,5) : "D", (8,6) : "D", (8,7) : "S", (8,8) : "S", (8,9) : "H", (8,10) : "H", (8,1) : "H",
               (7,2) : "H", (7,3) : "D", (7,4) : "D", (7,5) : "D", (7,6) : "D", (7,7) : "H", (7,8) : "H", (7,9) : "H", (7,10) : "H", (7,1) : "H",
               (6,2) : "H", (6,3) : "H", (6,4) : "D", (6,5) : "D", (6,6) : "D", (6,7) : "H", (6,8) : "H", (6,9) : "H", (6,10) : "H", (6,1) : "H",
               (5,2) : "H", (5,3) : "H", (5,4) : "D", (5,5) : "D", (5,6) : "D", (5,7) : "H", (5,8) : "H", (5,9) : "H", (5,10) : "H", (5,1) : "H",
               (4,2) : "H", (4,3) : "H", (4,4) : "H", (4,5) : "D", (4,6) : "D", (4,7) : "H", (4,8) : "H", (4,9) : "H", (4,10) : "H", (4,1) : "H",
               (3,2) : "H", (3,3) : "H", (3,4) : "H", (3,5) : "D", (3,6) : "D", (3,7) : "H", (3,8) : "H", (3,9) : "H", (3,10) : "H", (3,1) : "H"
}

pairSplitting = {}




# print(state.getPlayer())
# # print(f"{hardTotals[(11,3)]}")