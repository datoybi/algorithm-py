import sys
sys.setrecursionlimit(10000) # 파이썬 기본 재귀도는 횟수 늘리기

for _ in range(int(input())):
    n, m, k = map(int, input().split()) # 입력
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1 # 해당 좌표 1로 변경

    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1] # 상하좌우
    cnt = 0

    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m: # 좌표를 벗어나면
            return False
        if graph[x][y] == 1: # 이걸로 visited count
            graph[x][y] = 0 # 0으로 변경
            for i in range(4):
                dfs(x + dx[i], y + dy[i])
            return True
        return False    

    for i in range(n): # 모든 좌표 순회
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1
    
    print(cnt)