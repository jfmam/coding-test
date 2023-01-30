x, y = map(int, input().split())

for i in range(x, y+1):
    if i == 1:  # 1은 소수가 아뉘지!
        continue
    for j in range(2, int(i ** 0.5)+1): # 지워야할 범위는 제곱근으로 해도된다. 어차피 나누어 떨어지는 것은 약수이기 떄문에 제외됨으로
        if i % j == 0:
            break
    else:
        print(i)
