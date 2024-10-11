# 프로그래머스 '전화번호 목록'

answer = True
phone_book = ["1195524421", "119", "97674223"]
phone_book.sort()

hash_table = {}
for p in phone_book:
    if p not in hash_table:
        hash_table[p] = 1

for key in hash_table:
    temp = ''
    for k in key:
        temp += k
        if temp in hash_table and temp != key:
            answer = False
            break

print(answer)
