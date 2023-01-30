from itertools import combinations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
n, k = map(int, input().split())
a = [i for i in range(1, n+1)]
s = 0
for _ in combinations(a, k):
    s += 1
print(s)