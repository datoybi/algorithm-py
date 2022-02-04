# 맞았습니다!
#  n! / ((n - m)! * m!) = 1
n, m = map(int, input().split())
dp = [0 for i in range(101)]
dp[1] = 1
for i in range(2, 101):
    dp[i] = dp[i-1] * i 

print(int(dp[n] // (dp[n-m] * dp[m])))