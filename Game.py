import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

class Game():
    def __init__(self):
        self.board = np.array([0,0,0,0,0,0,0,0,0]).astype(int) # X's are -1, O's are +1. X always goes first
        self.turn = -1
  
    def move(self, player, pos): # player is 'X' or 'O'. Pos is an integer from 0 to 8
        # print('pos: ' + str(pos))
        if self.board[pos] == 0:
            if player == 'x':
                self.board[pos] = -1
            elif player == 'o':
                self.board[pos] = 1
            self.turn += 1
        else:
            return 'error'

    def open_positions(self):
        open = np.array([])
        for i in range(0,9):
            if self.board[i] == 0:
                open = np.append(open, i)
        #print(open)
        return open.astype(int)

game = Game()