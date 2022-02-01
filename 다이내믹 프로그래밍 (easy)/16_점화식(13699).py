# 맞았습니다!
import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)]
dp[0] = 1

for i in range(1, n+1):
    value = 0
    for j in range(i):
        value += dp[j] * dp[i-j-1]
    dp[i] = value
print(dp[n])


'''
t(n) = t(0) * t(n-1) + t(1) *t(n-2) + ... + t(n-1) * t(0)
t(0) = 1
t(1) = t(0) * t(0) = 1
t(2) = t(0) * t(1) + t(1) * t(0) = 1 + 1 = 2 
t(3) = t(0) * t(2) + t(1) * t(1) + t(2) * t(0) = 2 + 1 + 2 = 5
t(4) = t(0) * t(3) + t(1) * t(2) + t(2) * t(1) + t(3) * t(0) = 5 + 2 + 2 + 5 = 14
t(5) = t(0) * t(4) + t(1) * t(3) + t(2) * t(2) + t(3) * t(1) + t(4) * t(0) = 14 + 5 + 4 + 5 + 14 = 42
t(6) = t(0) * t(5) + t(1) * t(4) + t(2) * t(3) + t(3) * t(2) + t(4) * t(1) + t(5) * t(0) = 42 + 14 + 10 + 10 + 14 + 42 =  132


t(0) = 1; t(1) = 1
t(2) = t(1) + t(1)
t(3) = t(2) + t(1) + t(2)
t(4) = t(3) + t(2) + t

'''