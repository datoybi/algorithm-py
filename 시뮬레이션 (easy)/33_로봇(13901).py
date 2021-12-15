'''
맞았습니다!

방의 크기 R, C (3~1000)
장애물 개수 k (0~1000)
k개 줄에는 
    장애물의 위치 br(0<= br <= R-1)
    장애물의 위치 bc(0<= bc <= C-1)
로봇의 시작위치
이동방향의 순서(1-위, 2-아래, 3-왼쪽, 4-오른쪽)

반례    
4 3
1
1 2
2 1
1 2 3 4
답 2 2
'''

import sys
# 입력
R, C = list(map(int, sys.stdin.readline().split()))
k = list()
lst = list()

for _ in range(int(sys.stdin.readline())):
    br, bc = list(map(int, sys.stdin.readline().split())) # 장애물 위치 담기
    k.append([br, bc])

sr, sc = list(map(int, sys.stdin.readline().split())) # 로봇 시작 위치
move = list(map(int, sys.stdin.readline().split())) # 움직이는 순서

for r in range(R): # 발판 만들기
    tmp = list()
    for c in range(C):
        tmp.append('*')
    lst.append(tmp)

for i in range(len(k)): # 장애물 위치에 x 표시 하기
    lst[k[i][0]][k[i][1]] = 'x'

# print(lst)
# 계산 
now_r, now_c = sr, sc
i, idx_move, count = 0, 0, 0

while count < 5:
    lst[now_r][now_c] = i
    idx_move = idx_move % 4
    # print('idx_move : ' , idx_move)
    # print('move : ' , move[idx_move])
    # print('좌표 : ' , now_r, now_c)
    # print(lst)
    # print('count : ' , count)

    if move[idx_move] == 1: # 상
        if now_r-1 < 0 or lst[now_r-1][now_c] != '*':
            idx_move += 1
            count += 1
            continue
        else:
            now_r -= 1   
            i += 1   
            count = 0
    elif move[idx_move] == 2: # 하
        if now_r+1 > R-1 or lst[now_r+1][now_c] != '*':
            idx_move += 1
            count += 1
            continue
        else:
            count = 0
            now_r += 1
            i += 1   
    elif move[idx_move] == 3: # 좌
        if now_c-1 < 0 or lst[now_r][now_c-1] != '*':
            idx_move += 1
            count += 1
            continue
        else:
            now_c -= 1
            i += 1   
            count = 0
    elif move[idx_move] == 4: # 우
        if now_c+1 > C-1  or lst[now_r][now_c+1] != '*':
            idx_move += 1
            count += 1
            continue
        else:
            now_c += 1
            i += 1   
            count = 0

print(now_r, now_c)    


    


    

