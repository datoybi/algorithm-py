'''
/\은 행성을 나타낸다
.은 빈칸을 나타낸다

U:위, R:오른쪽, D:아래, L:왼쪽
만약, 방향이 여러 가지가 존재한다면, U, R, D, L의 순서 중 앞서는 것을 출력한다.

5 5 N행, M열 
블랙홀이 있는 칸을 만나거나 벗어날 때까지 계속 전파
어느 방향으로 시그널을 보내면, 시그널이 항성계 내부에 있는 시간이 최대가 되는지 구하기 

'''
import sys

N, M = list(map(int, sys.stdin.readline().split()))
lst = list()
for i in range(N):
    lst.append(str(sys.stdin.readline().rstrip()))
PR, PC = list(map(int, sys.stdin.readline().split()))

print(lst)
r,c = PR-1, PC-1
print(lst[r][c])
count_lst = list()
tc = 0
direction = {'u': [-1,0], 'r': [0,1], 'd': [1,0], 'l': [0,-1]}
# print(direction['u'])
key = 'u'
count = 1

for i in range(50): # while true
    print('전', key, r,c , lst[r][c], count)

    r += direction[key][0]
    c += direction[key][1]

    if count == 500: 
        print('Voyager')
        exit(0)
    
    if r < 0 or r >= N or c < 0 or c >= M : # 범위를 초과하면
        print('next')
        r,c = PR-1, PC-1
        count_lst.append(count)
        count = 1
        tc += 1
        if tc == 4: break
        key = list(direction.keys())[tc]
    else:
        if lst[r][c] == 'C': # 블랙홀을 만나면
            print('next')
            r,c = PR-1, PC-1
            count_lst.append(count)
            count = 1
            tc += 1
            if tc == 4: break
            key = list(direction.keys())[tc]
        elif lst[r][c] == '.':
            count += 1
        elif lst[r][c] == '/':
            if key == 'u': 
                key = 'r'
            elif key == 'r':
                key = 'u'
            elif key == 'l':
                key = 'd'
            elif key == 'd':
                key = 'l'
            count += 1
        elif lst[r][c] == '\\':
            if key == 'u': 
                key = 'l'
            elif key == 'r':
                key = 'd'
            elif key == 'l':
                key = 'u'
            elif key == 'd':
                key = 'r'
            count += 1

    print('후 ', key, r,c , lst[r][c], count)

print(count_lst)