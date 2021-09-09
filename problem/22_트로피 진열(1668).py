'''
    제목 : 트로피 진열
    난이도 : 하
    유형 : 탐색
    시간 : 20분
    문제 풀이 핵심 아이디어 
        선반 위에 올려져 있는 트로피들에 대하여 왼쪽에서, 오른쪽에서 봤을 때 보이는 
        트로피의 수를 각각 구합니다.
        트로피의 개수 N이 최대 50이므로 단순히 구현하면 됩니다.

'''

def ascending(array):
    result = 1
    now = array[0]
    for i in range(1, len(array)):
        if now < array[i]:
            result += 1
            now = array[i]
    return result;

n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

print(ascending(array))
array.reverse()
print(ascending(array))