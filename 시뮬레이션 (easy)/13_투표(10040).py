'''
맞았습니다!
    후보종목 N
    i번째 재미있는 경기는 i번째에 적혀있는 경기
    개최비용 Ai
    조직위원회 M 1~M
    각각의 위원 j는 자신의 심사 기준 B를 가지고 있으며 개최비용이 B를 넘지 않는 경기 중 가장 재미있는 경기에 표를 던졌다
    각 위원의 투표 기준에 해당하는 경기는 반드시 존재 
    가장 많은 표를 획득한 경기는 하나 

    
    가장 많은 표를 획득한 경기의 번호 출력

    N 경기의 수 
    M 위원의 수
    1<= N, M <= 1000
    N개의 줄에는 경기 i를 개최하는데 필요한 비용 A가 주어진다 1<= A <= 1000
    M개의 줄에는 위원 j의 심사 기준 B가 주어진다. (1 <= B <= 1000)
'''
import sys

N, M = list(map(int, sys.stdin.readline().split()))
A = [0] + [int(input()) for _ in range(N)]
B = [0] + [int(input()) for _ in range(M)]
lst = [0 for _ in range(M+2)]

for i in range(1, M+1):
    for j in range(1, N+1):
        if B[i] >= A[j]: 
            lst[j] += 1
            break

for i in range(len(lst)):
    if max(lst) == lst[i]:
        print(i)