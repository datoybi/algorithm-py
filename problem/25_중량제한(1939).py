'''
    제목 : 중량제한
    난이도 : 중상 - 대회에 나올법한 문제
    유형 : 이진 탐색
    시간 : 1시간 
    문제 풀이 핵심 아이디어
        다리의 개수 M은 최대 100.000이며, 중량 제한 C는 최대 1,000,000,000입니다. - (이걸 보고 일반적인 방법으로는 풀기 힘들고 로그라던지 루트를 사용할 껀덕지가 있지 않을까? 라는 의심을 해야한다, 실제로 이 문제에서는 C에 로그를 씌워야 함) 
        이진 탐색을 이용하여 O(M*logC)에 문제를 해결할 수 있습니다.
        한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 이진 탐색으로 찾습니다. 
    bfs 사용 - 간선의 갯수 만큼 시간복잡도 파악 가능
'''

from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)] # 무슨 뜻인지 찾아보기 

def bfs(c): # bfs 수행 - 경로가 있는지 확인하는 코드
    queue = deque([start_node])
    visited = [False] * (n + 1)
    visited[start_node] = True
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]

start = 100000000
end = 1

for _ in range(m):
    x, y, weight = map(int, input().split())
    adj[x].append((y, weight))
    adj[y].append((x, weight))
    start = min(start, weight)
    end = max(end, weight) 

start_node, end_node = map(int, input().split()) 

result = start
while(start <= end): # 이진탐색 수행
    mid = (start + end) // 2 # mid는 현재의 중량을 의미합니다 
    if bfs(mid): # 이동이 가능하므로, 중량을 증가시킵니다.
        result = mid
        start = mid+1
    else:
        end = mid - 1
print(result)




