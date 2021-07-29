"""
    제목 : 블랙잭
    난이도 : 하
    유형 : 배열, 완전 탐색
    시간 : 20분
"""

# a = list(map(int, input().split(' ')))

# count = a[0]
# m = a[1]
# bigtotal = 0
# remainder = 0
# counts = list(map(int, input().split(' ')))

# for i in range(0, count):
#     for j in range(i+1,count):
#         for z in range(j+1,count):
#             total = counts[i] + counts[j] + counts[z];
#             # print("i : " , counts[i], " j : " , counts[j] , " z :" , counts[z] , " total : " , total)
#             if remainder == 0:
#                 remainder = abs(m-total)
#             if remainder > abs(m-total):
#                 bigtotal = total
#                 remainder = abs(m-total)
#             # print("remainder : " , remainder)
# print(bigtotal)


# 답
n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

result = 0
length = len(data)

for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(result, sum_value)

print(result)

'''
    1. 문제를 잘못 읽음 - 절댓값이 필요 없고 작은 수로 했어야 햇음
    2. 난 max()를 몰라서 나머지를 비교해서 나머지가 작은 쪽을 기존 나머지에 대입하는 방식으로 하려 했으나 max라는 좋은 함수가 있었음을 몰랐음
    3. 기본로직은 비슷하게 잘 맞았음 칭찬함.
'''