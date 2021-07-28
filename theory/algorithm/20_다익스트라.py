# 우선순위 큐를 아용한 다익스트라 알고리즘
# 다시 보기

# 우선순위 큐 만들기
import heapq

queue = []
heapq.heappush(queue, [2,'A'])
heapq.heappush(queue, [5,'B'])
heapq.heappush(queue, [1,'C'])
heapq.heappush(queue, [7,'D'])

# sorting 된것 처럼 보이지는 않지만 데이터를 끄집어 낼 때 가장 작은 값을 가져옴
print(queue) #[[1, 'C'], [5, 'B'], [2, 'A'], [7, 'D']]

for index in range(len(queue)):
    print(heapq.heappop(queue))
'''
[1, 'C']
[2, 'A']
[5, 'B']
[7, 'D']
'''

mygraph = {
    'A': {'B':8, 'C':1, 'D':2},
    'B': {},
    'C': {'B':5, 'D':2},
    'D': {'E':3, 'F':5},
    'E': {'F':1},
    'F': {'A':5}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph} # 무한(inf)로 graph 초기화
    #print("distances : " , distances)
    distances[start] = 0 # 자기자신('A')은 0으로 초기화
    queue = []
    heapq.heappush(queue, [distances[start], start]) # 초기화 distance, node, heappush(삽입할 큐, 삽입할 것) 

    while queue:
        current_distance, current_node = heapq.heappop(queue) 

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            print("**" , adjacent, weight)
            distance = current_distance + weight

            if distance < distances[adjacent]: #지금 찾은 값 보다 더 크다면
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    return distances

print(dijkstra(mygraph, 'A'))

'''
    시간복잡도
        과정
            1. 각 노드마다 인접한 간선들을 모두 검사하는 과정
            2. 우선순위 큐에 노드/거리 정보를 넣고 삭제(pop)하는 과정
        각 과정별 시간복잡도
            1. 각 노드는 최대 한번 씩 방문
                즉, 각 노드마다 인접한 간선들을 모두 검사하는 과정은 O(E), E는 간선(Edge)의 약자
            2. 우선순위 큐에 가장 많은 노드, 거리 정보가 들어가는 경우, 우선순위 큐에 노드/거리 정보를 넣고, 삭제하는 과정이 최악의 시간이 걸림
                이 때 추가는 각 간선마다 최대 한 번 일어날 수 있으므로, 최대 O(E)의 시간이 걸리고, 
                O(E) 개의 노드/거리정보에 대해 우선순위 큐를 유지하는 작업은 O(logE)가 걸림
                따라서 해당 과정의 시간복잡도는 O(ElogE)
            총 시간복잡도 : O(ElogE)

'''




