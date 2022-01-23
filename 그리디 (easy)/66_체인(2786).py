'''
맞았습니다!

하나의 긴 체인으로 모든 체인을 묶기
6
2 2 10 10 10 10
4

5
4 3 5 7 9
3

10
5 1 4 5 5 5 1 3 4 1
6

3
3 3 3
2
'''
import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
chain, ring = 0, 0

if len(lst) == 2:
    print(1)
    exit(0)

for i in range(len(lst)):
    if sum(lst[0:i+1]) >= N-(i+2):
        chain = sum(lst[0:i+1])
        ring = N-(i+2)
        break

diff = chain - ring
if diff != 0:
    print(ring + 1)
else:
    print(ring)







# import sys
# N = int(sys.stdin.readline())
# lst = list(map(int, sys.stdin.readline().split()))
# lst.sort()
# chain = 0
# ring = 0

# if len(lst) == 2:
#     print(1)
#     exit(0)

# for i in range(len(lst)):
#     print(sum(lst[0:i+1]), N-(i+2))
#     if sum(lst[0:i+1]) >= N-(i+2):
#         chain = sum(lst[0:i])
#         ring = N-(i+1)
#         break
# if chain < ring:

# # print(chain , ring)
# # diff = chain - ring
# # print(ring + diff)
