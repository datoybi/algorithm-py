'''
건물의 개수 N, 가희가 볼 수 있는 건물의 개수 a, 단비가 볼 수 있는 건물의 개수 b
'''
import sys

N, a, b = list(map(int, sys.stdin.readline().split()))
front = [i for i in range(1, a+1)]
back = [i for i in range(b, 0, -1)]

if N == a:
    for i in range(len(front)):
        print(front[i], end = ' ')
else:
    value = str(max(front[-1], back[0]))
    del front[-1]
    del back[0]
    cnt = len(front) + len(back)
    add = ''
    for _ in range(N-cnt):
        add += ' ' + value
    result = ''
    for i in range(len(front)):
        result += ' ' + front[i]
    result += add
    for i in range(len(back)):
        result += ' ' + back[i]
        
    print(result)
    

