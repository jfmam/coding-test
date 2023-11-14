def solution(N, stages):

    fail = {} # 실패율을 추가할 딕셔너리
    all = len(stages) # 스테이지에 도달한 플레이어 수(전체)
    
    for i in range(1,N+1):
        if all == 0: # 스테이지에 도달한 플레이어 수가 0명일 때
            fail[i] = 0
        else:
            fail[i] = stages.count(i)/(all)
            all -= stages.count(i) # 스테이지에 도달한 플레이어 수
        
    fail= sorted(fail, key=fail.get, reverse=True) 

    return fail