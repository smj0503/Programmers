# 프로그래머스 '조이스틱'

def solution(name):
    answer = 0
    n = len(name)
    move = n - 1

    for n in name:
        answer += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)

    for idx in range(n):
        next_idx = idx + 1
        while next_idx < n and name[next_idx] == 'A':
    return answer

# print(solution('JAAN'))
