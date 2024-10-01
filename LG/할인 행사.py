# 프로그래머스 '할인 행사'

def solution(want, number, discount):
    answer = 0
    iteration = len(discount) - 9

    for i in range(iteration):
        counts = [0] * len(number)
        for j in range(i, i + 10):
            for k in range(len(want)):
                if want[k] == discount[j]:
                    counts[k] += 1

        if counts == number:
            answer += 1

    return answer
