# Twenty-One PEDAC

## Problem

### Rules

- Deck - Start with standard 52 card deck, 4 suits (Hearts, Diamonds, Clubs, Spades), and 13 values (2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace).
- Goal - Try to get as close to 21 as possible without going over. If you go over 21 it's a bust and you lose.
- Setup - game consists of dealer and player. Both iniitially dealt a hand of two cards. The player ccan see their two cards, but can only see one of the dealer's cards.
- Card values
  - Cards 2:10 are worth their face value.
  - All royals are worth 10.
  - Ace is worth 1 or 11 depending on circumstances **determined each time a new card is drawn from the deck**
    - If hand contains a 2, an Ace, and a 5, value is 18. Sum is 11 because sum doesn't exceed 2.
    - Say anothe Ace is drawn, one of the Ace's value must be 1 because 2 + 11 + 5 + 11 exceeds 21 (program must determine value of both Ace's). Same with a third Ace drawn etc...
    - Cannot ask player what value the Ace needs to be
- Player turn - player always goes first. Can choose to hit or stay.
  - Hit means dealt another card. If total exceeds 21, bust and loses
  - To hit or stay depends on the payer's and what they think the dealer has.
  - Player can hit as many times as they want - turn over when they bust or stay. If bust, game is over and dealer won
- Dealer turn - when player stays, it's the dealers turn. Rules for hit or stay: hit until the total is at least 17. If the dealer busts, then the player wins.
- Comparing cards - When both player and dealer stay, it's time to compare total value of the cards and see who has the highest value (winner)

- Inputs: player choosing hit or stay
- Outputs: if the player wins or not

### Possible Functions needed

- Deck constructor
- Bust or 21 checker
- Ace counter
- generic hand (cards) counter
- Ace value determiner
- generic hit
- generic stay
- loop for player round
- loop for dealer round
- loop for match
- shuffle function
- display cards (to terminal)

### Possible edge cases

- 1. 

## Examples / Test Cases

### Examples of game play

~~~text
Dealer has: Ace and unknown card
You have: 2 and 8
~~~

- You should hit in this scenario

~~~text
Dealer has: 7 and unknown card
You have: 10 and 7
~~~

- You should stay in this scenario since chances are good that the unknown card is not an Ace (only situation you can lose).

~~~text
Dealer has: 5 and unknown card
You have: Jack and 6
~~~

- Best chance here is to stay and hope the dealer busts because they have to hit based on their rules.

## Data Structures

- Use a nested list to represent each card's value and suite: [[2, 'S'], [2, 'H'], etc...]
- Use dictionary to represent the game board

## Algorithm

### High Level Pseudocode

1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
4. If player bust, dealer wins
5. Dealer turn: hit or stay - repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner

### Possible functions needed

- Deck constructor
- Bust or 21 checker
- Ace counter
- generic hand (cards) counter
- Ace value determiner
- generic hit
- generic stay
- loop for player round
- loop for dealer round
- loop for match
- shuffle function
- display cards (to terminal)
- game board display function (to terminal)

### Formal pseudocode

- **define create_card_for_display function** - this creates and returns an ascii formatted card that will display the passed face value and suite
  - Use f strings and ascii characters to format a string to represent the card
  - return the card

- **define display_board function** - displays the current hands to the player, takes argument board and an optional boolean flag to display all or not
  - *SET* list to contain the dealer's cards to display, *GET* them from the board argument
  - *SET* list to contain the player's cards to display, *GET* them from the board argument
  - print the dealer's cards (all of them if arg flag is true)
  - print the player's cards


- **define initialize_game_board function** - will hold the data structures that keep track of the cards on the table (in dealers and players hands)
  - *SET* the player's current hand of cards (starts off empty)
  - *SET* the dealer's current hand of cards (starts off empty, remember only shows 1 card upon initial deal, can be handled in the display_board function)
  - *SET* dictionary that will contain both the player's and dealer's hands of cards
  - return the dictionary containing the hands

- **define update_game_board_with_cards function** - takes in board, card argument, and string argument specifying dealer or player and updates the board dict data structure with the card or cards
  - iterate through the card or cards
    - add them to the associated data structure (player or dealer) in the board data structure

- **define initialize_deck function** - creates a deck of 52 cards, does NOT initially shuffle them
  - *SET* an empty list
  - *SET* string that contains all the valid card face values
  - *SET* string that contains all the valid card suites
  - Iterate through the two strings, appending all combinations to the empty list creating a nested list that contains all 52 cards
  - return the deck of cards

- **define shuffle_deck function** - takes in deck of cards argument and mutates the original list containing the deck
  - *PRINT* shuffling cards now...
  - return the deck of cards shuffled - use random.shuffle() method

- **define deal_cards function** - takes in deck of cards and board arguments, deals cards upon start of game to dealer and player.

- **define play_21 function** - main game loop function
  - *START* Outer game loop starts here (so player can choose to play multiple rounds) $
    - *SET* the deck of cards with initialize_deck function $
    - *SET* the game board with initialize_game_board function $
    - shuffle the deck of cards with shuffle function (*PRINT* that we are shuffling so player knows what's happening) $
    - deal cards to player and dealer with deal_cards function (*PRINT* that we are dealing the cards so player knows what's happening)
    - *PRINT* display the current state of the game board showing what cards are in player's hand and the one visible from dealer, call to display board function
    - call to play_round function to handle player and dealer gameplay
    - *PRINT* who won the round
    - *PRINT* Ask player if they want to play another round
    - IF no to another round, exit the loop


- **define main function call**:
  - *PRINT* Greet player to 21 game and provide basic instructions
  - call to play_21 function (main game loop)
  - Exit program by saying bye to player
