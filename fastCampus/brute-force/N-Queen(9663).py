'''
백트래킹
시간복잡도 : N = 14일때 정답? 21억을 넘는 지 모른다 -> 
일단 int로 정하고 N = 14를 입력으로 넣어 보고 확인하기

N개 중에서 중복을 허용해서 N개를 순서대로 나열하는 모든 경우 탐색하기
시간복잡도 : 14의 14승 -> 10^16

'''
import sys

input = sys.stdin.readline
n = int(input())
col = [0 for _ in range(n)]
ans = 0


def attackable(r1, c1, r2, c2):
    if c1 == c2:
        return True
    if r1 - c1 == r2 - c2:
        return True
    if r1 + c1 == r2 + c2:
        return True
    return False


def rec_func(row):
    if row == n:
        global ans
        ans += 1
    else:
        for cand in range(n):
            possible = True
            for i in range(row):
                if attackable(row, cand, i, col[i]):
                    possible = False
                    break

            if possible:
                col[row] = cand  # ?
                rec_func(row + 1)
                col[row] = 0


rec_func(0)
print(ans)
