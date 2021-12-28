'''
맞았습니다!
신기하게도 시뮬을 확실히 돌리고 진행하니까 바로 맞았습니다 가 떴다!@# 쪼앙
F: 한 눈금 앞으로
B: 한 눈금 뒤로
L: 왼쪽으로 90도 회전
R: 오른쪽으로 90도 회전

L과 R명령을 내렸을 때, 로봇은 이동하지 않고, 방향만 바꾼다.

'''
import sys

dic = {'U' : (0, 1), 'D' : (0, -1), 'R' : (1, 0), 'L' : (-1, 0)}
left = ['U', 'L', 'D', 'R']
right = ['U', 'R', 'D', 'L']

for _ in range(int(sys.stdin.readline())):
    r, c, now = 0, 0, 'U'
    max_r, min_r, max_c, min_c = 0, 0, 0, 0
    lst = list(map(str, sys.stdin.readline().rstrip()))
    
    for i in range(len(lst)):
        if lst[i] == 'F': 
            r += dic[now][0]; c += dic[now][1]
        elif lst[i] == 'B':
            r += -dic[now][0]; c += -dic[now][1]
        elif lst[i] == 'L':
            idx = 0
            for j in range(len(left)):
                if left[j] == now:
                    idx = j
            now = left[(idx + 1) % 4]
        elif lst[i] == 'R':
            idx = 0
            for j in range(len(right)):
                if right[j] == now:
                    idx = j
            now = right[(idx + 1) % 4]
        max_r = max(max_r, r); max_c = max(max_c, c);
        min_r = min(min_r, r); min_c = min(min_c, c)

    print((abs(max_r) + abs(min_r)) * (abs(max_c) + abs(min_c))) # 출력


        


    