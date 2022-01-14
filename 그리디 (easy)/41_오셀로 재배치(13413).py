'''
맞았습니다!
배치된 말 중 임의의 2개의 말을 골라 서로의 위치를 바꾼다.
말 1개를 들어 뒤집어 놓아 색상을 변경한다.
'''

# import sys

# for _ in range(int(sys.stdin.readline())):
#     int(sys.stdin.readline())
#     A = list(sys.stdin.readline().rstrip())
#     B = list(sys.stdin.readline().rstrip())
#     diff = [0, 0]
#     cnt = 0

#     for i in range(len(A)):
#         if A[i] != B[i] and A[i] == 'W': # 0
#             diff[0] += 1
#         elif A[i] != B[i] and A[i] == 'B':
#             diff[1] += 1

#     print(min(diff) + max(diff) - min(diff))


# 숏코딩 도저언
for _ in range(int(input())):
    int(input());A, B = list(input().rstrip()), list(input().rstrip())
    d, cnt = [0, 0], 0
    for i in range(len(A)):
        if A[i] != B[i] and A[i] == 'W': d[0] += 1;
        elif A[i] != B[i] and A[i] == 'B': d[1] += 1;
    print(min(d) + max(d) - min(d))

