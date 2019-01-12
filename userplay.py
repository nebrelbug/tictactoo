from random import randint
import numpy as np
np.set_printoptions(threshold=np.nan)
from Logic import is_game_won as score
from Logic import human_readable as msg
from Game import Game
import AIPlayer as AI
from printboard import print_board

def playGame():
    thisGame = Game()
    if randint(0, 1) == 0:
        print("AI is X and goes first")
        aiPlayer = 'x'
    else:
        print("You are X and go first")
    ai = AI.Player(aiPlayer)
    while score(thisGame) == 'none':
        if aiPlayer == 'x':
            thisGame.move('x', ai.play_random(thisGame)) ## player, pos
            print_board(thisGame.board)
            if score(thisGame) != 'none':
                print_board(thisGame.board)
                print(msg(score(thisGame)))
                break
            inputPos = input("O, your turn: ")
            inputPos = int(inputPos)
            thisGame.move('o', inputPos) ## player, pos
            # print_board(thisGame.board)
            if score(thisGame) != 'none':
                print_board(thisGame.board)
                print(msg(score(thisGame)))
                break 
        else:
            inputPos = input("X, your turn: ")
            inputPos = int(inputPos)
            thisGame.move('x', inputPos) ## player, pos
            print_board(thisGame.board)
            if score(thisGame) != 'none':
                print_board(thisGame.board)
                print(msg(score(thisGame)))
                break
            thisGame.move('o', ai.play_random(thisGame)) ## player, pos
            # print_board(thisGame.board)
            if score(thisGame) != 'none':
                print_board(thisGame.board)
                print(msg(score(thisGame)))
                break 

playGame()