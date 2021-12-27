# 맞았습니다!
# 문제 그대로 풀면 됐던 문제

import sys

# 입력
R,C = list(map(int, sys.stdin.readline().split()))
lst, result = list(), list()
check = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for i in range(R):
    lst.append(sys.stdin.readline().rstrip())    

# 연산
for i in range(R):
    tmp = ''
    for j in range(C):
        count = 0
        if lst[i][j] == 'X':
            for z in range(4): # 상하좌우 체크
                row, cal = i + check[z][0], j + check[z][1] 
                if row < 0 or cal < 0 or row >= R or cal >= C: # 범위 밖을 넘어가면 .으로 세기
                    count += 1
                else:
                    if lst[row][cal] == '.':
                        count += 1
        if count >= 3:
            tmp += '.'
        else:
            tmp += lst[i][j]
    result.append(tmp)

# 출력
min_row, max_row, min_cal, max_cal = R, 0, C, 0
for i in range(R):
    for j in range(C):
        if result[i][j] == 'X':
            min_row = min(min_row, i)
            max_row = max(max_row, i)
            min_cal = min(min_cal, j)
            max_cal = max(max_cal, j)

for i in range(min_row, max_row+1):
    for j in range(min_cal, max_cal+1):
        print(result[i][j], end="")
    print()
