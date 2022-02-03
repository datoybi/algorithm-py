
n = int(input())
dp = [0] * (n+2) # 이렇게 해도 되는 이유는 int형이니까
dp[0] = dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2] + 1

print(dp[n] % 1000000007)