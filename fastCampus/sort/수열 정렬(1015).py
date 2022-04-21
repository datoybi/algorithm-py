'''
    단순히 모든 N들을 순회하며 하면 시간복잡도 N*N,
    최대값은 N이 최대 50까지니까 50*50 = 2500초 1초에 1억번 연산이니까 가능하다.
'''
# 내 코드 (N제곱)
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
P = []

print(B)
for i in range(N):
    for j in range(N):
        if A[i] == B[j]:
            P.append(j)
            B[j] = 0
            break

for p in P:
    print(p, end=" ")

'''
배열 정렬 : 정렬은 O(N log N)
    p 배열 구하기 (순서대로 채우면 O(N))
    복잡도
        시간복잡도 : O(N log N)
        공간복잡도 : O(N)

'''

'''
강사코드 - NlogN이다

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
B = [(x, i) for i, x in enumerate(a)]
B.sort()
P = [0 for _ in range(n)]
for i in range(n):
    P[B[i][1]] = i
for i in range(n):
    print(P[i], ' ')

'''
