"""
맞았습니다!
보니까 XX..XX.. 이 케이스 처리도 해주어야 한다  

8
XX..XX..
..XX..XX
XX..XX..
..XX..XX
XX..XX..
..XX..XX
XX..XX..
..XX..XX

16

"""
import sys

# 입력
N, room = int(sys.stdin.readline()), list()
for i in range(N):
    room.append(list(map(str, sys.stdin.readline().rstrip())))

# 가로 계산
row = 0
for i in range(len(room)):
    row_cnt = 0 # 연속한 .이 몇개인지 
    for j in range(len(room)):
        if room[i][j] == '.': # . 이면 카운트
            row_cnt += 1
        elif room[i][j] == 'X' and row_cnt >= 2: # X이지만 카운트한게 2보다 크면 자리 +1
            row += 1
            row_cnt = 0
        else: 
            row_cnt = 0

    if row_cnt >= 2: # 카운트가 2보다 크면 자리 +1 
        row += 1

# print(row_cnt, row)
# 세로 계산
calumn = 0

for i in range(len(room)):
    calumn_cnt = 0 
    for j in range(len(room)):
        if room[j][i] == '.':
            calumn_cnt += 1
        elif room[j][i] == 'X' and calumn_cnt >= 2: 
            calumn += 1
            calumn_cnt = 0
        else:
            calumn_cnt = 0

    if calumn_cnt >= 2:
        calumn += 1

print(row, calumn)


