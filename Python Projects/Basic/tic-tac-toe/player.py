# Tic-Tac-Toe
import math 
import random as rd

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all their players to get their next move
    def get_move(self, game):
        pass # abstract method

class RandomComputerPlayer(Player): # sub-class of parent Player
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = rd.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn.Input move (0-8):')
        # we are going to check that this is a correct value by trying to cast
        # it to an integer, and if it's not, then we say it's invalid
        # if that spot is not available on the board, we also say it's invalid.
            try:
                val = int(square)
                if  val not in  game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. try again!')

            return val    
    
    