"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    x = 0
    o = 0
    for row in board:
        for cell in row:
            if cell == X:
                x += 1
            elif cell == O:
                o += 1

    if x == 0 and o == 0:
        return X
    if x <= o:
        return X
    else:
        return O


def actions(board):
    if terminal(board):
        return EMPTY
    possible_moves = set()
    for row in range(3):
        for cell in range(3):
            if board[row][cell] == EMPTY:
                possible_moves.add(tuple((row, cell)))

    return possible_moves


def result(board, action):
    dummy = copy.deepcopy(board)
    row, cell = action
    if dummy[row][cell] != EMPTY:
        raise "Not a Valid Move"
    dummy[row][cell] = player(dummy)
    return dummy


def winner(board):
    x, o = 0, 0
    for row in board:
        for cell in row:
            if cell == X:
                x += 1
            elif cell == O:
                o += 1
        if x == 3:

            return X
        elif o == 3:

            return O

        x, o = 0, 0

    for cell in range(3):
        for row in range(3):
            if board[row][cell] == X:
                x += 1
            elif board[row][cell] == O:
                o += 1
        if x == 3:

            return X
        elif o == 3:

            return O

        x, o = 0, 0

    col = 0
    for row in range(3):
        if board[row][col] == X:
            x += 1
        elif board[row][col] == O:
            o += 1
        col += 1
        if x == 3:

            return X
        elif o == 3:

            return O
    x, o = 0, 0

    col = 2
    for row in range(3):
        if board[row][col] == X:
            x += 1
        elif board[row][col] == O:
            o += 1
        col -= 1
        if x == 3:
            return X
        elif o == 3:
            return O

    return EMPTY


def terminal(board):
    total = 0
    if not winner(board) == EMPTY:
        return True
    for row in board:
        if EMPTY not in row:
            total += 1
    if total == 3:
        return True
    return False


def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    elif win == EMPTY:
        return 0


def maxValue(board):
    if terminal(board):
        return utility(board)
    else:
        v = -math.inf
        possible_moves = actions(board)

        for move in possible_moves:
            v = max(v, minValue(result(board, move)))
        return v


def minValue(board):
    if terminal(board):
        return utility(board)
    else:
        v = math.inf
        possible_moves = actions(board)

        for move in possible_moves:
            v = min(v, maxValue(result(board, move)))

        return v


def minimax(board):
    currentPlayer = player(board)
    dummy = copy.deepcopy(board)
    if terminal(dummy):
        return EMPTY

    elif currentPlayer == X:
        totalMoves = []
        for move in actions(dummy):
            totalMoves.append([minValue(result(dummy, move)), move])
        return sorted(totalMoves)[-1][1]

    elif currentPlayer == O:
        totalMoves = []
        for move in actions(dummy):
            totalMoves.append([maxValue(result(dummy, move)), move])
        return sorted(totalMoves)[0][1]
