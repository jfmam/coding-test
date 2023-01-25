import sys
input = sys.stdin.readline().rstrip
dic = {}

a = list(input().upper())
for i in a:
    if dic.get(i):
        dic[i] += 1
    else:
        dic[i] = 1
b = sorted(dic.items(), key=lambda x:x[1], reverse=True)

if len(b) == 1:
    print(b[0][0])
    exit()

if b[0][1] != b[1][1]:
    print(b[0][0])
else:
    print('?')
