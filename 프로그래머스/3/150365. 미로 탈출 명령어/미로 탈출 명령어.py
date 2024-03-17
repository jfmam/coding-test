from collections import deque

def distance(x, y, r, c):
    return abs(x - r) + abs(y - c)

def solution(n, m, x, y, r, c, k):
    answer = ''
    move = [(1, 0), (0, -1), (0, 1), (-1, 0)]
    move_directions = ['d', 'l', 'r', 'u']
    q = deque([(x, y, 0, '')])
    
    dist = distance(x, y, r, c)
    
    if k < dist or (k - dist) % 2 == 1:
        return 'impossible'
    
    while q:
        i, j, cnt, s = q.popleft()
        if i == r and j == c and cnt == k:
            return s
        if i == r and j == c and (k - cnt) % 2:
            return 'impossible'
        for idx, v in enumerate(move):
            ii = i + v[0]
            jj = j + v[1]
            if 1 <= ii <= n and 1 <= jj <= m:
                if k < cnt + distance(ii,jj,r,c) + 1:
                    continue
                q.append((ii, jj, cnt + 1, s + move_directions[idx]))
                break
                    
    return 'impossible'
