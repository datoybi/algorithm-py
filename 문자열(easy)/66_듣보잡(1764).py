'''
    N 듣도 못한 사람 M 보도 못한 사람
    N개 줄에 듣도 못한 사람의 일므 
    N+2 줄에 보도 못한 사람의 이름


    중복 출력

'''


import sys

N, M = map(int, sys.stdin.readline().split())
a,b = list(), list()

for i in range(N):
    a.append(sys.stdin.readline().rstrip())


# 넣은걸 이제.. 있나 판별하고 넣음 어떨까 그럼 조금 나을수도...

for i in range(M): 
    b.append(sys.stdin.readline().rstrip())

result = list()

for i in range(len(a)):
    if a[i] in b:
        result.append(a[i])


result.sort()
print(len(result))
for i in result:
    print(i)