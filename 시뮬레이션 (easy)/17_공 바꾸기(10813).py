'''
맞았습니다!
    N 바구니개수 , 공이 1개씩 들어있음(처음에는 바구니와 같은 수의 공임)
    M 공을 바꿀 횟수. 바구니 2개를 선택하고 공을 교환
    
'''
import sys

N, M = list(map(int, sys.stdin.readline().split()))
bucket = [[0,0]] + [[i,i] for i in range(1, N+1)]

for i in range(M):
    i, j = list(map(int, sys.stdin.readline().split()))
    bucket[i][1], bucket[j][1] = bucket[j][1], bucket[i][1]  

for i in range(1, len(bucket)):
    print(bucket[i][1], end=' ')
# print(bucket)