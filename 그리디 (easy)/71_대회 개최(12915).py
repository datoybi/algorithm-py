'''
헐.. 어렵다 ㅠㅠㅠㅠ 담에 다시 풀어보쟈
남에 코딩 봐도 모르겠당,
대회를 개최하기 위해서는 문제 3개가 모두 있어야 한다.


'''

import sys

E, EM, M, MH, H = list(map(int, sys.stdin.readline().split()))
ans = 0
for x in range(EM + 1):
    a = E + x
    b = M + EM + MH - x
    c = H
    y = (b - c) // 2 

    if y < 0:
        y = 0
    elif y > MH:
        y = MH

    k = min(a, b-y, c+y)
    ans = max(ans, k)
print(ans)




# 틀렸습니다
# import sys

# E, EM, M, MH, H = list(map(int, sys.stdin.readline().split()))
# min_val = min(E + EM, EM + M + MH, MH + H)
# print(min_val)

# for i in range(min_val, -1, -1):
#     front = EM - (i - E)
#     back = MH - (i - H)
#     if front > 0 :
#         front = EM
#     if back > 0 :
#         back = MH

#     print(i, front, back)
#     if M + front + back >= i:
#         print(i)
#         break
