'''
N개 중 중복없이 M를 순서 있게 나열하기

시간복잡도 못구하겠음..
시간복잡도 : 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40,320 (1억보다 작으니 1초안에 가능)
공간복잡도 M

'''

# 내코드
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
selected = [0 for _ in range(M)]

def solution(k):
    if k == M:
        print(' '.join(selected))
    else:
        for i in range(1, N+1):
            if str(i) not in selected:
                selected[k] = str(i) 
                solution(k + 1)
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
        for cand in range(1, n + 1):
            if used[cand]:
                continue
            selected[k] = cand
            used[cand] = 1
            rec_func(k + 1)
            selected[k] = 0
            used[cand] = 0

rec_func(0)
