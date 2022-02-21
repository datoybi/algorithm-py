'''
특정 노드에서 나머지 노드까지의 최단 거리를 찾아주는 알고리즘
- 다익스트라 알고리즘과 다른 점 : 음의 간선이 포함된 상황에서도 사용 가능 
- 시간복잡도 O(VE)

'''
import math

def balman_ford(num_vertexxes, edges, source):
    distance = [math.inf for i in range(num_vertexxes)]
    distance[source] = 0
    