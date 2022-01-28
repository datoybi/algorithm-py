
import sys

dp = list()
n, k = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    tmp = list()
    for j in range(i+1):
        tmp.append(1)
    dp.append(tmp)

if n >= 2:
    dp[0][0] = 1; dp[1][0] = 1; dp[1][1] = 1
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            
print(dp[n-1][k-1])
