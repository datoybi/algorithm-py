'''
 제목도 두 스티커인데 두개를 붙이는걸 문제 읽고도 몰랐다 지나ㅉ 난독이 있나보다..
2 2
2 
1 2
2 1

4

10 9
4
2 3
1 1
5 10
9 11

56

10 10
3
6 6
7 7
20 5

0
아오 어려웠다 이건 어캐 구현해야하는지 모르겠따. 다음에 꼮 풀어보기
'''

# import sys

# h, w = map(int, sys.stdin.readline().split())
# # print(h, w)
# paper = list()
# for _ in range(h):
#     paper.append([0 for _ in range(w)])

# print(paper)
# # [
# #   [0, 0], 
# #   [0, 0]
# # ]
# # N = int(sys.stdin.readline())
# sticker = list()
# for i in range(int(sys.stdin.readline())):
#     r, c = map(int, sys.stdin.readline().split())
#     sticker.append([r, c])

# print(sticker)
# # [[1, 2], 
# # [2, 1]]   
# for i in range(len(sticker)):
#     tmp_lst = list()
#     for _ in range(sticker[i][0]):
#         tmp_lst.append([0 for _ in range(sticker[i][1])])
#     if tmp_lst in paper:
#         print('yes')
#     print(tmp_lst)
        
# 남 코드 
import sys
h, w = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

sticker = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
result = 0

# print(sticker) # [[1, 2], [2, 1]]

for i in range(n):
    for j in range(i+1, n):
        r1 = max(sticker[i][0], sticker[i][1])
        c1 = min(sticker[i][0], sticker[i][1])
        r2 = max(sticker[j][0], sticker[j][1])
        c2 = min(sticker[j][0], sticker[j][1])
        # print(r1, c1, r2, c2)

        # 이해못하겠음 .. 
        if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
            result = max(result, r1*c1 + r2*c2)
        if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
            result = max(result, r1*c1 + r2*c2)
        if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
            result = max(result, r1*c1 + r2*c2)
        if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
            result = max(result, r1*c1 + r2*c2)

print(result)


