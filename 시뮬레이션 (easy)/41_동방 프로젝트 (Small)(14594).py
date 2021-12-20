'''
    맞았습니다!
    꽤 오래 걸린 문제다. 문제 이해는 쉬웠는데 왜인지 모르게 잘 풀리지 않았다.
    그래도 결국엔 맞았습니다!를 받았다.. 다음에 한번 더 풀어보고싶다. 정말 힘겹게 풀었다.

반례
8 
6
5 8
6 7
4 7
5 6
1 3
1 5

1
    방의 개수 : N (2~100)
    행동 횟수 M (0~100)
    동일한 행동을 여러번 할 수 있음 
    x,y : x번방부터 y번방 사이의 벽을 무너뜨림

'''

import sys

lst = [[i] for i in range(0, int(sys.stdin.readline())+1)]

for _ in range(int(sys.stdin.readline())):
    x, y = list(map(int, sys.stdin.readline().split()))
    x_idx, tmp = 0, list()

    for i in range(len(lst)): # x가 포함된 인덱스 찾기(처음 인덱스)
        if x in lst[i]:
            x_idx = i
            break

    for j in range(x+1, y+1):
        idx = 0
        for i in range(len(lst)): 
            if j in lst[i]: 
                tmp = list(set(lst[i]).union(set(lst[x_idx]))) # 이미 합쳐진 원소도 구하기

        for k in tmp:
            if k not in lst[x_idx]: # 처음 인덱스에 없으면
                for item in range(len(lst)):
                    if k in lst[item]:
                        del lst[item] # 기존것을 지우고 
                        break
                lst[x_idx].append(k) # 합치기

print(len(lst)-1)


# 숏코딩 - 와 이런방법도 있구나... 포함되면 0을 주고 1만 세기..

n=int(input())
t=int(input())
a=[1]*n
for i in range(t):
    s,f=map(int,input().split())
    for j in range(s,f):
        a[j]=0
    print(a)
print(a.count(1))

'''
100
6
1 9
1 8
3 10
59 60
4 70
65 95

31

10
2
6 8
1 8

8 
6
5 8
6 7
4 7
5 6
1 3
1 5

1
'''

