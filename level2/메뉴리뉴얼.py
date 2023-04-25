# 조건먼저 항상 체크하기
# 조건: 최대값이면서 선택한사람이 2명이상인 경우에만 answer에 추가할 것
# 조건: order는 정렬되지않아서 뽑아낼 시 문제가 될수도있음
# 1. orders 반복문을 돌면서 combination으로 course만큼 뽑기
# 2. 뽑은 후 딕셔너리 키값으로 설정 후 +1 씩해주기
# 3. 딕셔너리에서 가장큰 값 뽑기
# 4. 가장큰 값 뽑은 후 딕셔너리를 반복문을 돌면서 가장큰 값과 같으면서 2이상인 경우만 answer에 
#   넣을 것
# 5. return sorted(answer)

from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        a = {}
        for order in orders:
            for j in combinations(sorted(list(order)), c): # 배열이 정렬되었는지 확인
                b = ''.join(j)
                if b in a:
                    a[b] += 1
                else:
                    a[b] = 1
                
        try:
            maxV = max(list(a.values())) # 빈 배열을 보내면 동작하지 않는다.
            for i in list(a.items()):
                if i[1] == maxV and maxV >= 2: # 2이상인 조건 확인
                    answer.append(i[0])
        except:
            continue
    return sorted(answer)