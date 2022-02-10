'''
dfs를 활용하는 알고리즘 
1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 0이면서
아직 방문하지 않은 지점이 있다면 해당 지점을 방문합니다.
2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면,
연결된 모든 지점을 방문할 수 있습니다.
3. 모든 노드에 대하여 1~2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트 합니다.

'''

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m: # 범위를 벗어나면 
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input()))) # 입력

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1 # ?

print(result)