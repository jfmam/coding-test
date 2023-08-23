import sys
from collections import deque

wall = []
for i in range(8):
    temp = sys.stdin.readline()
    for j in range(8):
        if temp[j] == "#":
            wall.append([i, j])

# start: 7, 0 // end: 0, 7
def bfs():
    cnt = 0
    q = deque([(7, 0)]) # i, j
    move = [[0, 0], [1, 0], [-1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]] # 제자리에 있을 수있다.
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()

            if [i,j] in wall:
                continue # 들어있으면 더이상 지나갈 수 없다.
            if i == 0 or cnt == 9: # 행이 0에 도달하거나 9턴 이상 살아있다면 이미 벽이 다 내려가 무조건 도착할 수 있다.
                print(1)
                return

            for k in move:
                ii = k[0] + i
                jj = k[1] + j
                if 0 <= ii < 8 and 0 <= jj < 8:
                    if [ii, jj] not in wall: # wall이 같은 부분이 없을 때만 이동 가능
                        q.append((ii, jj))
        for i in range(len(wall)): # enumerate로 할 경우 tuple형태로 나와 변경 불가능
            wall[i] = [wall[i][0]+1, wall[i][1]] # 아래로 내려가는 것이기 때문에 

        cnt+=1

    print(0)

if len(wall) == 0:
    print(1)
else:
    bfs()