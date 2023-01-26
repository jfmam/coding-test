import sys
input = sys.stdin.readline
a = []
while True:
    temp = input().rstrip()
    if int(temp) == 0:
        break
    a.append(temp)

for j in range(len(a)):
    b = list(a[j])
    flag = True
    for i in range(len(b)):
        if b[i] != b[len(b) - i-1]:
            print('no')
            flag = False
            break
    if flag:
        print('yes')
