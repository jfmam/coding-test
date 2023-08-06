a,b,c,x,y=map(int,input().split())
if a+b<c*2: # 반반으로 사는게 더 비쌀경우
    print(a*x+b*y)
else: 
    m=min(x,y) # 반반으로 살 수 있는 최대를 사고 남은마리 수를 따로 구매한다.
    print(c*m*2+min(c*2,a)*max(0,x-m)+min(c*2,b)*max(0,y-m))