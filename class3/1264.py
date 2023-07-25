import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))


def rotate(i, j, end_i, end_j):
    topleft = board[i][j]
    bottomleft = board[end_i-1][j]
    bottomright = board[end_i-1][end_j-1]
    topright = board[i][end_j-1]

    for ii in range(i, end_i):
        board[ii][j] = board[i][j]
    for jj in range(j, end_j):
        board[i][jj] = board[i][j]
    for ii in range(end_i-1, i, -1):
        board[ii][j] = board[i][j]
    for ii in range(end_j-1, j, -1):
        board[i][jj] = board[i][j]

    board[i+1][j] = topleft
    board[end_i-1][j+1] = bottomleft
    board[end_i-2][end_j-1] = bottomright
    board[i][end_j-2] = topright


cycle = (n-1) * 2 + (m-1) * 2
for st in range(min(n, m) // 2):
    for _ in range(r % cycle):
        rotate(st, st, n - st, m - st)
    cycle -= 8
for i in board:
    print(*i, sep=" ")
