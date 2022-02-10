'''
맞았습니다!
그래도 얼추 이해가 되어서 다행이다. 이 문제는 dfs나 bfs를 사용하지 않은 것 같다.
첫문제부터 어렵다 어떻게 적용을 시켜야 할지 모르겠따.ㅜㅜ 점점 나아지겠지..
위 문제는 양 또는 늑대가 상하좌우로 움직 일 수 있는데 양이 있는 칸으로 이동하지 못하게
울타리를 설치하는 것이다.
울타리의 최소값을 구하는 것이 아니기 때문에 모든 땅에 울타리를 설치해도된다.

접근법
1. 모든 좌표를 탐색
 1-1. 늑대(W)일 경우, 상하좌우를 탐색하여 인접한 곳에 양이 있으면 flag를 false로 변경 
 1-2. 양(S)인 경우, 넘어감
 1-3. 빈칸인 경우, 모두 울타리로 채워줌

2. flag가 True인 경우 0을 출력 
    flag False인 경우 1을 출력하고 maps도 출력

'''

n, m = map(int, input().split())
lst = [list(input()) for _ in range(n)]

flag = False # 늑대에게 필연적으로 잡아먹히는지 아닌지 탐색
for i in range(n):
    for j in range(m):
        if lst[i][j] == 'W': # 늑대이면
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and lst[nx][ny] == 'S':  # 상하좌우 범위안의 좌표가 S면
                    flag = True
                    break

        elif lst[i][j] == 'S': # 양이면
            continue

        elif lst[i][j] == '.': # . 이면
            lst[i][j] = 'D'

if flag == True:
    print(0)
else:
    print(1)
    for i in lst:
        print(''.join(i))


'''
n, m = map(int,input().split())
grid = [input().replace('.', 'D') for i in range(n)]
for s in grid + [ * zip ( * grid)]:
    s = ''.join(s)
    if 'SW' in s or 'WS' in s: print(0); break
else:
    print(1)
    print(*grid, sep='\n')

'''