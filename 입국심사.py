# 프로그래머스 '입국심사'

def solution(n, times):
    answer = 0

    st = 1
    en = max(times) * n

    while st <= en:
        mid = (st + en) // 2
        temp = 0

        for t in times:
            temp += mid // t

            if temp >= n:
                break

        if temp >= n:
            en = mid - 1
            answer = mid
        else:
            st = mid + 1

    return answer
