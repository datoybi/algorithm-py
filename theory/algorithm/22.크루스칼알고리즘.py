'''
크루스칼 알고리즘 (kruskal's algorithm)
    1. 모든 정점을 독립적인 집합으로 만든다.
    2. 모든 간선을 비용을 기준으로 정렬하고, 비용이 적은 간선부터 양 끝의 두 정점을 비교한다.
    3. 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다 (최소신장트리는 사이클이 없으므로, 사이클이 생기지 않도록 하는 것임)
    (탐욕 알고리즘을 기초로 하고 있음 - 당장 눈 앞의 최소 비용을 선택해서, 결과적으로 최적의 솔루션을 찾음)

Union-Find 알고리즘
    Disjoint Set을 표현할 때 사용하는 알고리즘으로 트리 구조를 활용하는 알고리즘
    간단하게, 노드들 중에 연결된 노드를 찾거나, 노드들을 서로 연결할 때 사용 
    Disjoint Set이란
        서로 중복되지 않는 부분 집합들로 나눠진 원소들에 대한 정보를 저장하고 조직하는 자료구조
        공통 원소가 없는 (서로소) 상호 배타적인 부분 집합들로 나눠진 원소들에 대한 자료구조를 의미함
        Disjoint set - 서로소 집합 자료구조

        1. 초기화 : n개의 원소가 개별 집합으로 이뤄지도록 초기화
        2. Union : 두 개별 집합을 하나의 집합으로 합침, 두 트리를 하나의 트리로 만듦
        3. find : 여러 노드가 존재할 때, 두개의 노드를 선택해서, 현재 두 노드가 서로 같은 그래프에 속하는지 판별하기 위해, 각 구릅의 최상단 원소(즉, 루트노드)를 확인

Union-by-rank 기법
    각 트리에 대해 높이(rank)를 기억해두고, 
    Union시 두 트리의 높이(rank)가 다르면, 높이가 작은 트리를 높이가 큰 트리에 붙임 (즉, 높이가 큰 트리의 루트 노드가 합친 집합의 노드가 되게 함)

Path compression
    find를 실행한 노드에서 거쳐간 노드를 루트에 다이렉트로 연결하는 기법
    Find를 실행한 노드는 이후부터는 루트 노드를 한번에 알 수 있음
'''

mygraph = {
    'vertices': ['A','B','C','D','E','F','G'],
    'edges' : [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

edges = mygraph['edges']
edges.sort()
print(edges) # [(5, 'A', 'D'), (5, 'C', 'E'), (5, 'D', 'A'), (5, 'E', 'C'), (6, 'D', 'F'), (6, 'F', 'D'), (7, 'A', 'B'), (7, 'B', 'A'), (7, 'B', 'E'), (7, 'D', 'E'), (7, 'E', 'B'), (7, 'E', 'D'), (8, 'B', 'C'), (8, 'C', 'B'), (8, 'E', 'F'), (8, 'F', 'E'), (9, 'B', 'D'), (9, 'D', 'B'), (9, 'E', 'G'), (9, 'G', 'E'), (11, 'F', 'G'), (11, 'G', 'F')]

parent = dict()
rank = dict()

def find(node):
    #path compression
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)
    
    # union-by-rank 기법
    if rank[root1]> rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(mygraph):
    mst = list()

    # 1. 초기화
    for node in mygraph['vertices']:
        make_set(node)

    # 2. 간선 weight 기반 sorting
    edges = mygraph['edges']
    edges.sort()
    # print(edges) # [(5, 'A', 'D'), (5, 'C', 'E'), (5, 'D', 'A'), (5, 'E', 'C'), (6, 'D', 'F'), (6, 'F', 'D'), (7, 'A', 'B'), (7, 'B', 'A'), (7, 'B', 'E'), (7, 'D', 'E'), (7, 'E', 'B'), (7, 'E', 'D'), (8, 'B', 'C'), (8, 'C', 'B'), (8, 'E', 'F'), (8, 'F', 'E'), (9, 'B', 'D'), (9, 'D', 'B'), (9, 'E', 'G'), (9, 'G', 'E'), (11, 'F', 'G'), (11, 'G', 'F')]
    
    # 3. 간선 연결 (사이클 없는)
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)


    return mst


kruskal(mygraph)

'''
    시간복잡도
        크루스컬 알고리즘의 시간 복잡도는 O(E log E)

'''