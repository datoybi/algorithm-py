'''
맞았습니다!

j개의 사탕
상자 N개

T (1 <= T <= 10)
사탕의 개수 j, 상자의 개수 N (1 <= j, N <= 1000)
N개의 줄에 걸쳐
상자의 세로길이 R, 가로길이 C
'''

import sys

for _ in range(int(sys.stdin.readline())):
    candy, N = list(map(int, sys.stdin.readline().split()))
    capacity = list()
    
    for i in range(N):
        R, C = list(map(int, sys.stdin.readline().split()))
        capacity.append(R * C)

    capacity.sort(reverse=True)
    count = 0

    for i in range(len(capacity)):
        if candy <= 0:
            break
        else:
            candy -= capacity[i] 
            count += 1
    
    print(count)