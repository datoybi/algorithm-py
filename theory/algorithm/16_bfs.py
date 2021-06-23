'''
    너비 우선 탐색 (Breadth First Search)
        대표적인 그래프 탐색 알고리즘 
        정점들과 같은 레벨에 있는 노드들(현재 노드들)을 먼저 탐색하는 방식
        한 단계씩 내려가면서, 해당 노드와 같은 레벨에 있는 노드들(형제 노드들)을 먼저 순회함

    깊이 우선 탐색 (Depth First Search)
        정점의 자식들을 먼저 탐색하는 방식
        한 노드의 자식을 타고 끝까지 순회한 후, 다시 돌아와서 다른 형제들의 자식을 타고 내려가며 순회함
'''

# dictinary를 통해서 지정 노드를 key로 인접 정점을 value로 놓기
graph = dict()

graph['A'] = ['B','C'] # key, value
graph['B'] = ['A','D']
graph['C'] = ['A','G','H','I']
graph['D'] = ['B','E','F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C','J']
graph['J'] = ['I']

#print(graph)
'''
{
    'A': ['B', 'C'], 
    'B': ['A', 'D'], 
    'C': ['A', 'G', 'H', 'I'], 
    'D': ['B', 'E', 'F'], 
    'E': ['D'], 
    'F': ['D'], 
    'G': ['C'], 
    'H': ['C'], 
    'I': ['C', 'J'], 
    'J': ['I']
}

'''

#need_visit, visited 큐 생성
# A부터 visited에 넣고 A의 value는 need_visit에 넣는다. 그리고 need_visited에서 하나 가져와서 visited에 있는 지 없는지 비교한다.
# 있으면 아무것도 안하고 다음것(B)가져오기, 없으면 visited에 삽입 

def bfs(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0) # 특정 인덱스 번호를 뺴오고 뒤에서 앞으로 채움
        if node not in visited: # 노드가 visited에 있는지 없는지 판별 
            visited.append(node) # visited에 node 삽입
            need_visit.extend(graph[node]) # extend : 리스트 뒤에 리스트를 이어 붙이기, node의 value값을 need_visited에 삽입
    return visited

print(bfs(graph, 'A'))


'''
    시간복잡도
        노드 수: V
        간선 수: E
            위 코드에서 while need_visit은 V+E번 만큼 수행함
        시간복잡도: O(V+E) 
            간선의 수 + 노드의 수
'''