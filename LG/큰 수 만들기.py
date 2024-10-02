# 프로그래머스 '큰 수 만들기'

number = '187961'
k = 2

stack = []
for n in number:
    while stack and stack[-1] < n and k > 0:
        stack.pop()
        k -= 1
    stack.append(n)

if k > 0:
    for _ in range(k):
        stack.pop()

answer = ''.join(stack)
