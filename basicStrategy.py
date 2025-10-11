# This works, but is there a better way?

class gameState:
    def __init__(self, 
    PlayerTotal: int, 
    DealerTotal: int, 
    PlayerAce: bool, 
    PlayerHand : list, 
    SoftTotalPossible: bool,
    GameAlive: bool = True):

        self.playerTotal = PlayerTotal
        self.dealerTotal = DealerTotal
        self.state = (self.playerTotal, self.dealerTotal)
        self.playerAce = PlayerAce
        self.playerHand = PlayerHand
        self.softTotalPossible = SoftTotalPossible 
        self.gameAlive = GameAlive # This overrides the default value? 

    # TODO: 
    def serialize():
        pass 
    
    # TODO: 
    def deserialize():
        pass 
        
    def __str__(self):
        return f"Player: {self.playerTotal} \nDealer: {self.dealerTotal} \n"

    def get(self):
        return self.state

    def getPlayer(self):
        return self.state[0] 

    def bestMove(self):
        choice = ""

        # Split pairs: 
        if self.playerHand[0].value == self.playerHand[1].value:
            choice = pairSplitting[(self.playerHand[0].value, self.dealerTotal)] 

        # Soft total: 
        if self.playerAce == True and self.softTotalPossible == True:
            self.modifiedState = (self.playerTotal - 10, self.dealerTotal)
            choice = softTotals[self.modifiedState] 
        
        # Hard totals:
        elif self.state[0] < 8:
            choice = "H"
        elif self.state[0] > 17:
            choice = "S"
        else: 
            choice = hardTotals[self.state]
        
        return choice
    
# TODO: Correct to just use 1 for Ace here -> Got some edge case errors, when the dealer had ace as visible card 
# fix: Just add entries for both 1 and 11, with the same choices?

hardTotals = {(17,2) : "S", (17,3) : "S", (17,4): "S", (17,5): "S", (17,6): "S", (17,7): "S", (17,8): "S", (17,9): "S", (17,10): "S", (17,1): "S", (17, 11) : "S",
              (16,2) : "S", (16,3) : "S", (16,4) : "S", (16,5) : "S", (16,6) : "S", (16,7) : "H", (16,8) : "H", (16,9) : "H", (16,10) : "H", (16,1) : "H", (16,11) : "H",
              (15,2) : "S", (15,3) : "S", (15,4) : "S", (15,5) : "S", (15,6) : "S", (15,7) : "H", (15,8) : "H", (15,9) : "H", (15,10) : "H", (15,1) : "H", (15,11) : "H",
              (14,2) : "S", (14,3) : "S", (14,4) : "S", (14,5) : "S", (14,6) : "S", (14,7) : "H", (14,8) : "H", (14,9) : "H", (14,10) : "H", (14,1) : "H", (14,11) : "H",
              (13,2) : "S", (13,3) : "S", (13,4) : "S", (13,5) : "S", (13,6) : "S", (13,7) : "H", (13,8) : "H", (13,9) : "H", (13,10) : "H", (13,1) : "H", (14,11) : "H",
              (12,2) : "H", (12,3) : "H", (12,4) : "S", (12,5) : "S", (12,6) : "S", (12,7) : "H", (12,8) : "H", (12,9) : "H", (12,10) : "H", (12,1) : "H", (12,11) : "H",
              (11,2) : "D", (11,3) : "D", (11,4) : "D", (11,5) : "D", (11,6) : "D", (11,7) : "D", (11,8) : "D", (11,9) : "D", (11,10) : "D", (11,1) : "D", (11,11) : "D",
              (10,2) : "D", (10,3) : "D", (10,4) : "D", (10,5) : "D", (10,6) : "D", (10,7) : "D", (10,8) : "D", (10,9) : "D", (10,10) : "H", (10,1) : "H", (10,11) : "H",
              (9,2) : "H", (9,3) : "D", (9,4) : "D", (9,5) : "D", (9,6) : "D", (9,7) : "H", (9,8) : "H", (9,9) : "H", (9,10) : "H", (9,1) : "H", (9,11) : "H",
              (8,2) : "H", (8,3) : "H", (8,4) : "H", (8,5) : "H", (8,6) : "H", (8,7) : "H", (8,8) : "H", (8,9) : "H", (8,10) : "H", (8,1) : "H", (8,11) : "H"                    
}

