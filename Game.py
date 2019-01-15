import tensorflow as tf
from tensorflow import keras
import copy
from printboard import print_board

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

class Game():
    def __init__(self):
        self.board = np.array([0,0,0,0,0,0,0,0,0], dtype=int) # X's are -1, O's are +1. X always goes first
        self.turn = 0
  
    def move(self, player, pos): # player is 'X' or 'O'. Pos is an integer from 0 to 8
        print('Player ' + player + ' plays at ' + str(pos))
        if self.board[pos] == 0:
            if player == 'x':
                self.board[pos] = -1
            elif player == 'o':
                self.board[pos] = 1
            self.turn += 1
        else:
            print("Oops, that spot isn't open!")
        print_board(self.board)

    def return_move(self, player, pos): # player is 'X' or 'O'. Pos is an integer from 0 to 8
        return_board = copy.copy(self.board)
        if return_board[pos] == 0:
            if player == 'x':
                return_board[pos] = -1
            elif player == 'o':
                return_board[pos] = 1
        else:
            return 'error'
        return return_board

    def open_positions(self):
        open = np.array([], dtype=int)
        for i in range(0,9):
            if self.board[i] == 0:
                open = np.append(open, i)
        return open

game = Game()