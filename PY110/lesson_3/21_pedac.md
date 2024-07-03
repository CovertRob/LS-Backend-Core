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
- Player turn - player always goes first. Can choose to hit or stay.
  - Hit means dealt another card. If total exceeds 21, bust and loses
  - To hit or stay depends on the payer's and what they think the dealer has.
  - Player can hit as many times as they want - turn over when they bust or stay. If bust, game is over and dealer won
- Dealer turn - when player stays, it's the dealers turn. Rules for hit or stay: hit until the total is at least 17. If the dealer busts, then the player wins.
- Comparing cards - When both player and dealer stay, it's time to compare total value of the cards and see who has the highest value (winner)

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

### Possible edge cases

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
