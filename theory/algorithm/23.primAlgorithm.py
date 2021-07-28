'''
프림 알고리즘 (Prim Algorithm)
    시작 정점을 선택한 후, 정점에 인접한 간선중 최소 간선으로 연결된 정점을 선택하고, 해당 정점에서 다시 최소 간선으로 연결된 정점을 선택하는 방식으로 
    최소 신장 트리를 확장해가는 방식
    탐욕 알고리즘을 기초로 하고 있음




'''
# heapq 라이브러리 활용을 통해 우선순위 큐 사용하기
'''
import heapq
queue = []
graph_data =[[2,'A'],[5,'B'],[3,'C']]

for edge in graph_data:
    heapq.heappush(queue, edge)

for index in range(len(queue)):
    print(heapq.heappop(queue))

print(queue)
'''

import heapq

graph_data =[[2,'A'],[5,'B'],[3,'C']]
heapq.heapify(graph_data)

for index in range(len(graph_data)):
    print(heapq.heappop(graph_data))

print(graph_data) # []


from collections import defaultdict
list_dict = defaultdict(list) # int float set list ...
print(list_dict['key1'])

