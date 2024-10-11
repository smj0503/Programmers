# 프로그래머스 '기능개발'

from collections import deque

progresses = [93, 30, 55]
speeds = [1, 30, 5]

work_days = deque()
for i in range(len(progresses)):
    left = 100 - progresses[i]
    days = 0

    while left > 0:
        left -= speeds[i]
        days += 1

    work_days.append(days)

answer = []

while work_days:
    days = work_days.popleft()
    block = 1

    while work_days and days >= work_days[0]:
        next_days = work_days.popleft()
        block += 1

    answer.append(block)

print(answer)
