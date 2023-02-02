import sys
input = sys.stdin.readline
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
# 2차원 배열은 slice 할 수없다

ch = {-1: 0, 0: 0, 1: 0}

def dfs(x, y, l): # 시작점, 길이
    global board
    a = board[x][y]
    flag = True
    for i in range(x, x+l): # 다른게 있는지 검사
        for j in range(y, y+l):
            if a != board[i][j]:
                flag = False
                break
        if not flag:
            break
    if flag: # 없으면 카운팅
        ch[board[x][y]] += 1
    else: # 다른게 있으면 분할
        for i in range(x, x+l, l // 3): # range 범위구하기 힘들다...
            for j in range(y, y+l, l // 3):
                dfs(i, j, l//3)


dfs(0, 0, n)
for i in ch.values():
    print(i)
