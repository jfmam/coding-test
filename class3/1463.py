from collections import deque
n = int(input())
Min = 99999999
m = [0] * (n+1)

for i in range(2, n+1):
    m[i] = m[i-1] + 1 # i가 1이되는데 필요한 최소한의 연산횟수를 저장 -> 어차피 다음과정들을 통해 min value가 결정남으로 0이아닌 다른값을
    # 대입해서 비교할 수 있게 만들어준다.
    if i % 2 == 0:
        m[i] = min(m[i], m[i//2] + 1) # 이전 단계와 현단계의 비교
    if i % 3 == 0:
        m[i] = min(m[i], m[i//3] + 1)
print(m[n])

q = deque([n])
visited = [0] * (n+1)
while q:
    a = q.popleft()
    if a == 1:
        # a가 먼저 나오게 되는 순간이 최소값이 되는 순간이 된다.
        break
    if a % 3 == 0 and visited[a % 3] == 0:
        q.append(a//3)
        visited[a//3] = visited[a] +1 # 이 개념이 중요하다. 기존에 값에 +cnt를 해줌으로써 다음 노드에 접근을 몇번쨰에 했는지 알 수있다.
    elif a %2 == 0 and visited[a % 2] == 0:
        q.append(a//2)
        visited[a//2] = visited[a] +1
    q.append(a-1)
    visited[a-1] = visited[a] + 1
print(visited[1])