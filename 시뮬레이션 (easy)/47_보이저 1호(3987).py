'''
맞았습니다!
어려웠다 이거.. 까다롭..  

/\은 행성을 나타낸다
.은 빈칸을 나타낸다

U:위, R:오른쪽, D:아래, L:왼쪽
만약, 방향이 여러 가지가 존재한다면, U, R, D, L의 순서 중 앞서는 것을 출력한다.

5 5 N행, M열 
블랙홀이 있는 칸을 만나거나 벗어날 때까지 계속 전파
어느 방향으로 시그널을 보내면, 시그널이 항성계 내부에 있는 시간이 최대가 되는지 구하기 

처리해준 것
\\ 처리를 해줘야할 것 같다. 다른 기호같은걸로 .. ->?로 치환
두자리라서 애매해진다.

무한반복되는거 어떻게 처리할 지 생각해보기 -> N*M 보다 count가 크면(왠진 모른데 그렇다고 한다)
카운트가 500인것보다 더 좋은 방법이 있는지..
'''
import sys

N, M = list(map(int, sys.stdin.readline().split()))
lst = list()
for i in range(N):
    lst.append(str(sys.stdin.readline().rstrip()))
PR, PC = list(map(int, sys.stdin.readline().split()))

r,c = PR-1, PC-1
count_lst = list()
tc, key, count  = 0, 'u', 1
direction = {'u': [-1,0], 'r': [0,1], 'd': [1,0], 'l': [0,-1]}

for i in range(len(lst)): # \\를 ?로 바꾸기
    lst[i] = lst[i].replace('\\', '?')

while tc < 4:
    # print('전', key, r,c , lst[r][c], count)

    r += direction[key][0]
    c += direction[key][1]

    if count > 500000: # 무한일때 
        r,c = PR-1, PC-1
        count_lst.append('Voyager')
        tc += 1
        count = 1
        if tc == 4: break
        key = list(direction.keys())[tc]
    
    if r < 0 or r >= N or c < 0 or c >= M : # 범위를 초과하면
        # print('next')
        r,c = PR-1, PC-1
        count_lst.append(count)
        count = 1
        tc += 1
        if tc == 4: break
        key = list(direction.keys())[tc]
    else:
        if lst[r][c] == 'C': # 블랙홀을 만나면
            # print('next')
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
        elif lst[r][c] == '?':
            if key == 'u': 
                key = 'l'
            elif key == 'r':
                key = 'd'
            elif key == 'l':
                key = 'u'
            elif key == 'd':
                key = 'r'
            count += 1
    # print('후 ', key, r,c , lst[r][c], count)
    
# 출력
idx = 0
if 'Voyager' in count_lst:
    idx = count_lst.index('Voyager')
else:
    idx = count_lst.index(max(count_lst))

if idx == 0:
    print('U')
elif idx == 1:
    print('R')
elif idx == 2:
    print('D')
elif idx == 3:
    print('L')
print(count_lst[idx])
