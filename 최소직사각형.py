# 프로그래머스 '최소직사각형'

def solution(sizes):
    widths = []
    heights = []

    for s in sizes:
        w, h = s
        if w < h:
            w, h = h, w
        widths.append(w)
        heights.append(h)

    answer = max(widths) * max(heights)

    return answer
