# 맞았습니다!
import sys

# for _ in range(int(sys.stdin.readline())):
#     lst = list()
#     # 입력
#     for i in range(int(sys.stdin.readline())):
#         lst.append(list(map(str, sys.stdin.readline().split())))
#     #최대값 구하기
#     max_val = 0
#     for i in range(len(lst)):
#         max_val = max(max_val, int(lst[i][0]))
#     # 그 최대값을 가진 이름 구하기
#     for i in range(len(lst)):
#         if lst[i][0] == str(max_val):
#             print(lst[i][1])
#             break


# Dictionary를 사용한 남의 코드 - 간결해서 가져와봄
input = sys.stdin.readline 

n = int(input())

for _ in range(n) :
    p = int(input())
    player = {}
    for _ in range(p) :
        money, name = input().split()
        player[int(money)] = name
    print(player[max(list(player.keys()))])