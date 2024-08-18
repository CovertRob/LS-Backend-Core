# Object Oriented appraoch to rock-paper-scissors game

# Rock Paper Scissors is a two player game where each player chooses one of three possible moves: rock, paper, or scissors. The chosen moves will then be comopared to see who wins, according to the following rules:
#   - rock beats scissors (rock crushess scissors)
#   - scissors beats paper (scissors cut paper)
#   - paper beats rock (paper wraps rock)
#   If the players choose the same move, then it's a tie

# Now extract the nouns and verbs from the description to begin formatting it into OOP style

# Nouns: player, move, rule
# Verbs: choose, compare
# r, p, s are all variations on a move - almost like different states of a move

# step 3, organizing the verbs with the nouns

# Player - choose
# Move
# Rule
#  compare ?

# sketch out code
import random

class Player:

    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self) -> None:
        self.move = None

class Computer(Player):
    def init(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self) -> None:
        super().__init__()

    def choose(self):
        prompt = 'Please choose rock, paper, or scissors: '

        while True:
            choice = input(prompt).lower()
            if choice in Player.CHOICES:
                break
            print(f"Sorry, {choice} is not valid")

        self.move = choice 

# Now need orchestration engine

class RPSGame:
    def __init__(self) -> None:
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock ppaper Scissors. Goodbye!')

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == 'rock' and computer_move == 'scissors') or
            (human_move == 'paper' and computer_move == 'rock') or
            (human_move == 'scissors' and computer_move == 'paper'))

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((computer_move == 'rock' and human_move == 'scissors') or
                (computer_move == 'paper' and human_move == 'rock') or
                (computer_move == 'scissors' and human_move == 'paper'))

    def _display_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            print('You win!')
        elif self._computer_wins():
            print('Computer wins!')
        else:
            print("It's a tie")

    def _play_again(self):
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')

    def play(self):
        self._display_welcome_message()
        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break
        self._display_goodbye_message()

play = RPSGame()
play.play()