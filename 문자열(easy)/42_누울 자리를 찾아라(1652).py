"""
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

N, room = int(sys.stdin.readline()), list()
for i in range(N):
    room.append(list(map(str, sys.stdin.readline().rstrip())))
# print(room) # [['.', '.', '.', '.', 'X'], ['.', '.', 'X', 'X', '.'], ['.', '.', '.', '.', '.'], ['.', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.']]
# 가로 계산
row = 0
max_check = 0
for i in range(len(room)):
    row_cnt = 0 # 한 줄에 몇개인지
    check = 0 # 연속됐는지 체크
    for j in range(len(room)):
        if room[i][j] == '.':
            row_cnt += 1
            check += 1
        else:
            max_check = max(max_check, check)
    
    print(row_cnt, check, row)
        # if row_cnt >= 2:
        #     row += 1
        #     row_cnt = 0
        # print(row_cnt, row)
            
            
# 세로 계산
calumn = 0
for i in range(len(room)):
    calumn_cnt = 0
    for j in range(len(room)):
        if room[j][i] == '.':
            calumn_cnt += 1
        else:
            calumn_cnt = 0
        
        if calumn_cnt >= 2:
            calumn += 1
            break
            
print(row, calumn)


