import sys
from collections import Counter

input = sys.stdin.readline
n = int(input().rstrip())
ar = []
for _ in range(n):
    ar.append(int(input().rstrip()))


def sansul(a: list[int]):
    s = sum(a)
    return int(round(s/n, 0))


def mid(a: list[int]):
    s = sorted(a)
    midNum = s[(len(s) - 1) // 2]
    return midNum


def most(a: list[int]):
    b = sorted(a)
    cnt = Counter(b).most_common()
    if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
        return cnt[1][0]
    else:
        return cnt[0][0]


def rangeNum(a: list[int]):
    return max(a) - min(a)


print(sansul(ar))
print(mid(ar))
print(most(ar))
print(rangeNum(ar))
