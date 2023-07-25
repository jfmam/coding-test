import sys
from itertools import combinations
from collections import defaultdict

input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
answer = 0
sa = defaultdict(int) # defaultdict 개념
sb = defaultdict(int)

for i in range(1,n+1): # 부배열의 합을 구하는 로직
    for j in list(combinations(a,i)):
        print(j)