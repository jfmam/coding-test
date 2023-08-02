def find_nth_doomsday(n):
    count = 0
    num = 666

    while True:
        if '666' in str(num):  # 숫자에 '666'이 포함되어 있는지 확인
            count += 1
            if count == n:
                return num
        num += 1

n = int(input())
result = find_nth_doomsday(n)
print(result)
