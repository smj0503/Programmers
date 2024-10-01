# 프로그래머스 '정수를 나선형으로 배치하기'

from collections import deque

# 현재 좌표 (x, y) 일때,
# 오른쪽으로 한칸 이동 : (x, y+1)
# 아래로 한칸 이동 : (x+1, y)
# 왼쪽으로 한칸 이동 : (x, y-1)
# 위로 한칸 이동 : (x-1, y)

def solution(n):
    answer = [[0] * n for _ in range(n)]

    answer[0][0] = 1
    q = deque()
    q.append([0, 0])
    # 현재 이동 방향
    cur_dir = 'r'

    while q:
        x, y = q.popleft()

        # 현재 이동 방향이 오른쪽일 경우
        if cur_dir == 'r':
            # 오른쪽으로 이동 가능하면 오른쪽으로 이동
            if y + 1 < n and answer[x][y + 1] == 0:
                answer[x][y + 1] = answer[x][y] + 1
                q.append([x, y + 1])
            # 안되면 아래로 이동
            elif x + 1 < n and answer[x + 1][y] == 0:
                answer[x + 1][y] = answer[x][y] + 1
                q.append([x + 1, y])
                cur_dir = 'd'

        # 현재 이동 방향이 아래일 경우
        elif cur_dir == 'd':
            # 아래로 이동 가능하면 아래로 이동
            if x + 1 < n and answer[x + 1][y] == 0:
                answer[x + 1][y] = answer[x][y] + 1
                q.append([x + 1, y])
            # 안되면 왼쪽으로 이동
            elif y - 1 >= 0 and answer[x][y - 1] == 0:
                answer[x][y - 1] = answer[x][y] + 1
                q.append([x, y - 1])
                cur_dir = 'l'

        # 현재 이동 방향이 왼쪽일 경우
        elif cur_dir == 'l':
            # 왼쪽으로 이동 가능하면 왼쪽으로 이동
            if y - 1 >= 0 and answer[x][y - 1] == 0:
                answer[x][y - 1] = answer[x][y] + 1
                q.append([x, y - 1])
            # 안되면 위로 이동
            elif x - 1 >= 0 and answer[x - 1][y] == 0:
                answer[x - 1][y] = answer[x][y] + 1
                q.append([x - 1, y])
                cur_dir = 'u'

        # 현재 이동 방향이 위일 경우
        elif cur_dir == 'u':
            # 위로 이동 가능하면 위로 이동
            if x - 1 >= 0 and answer[x - 1][y] == 0:
                answer[x - 1][y] = answer[x][y] + 1
                q.append([x - 1, y])
            # 안되면 오른쪽으로 이동
            elif y + 1 < n and answer[x][y + 1] == 0:
                answer[x][y + 1] = answer[x][y] + 1
                q.append([x, y + 1])
                cur_dir = 'r'

    return answer
