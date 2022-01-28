'''
dp[1] = 1
dp[2] = dp[1] + 1 = 2
dp[3] = dp[2] + 1 = 3
dp[4] = dp[2*2] = 1
dp[5] = dp[4] + 1 = 2
dp[6] = dp[4] + dp[2] = 3
dp[7] = dp[4] + dp[3] = 4
dp[8] = dp[4] + dp[4] = 2

점화식 
dp[i] = dp[i - j * j] + dp[j * j]



'''
import sys, math

dp = [50001 for _ in range(51)]
dp[1] = 1
N = int(sys.stdin.readline())

for i in range(2, N+1): 

    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + dp[j * j])
        
print(dp[25])
