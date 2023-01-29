# Top down 과 bottm up
## Top down
import sys
input = sys.stdin.readline
test = int(input().rstrip())
res = []

def findNum(x,y):
    if board[x][y] != 0:
        return board[x][y]
    else:
        if x >= 0 and x <= k and y > 0 and y <= n:
            for i in range(y+1):
                board[x][y] += findNum(x-1, i)
            return board[x][y]
        else:
            return 0
            

for i in range(test):
    global k
    global n
    k = int(input().rstrip())
    n = int(input().rstrip())
    global board 
    board = [[0 for _ in range(n+1)] for _ in range(k+1)]
    for i in range(n+1):
        board[0][i] = i
    findNum(k,n)
    res.append(board[k][n])
print(*res, sep="\n")

# bottom up
# test = int(input())

# for i in range(test):
#     k= int(input())
#     n=int(input())
#     apt = [i for i in range(1, n+1)]
    
#     for i in range(k+1):
#         for j in range(1,n): # n 옆집까지
#             apt[j] += apt[j-1] # 아랫집 + 옆집
#     print(apt[-1])
