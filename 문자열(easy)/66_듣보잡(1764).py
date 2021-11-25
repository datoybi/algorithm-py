'''
맞았습니다!
    N 듣도 못한 사람 M 보도 못한 사람
    N개 줄에 듣도 못한 사람의 일므 
    N+2 줄에 보도 못한 사람의 이름


    중복 출력 잡기

'''

import sys

N, M = map(int, sys.stdin.readline().split())
a, result = list(), list()

for i in range(N+M):
    a.append(sys.stdin.readline().rstrip())
a.sort()
# print(a)

i = 0
while True:
    if i >= len(a)-1:
        break
    if a[i] == a[i+1]:
        result.append(a[i])
        i += 2
    else:
        i += 1

# 출력
print(len(result))
for i in result:
    print(i)





# # 이것도 시간초과.. 
# N, M = map(int, sys.stdin.readline().split())
# a, result= list(), list()

# for i in range(N):
#     a.append(sys.stdin.readline().rstrip())

# # 넣은걸 이제.. 있나 판별하고 넣음 어떨까 그럼 조금 나을수도...
# # print(a)

# for _ in range(M):
#     tmp = sys.stdin.readline().rstrip()
#     # print(tmp)
#     if tmp in a:
#         result.append(tmp)

# result.sort()
# print(len(result))
# for i in result:
#     print(i)

