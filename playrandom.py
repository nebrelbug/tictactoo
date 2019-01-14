from random import *
import numpy as np
np.set_printoptions(threshold=np.nan)
from Logic import is_game_won as score
from Logic import msg
from Game import Game
import AIPlayer as AI
from printboard import print_board
#from randomboards import training_boards
#from randomscores import training_scores

boardfile = open("randomboards.py", "w")
scorefile = open("randomscores.py", "w")
allGameBoards = np.array([])
allGameScores = np.array([])

for i in range(0,30000): #Starts at 0. (0,1) will play 1 game with i==0
    thisGame = Game()
    thisGameBoards = np.zeros((9, 9), dtype=np.int)
    playerX = AI.Player('x')
    playerO = AI.Player('o')
    while score(thisGame) == 'none':
        thisGame.move('x', playerX.play_random(thisGame)) ## player, pos
        #print("turn # " + str(thisGame.turn))
        thisGameBoards[thisGame.turn] = thisGame.board
        #print_board(thisGame.board)
        if score(thisGame) != 'none':
            break
        thisGame.move('o', playerO.play_random(thisGame)) ## player, pos
        thisGameBoards[thisGame.turn] = thisGame.board

        #print_board(thisGame.board)
        if score(thisGame) != 'none':
            break 
    #print_board(thisGame.board)
    #msg(score(thisGame), thisGame.board)
    thisGameBoards = thisGameBoards[~np.all(thisGameBoards == 0, axis=1)]
    thisGameScores = np.full(len(thisGameBoards), score(thisGame) + 1, dtype=np.int)
    if i == 0: ## Initializing the arrays
        allGameBoards = thisGameBoards
        allGameScores = thisGameScores
    else:
        allGameBoards = np.append(allGameBoards, thisGameBoards, axis=0)
        allGameScores = np.append(allGameScores, thisGameScores)

    #print(thisGameScores)
    #fill(score(thisGame))

    #print(np.array2string(thisGameBoards, separator = ','))
    #print(np.array2string(thisGameScores, separator = ','))
    #print("Finished game number: " + str(i))


from sklearn.utils import shuffle
allGameBoards, allGameScores = shuffle(allGameBoards, allGameScores)


training_boards = np.array2string(allGameBoards, separator = ',')
training_scores = np.array2string(allGameScores, separator = ',')
outputboardcontent = """import numpy as np
training_boards = np.array(""" + training_boards + ")"
outputscorecontent = """import numpy as np
training_scores = np.array(""" + training_scores + ")"
boardfile.write(outputboardcontent)
scorefile.write(outputscorecontent)