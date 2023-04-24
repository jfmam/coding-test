def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    converted = ''
    while n > 0:
        n, mod = divmod(n, k)
        converted += str(mod)

    converted = converted[::-1]
    nums = converted.split('0')
    count = 0
    for num in nums:
        if num == '':
            continue
        if is_prime(int(num)):
            count += 1
    return count