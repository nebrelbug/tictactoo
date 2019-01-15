from random import randint
import numpy as np
np.set_printoptions(threshold=np.nan)
from Logic import is_game_won as score
from Logic import msg
from Game import Game
import AIPlayer as AI

def playGame():
    if randint(0, 1) == 0:
        print("AI is X and goes first")
        play_ai_as_x()
    else:
        print("You are X and go first")
        play_ai_as_o()

def play_ai_as_x():
    thisGame = Game()
    ai = AI.Player()
    while score(thisGame) == 'none':
        if thisGame.turn % 2 == 0: # turn is even, it's x's turn
            aiMove = ai.play(thisGame, 'x')
            # print("ai wants to move: " + str(aiMove))
            thisGame.move('x', aiMove) ## player, pos
        else: # User's turn
            inputPos = input("O, your turn: ")
            inputPos = int(inputPos)
            thisGame.move('o', inputPos) ## player, pos

        if score(thisGame) != 'none': # If the game is won or drawn
            msg(score(thisGame), thisGame.board)
            break

def play_ai_as_o():
    thisGame = Game()
    ai = AI.Player()
    while score(thisGame) == 'none':
        if thisGame.turn % 2 != 0: # turn is even, so it's x's turn
            aiMove = ai.play(thisGame, 'o')
            # print("ai wants to move: " + str(aiMove))
            thisGame.move('o', aiMove) ## player, pos
        else: # User's turn
            inputPos = input("X, your turn: ")
            inputPos = int(inputPos)
            thisGame.move('x', inputPos) ## player, pos

        if score(thisGame) != 'none': # If the game is won or drawn
            msg(score(thisGame), thisGame.board)
            break 

playGame()