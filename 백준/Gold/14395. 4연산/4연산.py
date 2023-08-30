from collections import deque
s,t = map(int,input().split())

if s == t:
    print(0)
    exit(0)
ch = set()
q = deque([(s, '')])
Max = 10e9
answer = []

while q:
    v, a = q.popleft()
    
    if v == t:
        print(a)
        exit(0)
    
    v_sum = v + v
    v_minus = v - v
    v_mul = v * v
    
    if v_mul <= Max and v_mul not in ch:
        ch.add(v_mul)
        q.append((v_mul, a + '*'))
    if  v_sum <= Max and v_sum not in ch:
        ch.add(v_sum)
        q.append((v_sum, a + '+'))
    if v != 0:
        v_div = v // v
        if v_div <= Max and  v_div not in ch:
            ch.add(v_div)
            q.append((v_div, a + '/'))
print(-1)