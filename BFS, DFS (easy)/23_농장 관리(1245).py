'''
1. 격자형 그래프로 표현하기
    그래프로 표현하다 == 정점과 간선을 정의한다
2. 산봉우리를 그래프에서 연결 요소로 나타내기
3. 그래프 연결 요소로 정답 계산하는 방법 찾기
4. 연결 요소를 찾기 위한 "그래프 탐색" 필요
5. 그래프 탐색을 하는 알고리즘 필요
6. BFS 또는 DFS 필요
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 3)

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
print(graph)
print(visited)

flag = True
cnt = 0

def dfs(x, y):    
    global flag
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    visited[x][y] = True

    for k in range(8):
        nx, ny = dx[k] + i, dy[k] + j
        if 0 <= nx < N and 0 <= ny < M :
            if graph[i][j] > graph[nx][ny]:
                flag = False
            if graph[i][j] == graph[nx][ny] and not visited[nx][ny]: 
                dfs(nx, ny)

for i in range(N):
    for j in range(M):
        if graph[i][j] > 0 and not visited[i][j]:
            flag = True
            dfs(i, j)
        if flag:
            cnt += 1

print(cnt)
