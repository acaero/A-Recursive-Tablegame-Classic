"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"  # The maximizing player
O = "O"  # The minimizing player
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_moves = 0
    o_moves = 0

    for row in board:
        for column in row:
            if column == X:
                x_moves += 1
            elif column == O:
                o_moves += 1

    if x_moves == o_moves:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (apa) in form (i, j) available on the board.
    """
    apa = set()
    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                apa.add((row, column))

    return apa


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    apa = actions(board)
    if action not in apa:
        raise NotImplementedError("Eyooo here we go again.")

    p = player(board)
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = p
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    Transforms lists into sets, which automatically throws duplicates out.
    If the length of the set is 1 and the value in the set is not none (EMPTY) then it must be 3 in a row.
    """
    # Check Rows
    for row in board:
        if len(set(row)) == 1 and row[0] is not None:
            return row[0]

    # Check Columns
    for i in range(3):
        if len(set([row[i] for row in board])) == 1 and board[0][i] is not None:
            return board[0][i]

    # Check Diagonal from top left to bottom right
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] is not None:
        return board[0][0]

    # Check Diagonal from bottom left to top right
    if len(set([board[i][-(i+1)] for i in range(3)])) == 1 and board[2][0] is not None:
        return board[2][0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    Checks if there are empty squares left.
    If there are no empty squares left or the winner function returns a winner, the game must be over.
    """
    finished = True
    for row in board:
        if row.count(None) != 0:
            finished = False

    if winner(board) is not None or finished:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    apa = actions(board)
    p = player(board)

    if p == X:
        v = -99
        a = None
        for action in apa:
            m = min_value(result(board, action))
            if m > v:
                v = m
                a = action
        return a

    if p == O:
        v = 99
        a = None
        for action in apa:
            m = max_value(result(board, action))
            if m < v:
                v = m
                a = action
        return a


def min_value(board):
    if terminal(board):
        return utility(board)

    v = 99
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -99
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
