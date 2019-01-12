def is_game_won(game):
    board = game.board
    result = 'none'
    if board[0] == board[1] and board[0] == board[2] and board[2] != 0: # First horizontal row
        result = board[0]
    elif board[3] == board[4] and board[3] == board[5] and board[5] != 0: # Second horizontal row
        result = board[3]
    elif board[6] == board[7] and board[7] == board[8] and board[8] != 0: # Third horizontal row
        result = board[6]
    elif board[0] == board[3] and board[3] == board[6] and board[6] != 0: # First column
        result = board[0]
    elif board[1] == board[4] and board[4] == board[7] and board[7] != 0: # Second column
        result = board[1]
    elif board[2] == board[5] and board[5] == board[8] and board[8] != 0: # Third column
        result = board[2]
    elif board[0] == board[4] and board[4] == board[8] and board[8] != 0: # First diagonal
        result = board[0]
    elif board[2] == board[4] and board[4] == board[6] and board[6] != 0: # Second diagonal
        result = board[2]
    elif len(game.open_positions()) == 0:
        result = 0
    return result


def human_readable(score):
    if score == -1:
        return "X wins!"
    elif score == 1:
        return "O wins!"
    else:
        return "It's a draw!"