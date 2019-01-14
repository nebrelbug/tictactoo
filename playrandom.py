import numpy as np
np.set_printoptions(threshold=np.nan)
from Logic import is_game_won as score
from Logic import msg
from Game import Game
from RandomPlayer import Random

boardfile = open("randomboards.py", "w")
scorefile = open("randomscores.py", "w")
testboardfile = open("testboards.py", "w")
testscorefile = open("testscores.py", "w")

def return_boards():
    allGameBoards = np.array([])
    allGameScores = np.array([])

    for i in range(0,3000): #Starts at 0. (0,1) will play 1 game with i==0
        thisGame = Game()
        thisGameBoards = np.zeros((9, 9), dtype=np.int)
        while score(thisGame) == 'none':
            thisGame.move('x', Random(thisGame)) ## player, pos
            thisGameBoards[thisGame.turn-1] = thisGame.board
            if score(thisGame) != 'none':
                break
            thisGame.move('o', Random(thisGame)) ## player, pos
            thisGameBoards[thisGame.turn] = thisGame.board
            if score(thisGame) != 'none':
                break 
        thisGameBoards = thisGameBoards[~np.all(thisGameBoards == 0, axis=1)]
        thisGameScores = np.full(len(thisGameBoards), score(thisGame) + 1, dtype=np.int)
        if i == 0: ## Initializing the arrays
            allGameBoards = thisGameBoards
            allGameScores = thisGameScores
        else:
            allGameBoards = np.append(allGameBoards, thisGameBoards, axis=0)
            allGameScores = np.append(allGameScores, thisGameScores)

    from sklearn.utils import shuffle
    allGameBoards, allGameScores = shuffle(allGameBoards, allGameScores)


    training_boards = np.array2string(allGameBoards, separator = ',')
    training_scores = np.array2string(allGameScores, separator = ',')
    outputboardcontent = "import numpy as np\ntraining_boards = np.array(" + training_boards + ")"
    outputscorecontent = "import numpy as np\ntraining_scores = np.array(" + training_scores + ")"
    return outputboardcontent, outputscorecontent

randomboards, randomscores = return_boards()

boardfile.write(randomboards)
scorefile.write(randomscores)

testboards, testscores = return_boards()
testboardfile.write(testboards)
testscorefile.write(testscores)