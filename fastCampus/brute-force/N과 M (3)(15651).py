'''
    N개 중 중복을 허용해서 M개를 순서있게 나열하기
    https://www.acmicpc.net/problem/15651

    1. 문제를 이해하기 
        N=4, M=3 일때, 1 1 1, 1 1 2, 1 1 3, 1 1 4 하고 1 2 1 부터 시작함.. 이런 논리
    2. 시간복잡도, 공간복잡도 계산
        시간복잡도
            4x4x4 = 4^3 = 64
            O(N의 M승) = 7의 7승 => 82만 (최악의 경우)
        공간복잡도
            O(M)

    3. 구현 스캐치
        N, M
        selected = []
        # Recurrence Function (재귀 함수)
        # 만약 M개를 전부 고름 => 조건에 맞는 탐색을 한 가지 성공한 것!
        # 아직 M개를 고르지 않음 => k번째부터 M번째 원소를 조건에 맞게 고르는 모든 방법을 시도한다.

        def rec_func(x):
            if(k == M + 1): # 다 골랐다면
                ... # selected[1...M] 배열이 새롭게 탐색된 결과
            else:
                ... # 1~N 까지를 k번 원소로 한 번씩 정하고,
                    # 매번 k+1번 부터 M번 원소로 재귀호출 해주기

'''
 
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split(' '))
# selected = [0 for _ in range(m)]
# print(selected)
# # [0, 0, 0]
# # [0, 0, 0, 0, 0]
# def rec_func(k):
#     if k == m:
#         for x in selected:
#             sys.stdout.write(str(x) + ' ')
#         sys.stdout.write('\n')
#     else:
#         for cand in range(1, n+1): # 1 ~ 4
#             selected[k] = cand
#             print('selected[k] : ' , selected[k])
#             print('k : ' , k , ' , cand :' , cand)
#             rec_func(k + 1)
#             selected[k] = 0

# rec_func(0)

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
selected = [0 for _ in range(m)]

def solution(k):
    if k == m :
        print(' '.join(selected))
    else:
        for i in range(1, n+1):
            selected[k] = str(i)
            solution(k + 1)

solution(0);