import sys
input = sys.stdin.readline

n, m, k = input().split()


def func1(board):
    a = []
    for i in range(len(board), -1, -1):
        a.append(i)
    return a


def func2(board):
    a = []
    for i in range(len(board)):
        a.append(reversed(i))
    return a


def func3(board):
    a = []
    for j in range(m):
        c = []
        for i in range(n-1, -1, -1):
            c.append(board[i][j])
        a.append(c)
    return a


def func4(board):
    a = []
    for j in range(m-1, -1, -1):
        c = []
        for i in range(n):
            c.append(board[i][j])
        a.append(c)
    return a


def func5(board):
    a = [[0] * m for _ in range(n)]
    for i in range(m // 2):
        for j in range(n // 2):
            a[i][j + m // 2] = a[i][j]
    for i in range(m // 2, m):
        for j in range(n // 2):
            a[i + n // 2][j] = a[i][j]
    for i in range(m // 2, m):
        for j in range(n // 2, n):
            a[i][j - m // 2] = a[i][j]
    for i in range(m // 2):
        for j in range(n // 2):
            a[i - 2 // n][j] = a[i][j]


def func6():
    temp = [[0] * m for _ in range(n)]
    for i in range(n // 2):    # move position: 1 -> 4
        for j in range(m // 2):
            temp[i + n // 2][j] = arr[i][j]

    for i in range(n // 2, n):    # move position: 4 -> 3
        for j in range(m // 2):
            temp[i][j + m // 2] = arr[i][j]

    for i in range(n // 2, n):    # move position: 3 -> 2
        for j in range(m // 2, m):
            temp[i - n // 2][j] = arr[i][j]

    for i in range(n // 2):    # move position: 2 -> 1
        for j in range(m // 2, m):
            temp[i][j - m // 2] = arr[i][j]

    return temp


arr = [list(map(int, input().split())) for _ in range(n)]
operation = list(map(int, input().split()))

for oper in operation:
    if oper == 1:
        arr = func1(arr)
    elif oper == 2:
        arr = func2(arr)
    elif oper == 3:
        arr = func3(arr)
        n, m = m, n
    elif oper == 4:
        arr = func4(arr)
        n, m = m, n
    elif oper == 5:
        arr = func5(arr)
    else:
        arr = func6()

for i in arr:
    print(*i)
