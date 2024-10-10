# 프로그래머스 '구명보트'

def solution(people, limit):
    people.sort()

    answer = 0
    st = 0
    en = len(people) - 1

    while st <= en:
        if people[st] + people[en] <= limit:
            st += 1
            en -= 1
        else:
            en -= 1
        answer += 1

    return answer
