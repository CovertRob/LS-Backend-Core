'''

OOP Design approach

1. Write a textual description of the problem or exercise
2. Extract the significant nouns and verbs from the description
3. Organize and associate the verbs and nouns

Description

1. Tic Tac Toe is a 2 player board game
2. The board is a 3x3 grid
3. Players take turns marking a square with a marker than that identifies the player
4. The first player to mark 3 squares in a row wins
5. Traditionally, the player to go first uses the marker X to mark their squares, and the player to go second uses O as a marker.
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

class Row:
    def __init__(self):
        # STUB
        # We need some way to identify a row of 3 squares
        pass

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

    def play(self):
        # STUB
        # We need a way for each player to play the game.
        # Do we need access to the board?
        pass

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

        while True:
            self.board.display()

            self.human_moves()
            if self.is_game_over():
                break
            self.computer_moves()
            if self.is_game_over():
                break
        self.board.display()
        self.display_results()
        self.display_goodbye_message()

    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_results(self):
        pass

    def human_moves(self):
        choice = None
        while True:
            choice = input("Choose a square between 1 and 9: ")
            try:
                choice = int(choice)
                if 1 <= choice <= 9:
                    break
            except ValueError:
                pass
            print("Sorry, that's not a valid choice.")
            print()
        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        choice = random.randint(1, 9)
        self.board.mark_square_at(choice, self.computer.marker) # doesn't currently check if a square is already taken or not

    def is_game_over(self):
        return False
    



game = TTTGame()
game.play()