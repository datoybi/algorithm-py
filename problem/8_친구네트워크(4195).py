"""
    제목 : 친구 네트워크
    난이도 : 중
    유형 : 해시, 집합, 그래프
    시간 : 50분
    느낀점 : 잘 모르겠음 ㅠ union 알고리즘이나 중급 난이도의 알고리즘이니 초보들은 힘들수도 있다고 한다. 다음에 한번 더 풀어보기로 하자
"""

"""
    문제풀이 핵심 아이디어
    1. 해시를 활용한 Union-Find(합집합 찾기) 알고리즘을 이용해 문제를 풀 수 있습니다.
    2. Python에서는 dictonary 자료형을 해시처럼 사용할 수 있습니다.
"""

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x!= y:
        parent[y] = x
        number[x] += number[y]

test_case = int(input())

for _ in range(test_case):
    parent = dict()
    number = dict()
    
    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)
        print(number[find(x)])
            