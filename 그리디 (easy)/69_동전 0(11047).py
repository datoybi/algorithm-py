'''
맞았습니다!
좀 어렵게 생각했나보다... 조건이 당연히 있어야 한다고 생각했는데 없어도 됐었다

동전은 총 N종류
가치의 합을 K
이때 필요한 동전 개수의 최솟값
N과 K

'''
import sys

N, K = list(map(int, sys.stdin.readline().split()))
lst = list()
for _ in range(N):
    lst.insert(0, int(sys.stdin.readline()))
cnt = 0

for i in range(N):
    cnt += K // lst[i] 
    K = K % lst[i]
print(cnt)