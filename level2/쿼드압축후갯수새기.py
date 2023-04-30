from collections import deque


def solution(board):
    answer = [0, 0]
    n = len(board)
    q = deque([(0, 0, n)])
    while q:
        x, y, l = q.popleft()
        if all(board[x+i][y+j] == board[x][y] for i in range(l) for j in range(l)):
            answer[board[x][y]] += 1
        else:
            nl = l // 2
            q.append((x, y, nl))
            q.append((x, y+nl, nl))
            q.append((x+nl, y, nl))
            q.append((x+nl, y+nl, nl))
    return answer
