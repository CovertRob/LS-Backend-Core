'''

OOP Design approach

1. Write a textual description of the problem or exercise
2. Extract the significant nouns and verbs from the description
3. Organize and associate the verbs and nouns

Description

1. Tic Tac Toe is a 2 player board game
2. The board is a 3x3 grid
3. Players take turns marking a square with a marker than that 
identifies the player
4. The first player to mark 3 squares in a row wins
5. Traditionally, the player to go first uses the marker X to 
mark their squares, and the player to go second uses O as a marker.
6. The first player to mark 3 squares in a row with their marker wins the game
7. A row can be horizontal, vertical, or either of the two diaganols 
8. There is one human player and one computer player
9. The human player always moves first in the initial version of our game

Nouns: game, board, square, grid, marker, row, player, human, computer
Verbs: play, mark, move, place

Organize most likely relationships:

Game
Board
Row
Square
Marker
Player
    Mark
    Play
    Human
    Computer

    
Now create scaffolding


'''
import random
import os

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        # STUB
        # We need some way to keep track of this square's
        #   marker.
        self.marker = marker

    def __str__(self) -> str:
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

def clear_screen():
    os.system('clear')

class Board:
    def __init__(self):
        # STUB
        # We need a way to model the 3x3 grid. Perhaps
        #   "squares"?
        # What data structure should we use? A list? A
        #   dictionary? Something else?
        # What should the data structure store? Strings?
        #   Numbers? Square objects?
        # Matrix is messy, lists are confusing starting with index 0
        self.squares = {key: Square() for key in range(1, 10)}

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

class Player:
    def __init__(self, marker):
        # STUB
        # A player is either a human or a computer that is
        #   playing the game.
        # Perhaps we need a "marker" to keep track of this
        #   player's symbol? (i.e., 'X' or 'O')
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

class Human(Player):
    def __init__(self):
        # STUB
        # What does a human player need to do? How does it
        #   differ from the basic Player or a Computer?
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        # STUB
        # What does a computer player need to do? How does
        #   it differ from the basic Player or a Human?
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:

    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of board
        (4, 5, 6),  # center row of board
        (7, 8, 9),  # bottom row of board
        (1, 4, 7),  # left column of board
        (2, 5, 8),  # middle column of board
        (3, 6, 9),  # right column of board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7),  # diagonal: top-right to bottom-left
    )

    def __init__(self):
        # STUB
        # We need a board and two players.
        self.board = Board()
        self.human = Human()
        self.computer = Computer()

    def play(self):
        # STUB
        # Orchestrate game play.
        # Display a welcome messsage
        # Repeat until the game is over
            # dispay the current state of the board
            # Let the first player make a move
            # Is the game over? If so, exit this loop
            # Let the second player make a move
            # Is the game over? If so, exit this loop
        # Display the final state of the board
        # Display the final result
        # Display a goodbye message

        self.display_welcome_message()
        self.board.display()

        while True:
            self.human_moves()
            if self.is_game_over():
                break
            self.computer_moves()
            if self.is_game_over():
                break
            self.board.display_with_clear()
        self.board.display_with_clear()
        self.display_results()
        self.display_goodbye_message()

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to Tic Tac Toe!\n")

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("Computer won.")
        else:
            print("A tie game.")

    def human_moves(self):
        while True:
            valid_choices = self.board.unused_squares()
            choices_list = [str(choice) for choice in valid_choices]
            choices_str = ", ".join(choices_list)
            prompt = f"Choose a square ({choices_str}): "
            choice = input(prompt)
            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass
            print("Sorry, that's not a valid choice.")
            print()
        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        valid_choices = self.board.unused_squares()
        choice = random.choice(valid_choices)
        self.board.mark_square_at(choice, self.computer.marker)

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or self.is_winner(self.computer))

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True
        return False

game = TTTGame()
game.play()