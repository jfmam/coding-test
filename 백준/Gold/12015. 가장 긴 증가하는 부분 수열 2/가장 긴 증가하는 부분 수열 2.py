def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

n = int(input())
a = list(map(int, input().split()))

lis = [a[0]]

for i in range(1, n):
    # a[i] 가 lis 마지막값보다 크다면 제일 큰 값 갱신
    if a[i] > lis[-1]:
        lis.append(a[i])
    else: # 작거나 같을 경우 lis에 target을 넣어줄 index를 찾는다.
        idx = binary_search(lis, a[i])
        lis[idx] = a[i]

print(len(lis))
