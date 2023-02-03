import sys
input = sys.stdin.readline

n = int(input())
board = []
for i in range(n):
    b = input().rstrip()
    c = []
    for j in b:
        c.append(int(j))
    board.append(c)


def dfs(x, y, l):
    global board
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
        print(board[x][y], end= "")
    else: # 배열 슬라이스
        print("(", end="")
        # 기존의 배열에서 (x~x+l, y,y+l) l//2만큼 이동하면서 시작점을 재조정 
        for i in range(x, x+l, (l // 2) or 1): # 범위 조심! 기존의 배열에서 step을통해 2차원 배열 slice
            for j in range(y, y+l, (l // 2) or 1): # l//2 ==0에서 왜 오류가 안뜰까? flag 때문에  l=1일 때 else문을 돌지 않는다.
                dfs(i, j, l//2)
        print(")", end="") 


dfs(0, 0, n)
