import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    q = deque()
    q.append(i)
    ch = [0] * n
    # ch[i] = 1 # 시작한 부분을 check 하지 않는다... 다시 돌아 올 수도 있으니까?
    while q:
        v = q.popleft()
        for j in range(n):
            if ch[j] == 0 and board[v][j] == 1:
                board[i][j] = 1 # board[v][j] board[i][j]의 차이점 -> 현재 i에서 갈 수 있는 노드를 찾는 것임으로 board[i][j]로 표시
                ch[j] = 1
                q.append(j)
for i in range(n):
    print(*board[i])
