# 프로그래머스 '요격 시스템'

def solution(targets):
    targets.sort(key=lambda x : x[1])
    answer, end = 0, 0

    for st, en in targets:
        if st >= end:
            answer += 1
            end = en

    return answer