#TODO: How to handle these, have to read the hand of the player - how should it be represented? 
# Can do .hasAce() == True, then just represent with the (Ace + other_card, dealers_sum)
# Example: (10,2) means the player has Ace and a 9 -> Flaw: Here we have assumed that the player has two cards, but does not really matter if sum is the same. 
softTotals = {(10,2) : "S", (10,3) : "S", (10,4) : "S", (10,5) : "S", (10,6) : "S", (10,7) : "S", (10,8) : "S", (10,9) : "S", (10,10) : "S", (10,1) : "S", (10,11) : "S",
               (9,2) : "S", (9,3) : "S", (9,4) : "S", (9,5) : "S", (9,6) : "D", (9,7) : "S", (9,8) : "S", (9,9) : "S", (9,10) : "S", (9,1) : "S", (9,11) : "S",
               (8,2) : "D", (8,3) : "D", (8,4) : "D", (8,5) : "D", (8,6) : "D", (8,7) : "S", (8,8) : "S", (8,9) : "H", (8,10) : "H", (8,1) : "H", (8,11) : "H",
               (7,2) : "H", (7,3) : "D", (7,4) : "D", (7,5) : "D", (7,6) : "D", (7,7) : "H", (7,8) : "H", (7,9) : "H", (7,10) : "H", (7,1) : "H", (7,11) : "H",
               (6,2) : "H", (6,3) : "H", (6,4) : "D", (6,5) : "D", (6,6) : "D", (6,7) : "H", (6,8) : "H", (6,9) : "H", (6,10) : "H", (6,1) : "H", (6,11) : "H",
               (5,2) : "H", (5,3) : "H", (5,4) : "D", (5,5) : "D", (5,6) : "D", (5,7) : "H", (5,8) : "H", (5,9) : "H", (5,10) : "H", (5,1) : "H", (5,11) : "H",
               (4,2) : "H", (4,3) : "H", (4,4) : "H", (4,5) : "D", (4,6) : "D", (4,7) : "H", (4,8) : "H", (4,9) : "H", (4,10) : "H", (4,1) : "H", (4,11) : "H",
               (3,2) : "H", (3,3) : "H", (3,4) : "H", (3,5) : "D", (3,6) : "D", (3,7) : "H", (3,8) : "H", (3,9) : "H", (3,10) : "H", (3,1) : "H", (3,11) : "H"
}

# NOTE: Since all entries in this matrix is a pair, we write the players hand as just one card, i.e. if play has A,A we just write (1, dealersum) 
# Currently not take into account the DAS case. 
# TODO: Lookup 3 pair, and 2 pair cases, when we dont split, what do we do? -> Just play normally? 

pairSplitting = {(11,2) : "SP", (11,3) : "SP", (11,4) : "SP", (11,5) : "SP", (11,6) : "SP", (11,7) : "SP", (11,8) : "SP", (11,9) : "SP", (11,10) : "SP", (11,11) : "SP", 
                 (1,2) : "SP", (1,3) : "SP", (1,4) : "SP", (1,5) : "SP", (1,6) : "SP", (1,7) : "SP", (1,8) : "SP", (1,9) : "SP", (1,10) :  "SP", (1,1) : "SP", (1,11) : "SP",
                 (10,2) : "S", (10,3) : "S", (10,4) : "S", (10,5) : "S", (10,6) : "S", (10,7) : "S", (10,8) : "S", (10,9) : "S", (10,10) : "S", (10,1) : "S", (10,11) : "S",
                 (9,2) : "SP", (9,3) : "SP", (9,4) : "SP", (9,5) :  "SP", (9,6) : "SP", (9,7) : "S", (9,8) : "SP", (9,9) : "SP", (9,10) : "S", (9,1) : "S", (9,11) : "S",
                 (8,2) : "SP", (8,3) : "SP", (8,4) : "SP", (8,5) : "SP", (8,6) : "SP", (8,7) : "SP", (8,8) : "SP", (8,9) : "SP", (8,10) : "SP", (8,1) : "SP", (8,11) : "SP",
                 (7,2) : "SP", (7,3) : "SP", (7,4) : "SP", (7,5) : "SP", (7,6) : "SP", (7,7) : "SP", (7,8) : "H", (7,9) : "H", (7,10) : "S", (7,1) : "H", (7,11) : "H",
                 (6,2) : "H", (6,3) : "SP", (6,4) : "SP", (6,5) : "SP", (6,6) : "SP", (6,7) : "H", (6,8) : "H", (6,9) : "H", (6,10) : "H", (6,1) : "H", (6,11) : "H",
                 (5,2) : "D", (5,3) : "D", (5,4) : "D", (5,5) : "D", (5,6) : "D", (5,7) : "D", (5,8) : "D", (5,9) : "D", (5,10) : "H", (5,1) : "H", (5,11) : "H",
                 (4,2) : "H", (4,3) : "H", (4,4) : "H", (4,5) : "H", (4,6) : "H", (4,7) : "H", (4,8) : "H", (4,9) : "H", (4,10) : "H", (4,1) : "H", (4,11) : "H",
                 (3,2) : "H", (3,3) : "H", (3,4) : "SP",  (3,5) : "SP", (3,6) : "SP", (3,7) : "SP", (3,8) : "H", (3,9) : "H", (3,10) : "H", (3,1) : "H", (3,11) : "H",
                 (2,2) : "H", (2,3) : "H", (2,4) : "SP", (2,5) : "SP", (2,6) : "SP", (2,7) : "SP", (2,8) : "H", (2,9) : "H", (2,10) : "H", (2,1) : "H", (2,11) : "H"                
} 