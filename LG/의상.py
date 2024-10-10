# 프로그래머스 '의상'

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
dic = {}
answer = 1

for c in clothes:
    key = c[1]
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1

for key in dic:
    answer *= (dic[key] + 1)

print(answer)
