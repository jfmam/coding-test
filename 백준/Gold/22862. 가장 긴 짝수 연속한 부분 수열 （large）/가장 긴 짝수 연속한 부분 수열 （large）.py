n,k = map(int, input().split())
a = list(map(int, input().split()))

s,e = 0,0 # 끝
result = 0 # 짝수로 이루어져 있는 연속한 부분 수열중 가장 긴길이
even= 0 # s,e사이의 짝수 갯수
odd = 0 # 지우려는 홀수 count 하기

while s < n and e < n:
    if odd > k:
        result = max(result, even)
        if a[s] % 2 == 1:
            odd -= 1
        else:
            even -= 1
        s += 1
    else:
        if a[e] % 2 == 1:
            odd += 1
        else:
            even += 1
        e += 1
        
# even을 계속 더해주다가 k개를 초과하지 못하고 더하고 끝냈을 경우가 있기 때문에 한번 더 추가해준다.
result = max(result, even)
print(result)
