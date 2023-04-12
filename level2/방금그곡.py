# 자신이 기억한 메로디를 이용해 음악을 찾는다.
# 한곡을 반복한 음악일 경우 끝분과 첫부분이 이어질 수 있다.
# 음악제목, 재생시작, 끝난시각, 악보
# 음은 C ~ B 12가지, 각음은 1분에 한개씩 재생, 음의 길이가 음악의 길이
# 음악 길이 > 재생기간 한곡 반복
# 반대인 경우 중간에 끊김
# 음악은 00:00을 넘기지 않는다.
# 조건이 일치하지 않는 음악의 경우 NONE 반환
# 조건이 일치하는 음악이 여러개일 경우  제일 긴 음악 제목을 반환


# #이 들어가면서 길이를 구하는데 문제가 생겼다. #을 소문자로 바꾸는 것
def changeSharpToLower(s):
    return s.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")


def changeMinutes(start, end):
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))
    sm = sh * 60 + sm
    em = eh * 60 + em
    return em - sm


def solution(m, musicinfos):
    # m: 기억하고 있는 멜로디
    # musicinofos 음악정보
    answer = '(None)'
    # 음악 제목 반환하기
    m = changeSharpToLower(m)
    maxTime = 0
    for i in musicinfos:
        start, end, title, music = i.split(',')
        music = changeSharpToLower(music)
        musicLen = len(music)
        total = changeMinutes(start, end)
        cnt = total // musicLen
        remain = total % musicLen
        listenMusic = cnt * music + music[:remain]

        if m in listenMusic:
            if total > maxTime:  # 빠진 조건
                maxTime = total
                answer = title

    return answer
