n = int(input())

s = 1
cnt = 1

while s < n:
    s += cnt * 6
    cnt += 1
print(cnt)
