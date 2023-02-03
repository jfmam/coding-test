import sys
input = sys.stdin.readline

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

white = 0
blue = 0


def divide(x, y, l):
    a = board[x][y]
    flag = True
    for i in range(x, x+l):
        for j in range(y, y+l):
            if board[i][j] != a:
                flag = False
                break
        if not flag:
            break
    if flag:
        global white
        global blue
        if board[x][y] == 1:
            blue += 1
        else:
            white += 1
    else:
        for i in range(x, x+l, l // 2):
            for j in range(y, y+l, l//2):
                divide(i, j, l//2)


divide(0, 0, n)
print(white,blue,sep="\n")