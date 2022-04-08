'''
    N개중 중복없이 M개를 고르기
    시간복잡도 : 8*7 = 70
    젤 큰값은 N=8, M=4일때


'''

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
selected = [0 for _ in range(M)]

def solution(k):
    if k == M:
        for x in selected:
            print(x, end = ' ')
        print()
    else:
        for i in range(1, N+1):
            if i > max(selected):
                selected[k] = i
                solution(k+1)
                selected[k] = 0

solution(0)


# 강사코드
import sys
n, m = map(int, sys.stdin.readline().split(' '))

selected = [0 for _ in range(m)]
used = [0 for _ in range(n + 1)]
def rec_func(k):
    if k == m:
        for x in selected:
            sys.stdout.write(str(x) + ' ')
        sys.stdout.write('\n')
    else:
        start = 1 if k == 0 else selected[k - 1] + 1
        for cand in range(start, n + 1):
            selected[k] = cand
            rec_func(k + 1)
            selected[k] = 0

rec_func(0)