    function makeImg(card) {
        const img = document.createElement("img");
        img.src = "../static/cards/" + card.filename;
        img.width = 100;
        return img;
    }

    function applySplitVisual(cards) {
        const hand1 = document.getElementById("player-hand-1");
        const hand2 = document.getElementById("player-hand-2");

        hand1.innerHTML = "";
        hand2.innerHTML = "";

        hand1.appendChild(makeImg(cards[0]));
        hand2.appendChild(makeImg(cards[1]));

        // Remove the .hidden from the class of hand2 
        hand2.classList.remove("hidden");

        hand1.classList.add("split-left");
        hand2.classList.add("split-right");
    }

    function resetSplitVisual() {
        const hand1 = document.getElementById("player-hand-1");
        const hand2 = document.getElementById("player-hand-2");

        // Hide the second hand again
        hand2.classList.add("hidden");

        // Remove the split positioning
        hand1.classList.remove("split-left");
        hand2.classList.remove("split-right");
    }

    async function sendAction(action) {
        
        // error in this function, hand2 is null on the 2.nd call. 
        // resetSplitVisual();

        const response = await fetch("/action", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ action: action })
        });

        // Gets the jsonify'ed data from handle_action(). 
        const data = await response.json();

        if (data.split_cards == true) {
            applySplitVisual(data.player.hand)

            // TODO: More stuff here, handle this case aside from the other cases. 
        }

        // Update message text dynamically
        document.querySelector("#message").innerText = `Ready to play blackjack (Gamestate: ${data.gameAlive})`;
        document.querySelector("#game_message").innerText = `GAME MESSAGE: ${data.game_message}`;

        // Update sums 
        document.querySelector("#dealer-sum").innerText = `Dealer Sum: ${data.dealer.sum}`;
        document.querySelector("#dealer-visible-sum").innerText = `Dealer Visible Sum: ${data.dealer.hand[0].value}`;
        document.querySelector("#player-sum").innerText = `Player Sum: ${data.player.sum}`;

        // Update display card 
        const playerCardDiv = document.querySelector("#player-cards");
        const dealerCardDiv = document.querySelector("#dealer-cards");

        playerCardDiv.innerHTML = "";
        dealerCardDiv.innerHTML = "";

        for (const card of data.player.hand) {
            const img = document.createElement("img");
            img.src = `/static/cards/${card.filename}`;
            img.width = 100;
            playerCardDiv.appendChild(img);
        }

        for (const card of data.dealer.hand) {
            const img = document.createElement("img");
            img.src = `/static/cards/${card.filename}`;
            img.width = 100;
            dealerCardDiv.appendChild(img);
        }



        // TODO: Animations for actions 

        // For debugging.    
        console.log("Response data:", data);
    }