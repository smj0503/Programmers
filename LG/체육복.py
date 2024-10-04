# 프로그래머스 '체육복'

num = 5
los = [2, 4]
res = [1, 3, 5]

def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n+2)

    for r in reserve:
        students[r] += 1

    for l in lost:
        students[l] -= 1

    for i in range(1, n+1):
        if students[i] == 2:
            if students[i-1] == 0:
                students[i] -= 1
                students[i-1] += 1
            elif students[i+1] == 0:
                students[i] -= 1
                students[i+1] += 1

    for i in range(1, n+1):
        if students[i] > 0:
            answer += 1

    return answer
