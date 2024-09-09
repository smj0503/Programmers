# from itertools import permutations
# solution 1 : permutations(순열) 사용
# def solution(k, dungeons):
#     answer = 0
#
#     for p in permutations(dungeons, len(dungeons)):
#         tmp = k
#         cnt = 0
#
#         for need, spend in p:
#             if tmp >= need:
#                 tmp -= spend
#                 cnt += 1
#             answer = max(answer, cnt)
#
#     return answer


# solution 2 :
answer = 0

def dfs(k, cnt, dungeons, visited):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
            visited[i] = False

def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer
