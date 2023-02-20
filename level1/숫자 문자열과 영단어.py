def solution(s: str):
    a = {
        'zero': "0",
        'one': "1",
        'two': "2",
        'three': "3",
        'four': "4",
        'five': "5",
        'six': "6",
        'seven': "7",
        'eight': "8",
        'nine': "9"
    }

    for i in a.keys():
        print(i)
        s = s.replace(i, a.get(i))


    print(s)
    return int(s)

print(solution("one4seveneight"))
