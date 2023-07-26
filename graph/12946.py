import sys
sys.setrecursionlimit(10**9)

n = int(input())

board = []

for _ in range(n):
    board.append(list(input()))

# 육각형을 구할땐 왼쪽대각선위, 오른쪽 대각선 아래를 추가할 것
dx = [-1,-1,0,0,1,1] 
dy = [0,1,-1,1,-1,0]

ans = 0

def dfs(x, y):
    global ans
    ans = max(ans, 1)

    # 다음 방향
    for k in range(6):
        nx, ny = x+ dx[k], y+ dy[k]

        if 0 <= nx < n and 0 <= ny <n and board[nx][ny] == 'X':
            if  visited[nx][ny] == 0:
                visited[nx][ny] = -visited[x][y] # 다른색으로 칠함 -> 0,1,0,1 이런식으로 칠해지는것과 같은 원리, 최소한
                dfs(nx, ny)
                ans = max(ans, 2)
            else:
                if visited[nx][ny] == visited[x][y]: ## 0,1,0,1,1 이런게 발견될 경우 -> 0,1,0,2,1이되고 3 출력하고 종료
                    ans = max(ans, 3)
                    return

visited = [[0]*n for _ in range(n)]

for x in range(n):
    for y in range(n):
        if board[x][y] == 'X' and visited[x][y] == 0:
            visited[x][y] = 1 
            dfs(x, y)


print(ans)