import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
Min = 99999999

for i in range(n):
    for j in range(i+1,n): # +를 안하면 같은수를 여러번 더하게 된다
        for k in range(j+1,n):
            s = a[i] + a[j] + a[k]
            if s <= m:
                Min = min(Min, m-s)
print(m-Min)
            

# sys.setrecursionlimit(10**7)

# ch = [False for _ in range(m)]

# def func(total, cnt, idx):
#     if(len(a) == idx):
#         return
#     if cnt == 3:
#         if total <= m:
#             global Min
#             Min = min(Min, m-total)
#     else:
#         for i in range(n):
#             if not ch[i]:
#                 ch[i] = True
#                 func(total + a[i], cnt+1, idx+1)
                
#                 ch[i] = False
#                 func(total, cnt, idx+1)

# func(0, 0, 0)
# print(m-Min)
