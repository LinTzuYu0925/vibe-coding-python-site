# P5：井字棋棋盤，巢狀 list
board = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    [" ", " ", "X"],
]
print(board[1])
print(board[1][1])
print(board[0][2])
board[2][0] = "O"
print(board[2])
print(len(board))
print(len(board[0]))
