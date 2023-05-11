import sys
input = sys.stdin.readline

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

ch = [0] * n
Min = 100 * n  # 능력치 범위를 고려한 초기값 설정


def dfs(L, start):
    global Min

    if L == n // 2:  # 한 팀의 인원이 n // 2명인 경우
        team1 = [i for i in range(n) if ch[i] == 1]  # 팀 1에 속한 멤버들
        team2 = [i for i in range(n) if ch[i] == 0]  # 팀 2에 속한 멤버들

        # 팀 1의 능력치 계산
        s1 = sum(board[i][j] for i in team1 for j in team1)
        # 팀 2의 능력치 계산
        s2 = sum(board[i][j] for i in team2 for j in team2)

        Min = min(Min, abs(s1 - s2))
        return

    for i in range(start, n):
        ch[i] = 1  # 팀 1에 속한 멤버 선택
        dfs(L+1, i+1)  # 다음 멤버 선택
        ch[i] = 0  # 선택 취소
        dfs(L+1, i+1)  # 다음 멤버 선택하지 않고 다음으로 넘어감

dfs(0, 0)
print(Min)
