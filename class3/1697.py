from collections import deque
n, k = map(int, input().split())
ch = [0] * 100001
q = deque([n])

# while q:
#     a = q.popleft()
#     if a == k:
#         break
#     if a-1 >= 0 and ch[a-1] == 0:
#         q.append(a-1)
#         ch[a-1] = ch[a]+1
#     if a+1 <= 2*(k+1) and ch[a+1] == 0:
#         q.append(a+1)
#         ch[a+1] = ch[a] + 1
#     if 2*a < 2*(k+1) and ch[2*a] == 0:
#         q.append(2*a)
#         ch[2*a] = ch[a] + 1
while q:
    a = q.popleft() # cur 
    if a == k:
        break
    for i in (a-1, a+1, 2*a):
        if 0 <= i <= 100001 and ch[i] == 0: # BFS DFS 핵심은 접근하지 않은 곳을 중복적으로 접근하면 안된다!
            ch[i] = ch[a] + 1 # next = cur + 1 이거 중요하다.!
            q.append(i)

print(ch[k])
