'''
BFS(Breadth-First Search) : 너비 우선 탐색 - queue 사용 

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를
모두 큐에 삽입하고 방문처리 합니다.
3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.

'''

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True # 현재 노드 방문 처리
    while queue:
        v = queue.popleft() # 큐에서 하나의 원소를 뽑아 출력하기
        print(v, end=' ')

        for i in graph[v]: # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차언 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)

'''
Bfs VS Dfs 
- 방문 순서에 차이가 있다 . bfs는 냇가에 돌을 던지면 퍼지듯 탐색하고
dfs는 깊이 끝까지 간 뒤 탐색

- 거리 측정은 bfs만 할 수 있다 - 다차원 배열에서 순회하는 문제 ( 최단거리 문제 )
(현재 보는 칸으로부터 추가되는 인접한 칸은 
거리가 현재 보는 칸보다 1만큼 더 떨어져 있다)

- 그래프와 트리라는 자료구조를 배울 때 dfs를 사용

- 탐색 깊이가 정해져 있지 않다면 DFS 사용 불가


'''