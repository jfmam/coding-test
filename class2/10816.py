import sys

input = sys.stdin.readline
b = [0] * 10001
n = int(input())
for i in range(n):
    b[int(input())] += 1
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]): # value 만큼 출력한다
            print(i)

# for 문에서 append를 하게 되면 메모리 재할당이 일어남으로 미리 할당해논다