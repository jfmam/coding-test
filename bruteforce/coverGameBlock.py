import sys
input = sys.stdin.readline

C = int(input())
coverType = [[(0, 0), (0, 1), (-1, 1)], [(0, 0), (1, 0), (1, 1)],
             [(0, 0), (1, 0), (0, 1)], [(0, 0), (0, 1), (1, 1)]]

def isCover(x,y,w,h):
    for i in coverType:
        for dx,dy in i:
            xx = dx + x
            yy = dy + y
            if board[xx][yy] == '#':
                break;
            if xx < 0 or xx >= w or yy < 0 or yy >= h:
                break;
            
                

def solution(h, w, board):
    x,y=0,0
    for i in range(h):
        for j in range(w):
            if(board[i][j] == '.'):
                isCover(i,j,w,h)
                


for _ in range(C):
    h, m = map(int, input().rstrip().split())
    # 문자열을 list로 반환하면 문자 하나씩 배열로 만들어진다.
    board = [ list(input()) for _ in range(h)] # 2차원배열의 행을 넣어줄 것
    solution(h,m,board)
