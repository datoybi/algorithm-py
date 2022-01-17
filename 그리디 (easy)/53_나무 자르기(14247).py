'''
맞았습니다!

n개의 나무를 하루에 한 나무씩 n일 산에 오르며 자른다.
어느 나무를 먼저 잘라가느냐에 따라서 총 구할 수 있는 나무의 양이 다른데,
나무의 처음 길이와 하루에 자라는 양
영선이가 얻을 수 있는 최대 나무양
자른 이후에도 나무는 0부터 다시 자라기 때문에 같은 나무를 여러 번 자를 수는 있다.

'''
import sys

N = int(sys.stdin.readline())
tmp1 = list(map(int, sys.stdin.readline().split()))
tmp2 = list(map(int, sys.stdin.readline().split()))
lst = list()

for i in range(N):
    lst.append([tmp1[i], tmp2[i]])
lst.sort(key = lambda x : [x[1]])
result = 0

for i in range(N):
    result += lst[i][0] + lst[i][1]*i
print(result)

# 시간초과
# import sys

# N = int(sys.stdin.readline())
# tmp1 = list(map(int, sys.stdin.readline().split()))
# tmp2 = list(map(int, sys.stdin.readline().split()))
# lst = list()

# for i in range(N):
#     lst.append([tmp1[i], tmp2[i]])
# lst.sort(key = lambda x : [x[1]])
# print(lst)
# result = 0

# for i in range(N):
#     print(lst)
#     result += lst[i][0]
#     lst[i][0] = 0
#     for j in range(N):
#         lst[j][0] += lst[j][1]
# print(result)