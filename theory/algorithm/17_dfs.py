'''
    깊이 우선 탐색(Depth First Search)
        정점의 자식들을 먼저 탐색하는 방식
        한 노드의 자식을 타고 끝까지 순회한 후, 다시 돌아와서 다른 형제들의 자식을 타고 내려가며 순회함

    bfs와 다른점은 need_visited에서 stack을 사용

    시간복잡도
        노드 수: V
        간선 수: E
            위 코드에서 while need_visit은 V+E번 만큼 수행함
        시간복잡도: O(V+E) 
            간선의 수 + 노드의 수
     
'''
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

def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop() # 맨마지막 데이터 삭제 후 가져오기
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
            
    return visited

print(dfs(graph,'A'))