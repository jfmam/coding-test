import sys
input = sys.stdin.readline
a = list(map(int, input().split()))
flag = 0
if a[0] == 1:
    flag = 1
elif a[0] == 8:
    flag = 2
else:
    print("mixed")
    exit()

if flag == 2:
    for i in range(8,0,-1):
        if i != a[8-i]:
            print("mixed")
            exit()
    print("descending")
    exit()
elif flag == 1:
    for i in range(1, 9):
        if i != a[i-1]:
            print("mixed")
            exit()
    print("ascending")
    exit()
